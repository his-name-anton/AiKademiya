import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { authApi } from '@/api/auth';
import type { User, AuthTokens, LoginCredentials, RegisterData } from '@/types';

export const useAuthStore = defineStore('auth', () => {
  // State
  const user = ref<User | null>(null);
  const accessToken = ref<string | null>(localStorage.getItem('access_token'));
  const refreshToken = ref<string | null>(localStorage.getItem('refresh_token'));
  const isLoading = ref(false);
  const isInitialized = ref(false);
  const tokenRefreshTimer = ref<number | null>(null);
  const inactivityTimer = ref<number | null>(null);
  const lastActivityTime = ref<number>(Date.now());

  // Getters
  const isAuthenticated = computed(() => !!accessToken.value && !!user.value);
  const token = computed(() => accessToken.value);
  const userEmail = computed(() => user.value?.email);
  const userName = computed(() => {
    if (!user.value) return '';
    return user.value.firstName && user.value.lastName
      ? `${user.value.firstName} ${user.value.lastName}`
      : user.value.email;
  });

  // Helper function to check if token is expired
  function isTokenExpired(token: string): boolean {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      const currentTime = Date.now() / 1000;
      return payload.exp < currentTime;
    } catch {
      return true;
    }
  }

  // Helper function to get token expiration time
  function getTokenExpirationTime(token: string): number {
    try {
      const payload = JSON.parse(atob(token.split('.')[1]));
      return payload.exp * 1000; // Convert to milliseconds
    } catch {
      return 0;
    }
  }

  // Helper function to set up automatic token refresh
  function setupTokenRefreshTimer(): void {
    // Clear existing timer
    if (tokenRefreshTimer.value) {
      clearTimeout(tokenRefreshTimer.value);
    }

    if (!accessToken.value) return;

    const expirationTime = getTokenExpirationTime(accessToken.value);
    const currentTime = Date.now();
    const timeUntilExpiration = expirationTime - currentTime;

    // Refresh token 5 minutes before expiration
    const refreshTime = Math.max(timeUntilExpiration - 5 * 60 * 1000, 60000); // At least 1 minute

    tokenRefreshTimer.value = window.setTimeout(async () => {
      try {
        await refreshTokens();
        // Set up next refresh timer
        setupTokenRefreshTimer();
      } catch (error) {
        console.error('Automatic token refresh failed:', error);
      }
    }, refreshTime);
  }

  // Actions
  async function login(credentials: LoginCredentials): Promise<void> {
    isLoading.value = true;
    try {
      const { user: userData, tokens } = await authApi.login(credentials);
      
      // Store tokens
      accessToken.value = tokens.access;
      refreshToken.value = tokens.refresh;
      localStorage.setItem('access_token', tokens.access);
      localStorage.setItem('refresh_token', tokens.refresh);
      
      // Store user data
      user.value = userData;
      
      // Set up automatic token refresh
      setupTokenRefreshTimer();
      // Set up activity monitoring
      setupActivityMonitoring();
    } catch (error) {
      console.error('Login failed:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function register(data: RegisterData): Promise<void> {
    isLoading.value = true;
    try {
      const { user: userData, tokens } = await authApi.register(data);
      
      // Store tokens
      accessToken.value = tokens.access;
      refreshToken.value = tokens.refresh;
      localStorage.setItem('access_token', tokens.access);
      localStorage.setItem('refresh_token', tokens.refresh);
      
      // Store user data
      user.value = userData;
      
      // Set up automatic token refresh
      setupTokenRefreshTimer();
      // Set up activity monitoring
      setupActivityMonitoring();
    } catch (error) {
      console.error('Registration failed:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function refreshTokens(): Promise<boolean> {
    if (!refreshToken.value) return false;

    try {
      const { access } = await authApi.refreshToken(refreshToken.value);
      
      accessToken.value = access;
      localStorage.setItem('access_token', access);
      
      // Set up automatic token refresh for new token
      setupTokenRefreshTimer();
      // Set up activity monitoring
      setupActivityMonitoring();
      
      return true;
    } catch (error) {
      console.error('Token refresh failed:', error);
      logout();
      return false;
    }
  }

  async function logout(): Promise<void> {
    try {
      if (refreshToken.value) {
        await authApi.logout(refreshToken.value);
      }
    } catch (error) {
      console.error('Logout API call failed:', error);
    } finally {
      // Clear state regardless of API call success
      clearAuthData();
    }
  }

  function clearAuthData(): void {
    user.value = null;
    accessToken.value = null;
    refreshToken.value = null;
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    
    // Clear token refresh timer
    if (tokenRefreshTimer.value) {
      clearTimeout(tokenRefreshTimer.value);
      tokenRefreshTimer.value = null;
    }
    
    // Clear inactivity timer
    if (inactivityTimer.value) {
      clearTimeout(inactivityTimer.value);
      inactivityTimer.value = null;
    }
    
    // Note: Event listeners will be cleaned up when the page is unloaded
    // or when new ones are added on next authentication
  }

  async function fetchProfile(): Promise<void> {
    if (!accessToken.value) return;

    try {
      const userData = await authApi.getProfile();
      user.value = userData;
    } catch (error) {
      console.error('Failed to fetch profile:', error);
      throw error;
    }
  }

  async function updateProfile(data: Partial<User>): Promise<void> {
    try {
      const updatedUser = await authApi.updateProfile(data);
      user.value = updatedUser;
    } catch (error) {
      console.error('Failed to update profile:', error);
      throw error;
    }
  }

  async function changePassword(oldPassword: string, newPassword: string): Promise<void> {
    try {
      await authApi.changePassword({ oldPassword, newPassword });
    } catch (error) {
      console.error('Failed to change password:', error);
      throw error;
    }
  }

  async function uploadAvatar(file: File, onProgress?: (progress: number) => void): Promise<void> {
    try {
      const updatedUser = await authApi.uploadAvatar(file, onProgress);
      user.value = updatedUser;
    } catch (error) {
      console.error('Failed to upload avatar:', error);
      throw error;
    }
  }

  async function deleteAvatar(): Promise<void> {
    try {
      const updatedUser = await authApi.deleteAvatar();
      user.value = updatedUser;
    } catch (error) {
      console.error('Failed to delete avatar:', error);
      throw error;
    }
  }

  // Initialize auth state on store creation
  async function initializeAuth(): Promise<void> {
    if (isInitialized.value) return;
    
    try {
      // Check if we have tokens
      if (accessToken.value && refreshToken.value) {
        // Check if access token is expired
        if (isTokenExpired(accessToken.value)) {
          // Try to refresh the token
          const refreshed = await refreshTokens();
          if (!refreshed) {
            // If refresh failed, clear auth data
            clearAuthData();
            isInitialized.value = true;
            return;
          }
        }
        
        // Fetch user profile to verify token is still valid
        try {
          await fetchProfile();
          // Set up automatic token refresh
          setupTokenRefreshTimer();
          // Set up activity monitoring
          setupActivityMonitoring();
        } catch (error) {
          console.error('Failed to fetch profile during initialization:', error);
          // If profile fetch fails, try to refresh token one more time
          const refreshed = await refreshTokens();
          if (refreshed) {
            await fetchProfile();
            // Set up automatic token refresh
            setupTokenRefreshTimer();
            // Set up activity monitoring
            setupActivityMonitoring();
          } else {
            clearAuthData();
          }
        }
      } else {
        // No tokens found, clear any stale data
        clearAuthData();
      }
    } catch (error) {
      console.error('Auth initialization failed:', error);
      clearAuthData();
    } finally {
      isInitialized.value = true;
    }
  }

  // Helper function to set up activity monitoring
  function setupActivityMonitoring(): void {
    // Clear existing inactivity timer
    if (inactivityTimer.value) {
      clearTimeout(inactivityTimer.value);
    }

    // Set up inactivity timer (24 hours)
    const INACTIVITY_TIMEOUT = 24 * 60 * 60 * 1000; // 24 hours in milliseconds
    
    inactivityTimer.value = window.setTimeout(() => {
      console.log('User inactive for 24 hours, logging out');
      logout();
    }, INACTIVITY_TIMEOUT);

    // Reset token refresh timer and inactivity timer on user activity
    const resetTimers = () => {
      lastActivityTime.value = Date.now();
      
      if (accessToken.value && !isTokenExpired(accessToken.value)) {
        setupTokenRefreshTimer();
      }
      
      // Reset inactivity timer
      if (inactivityTimer.value) {
        clearTimeout(inactivityTimer.value);
      }
      inactivityTimer.value = window.setTimeout(() => {
        console.log('User inactive for 24 hours, logging out');
        logout();
      }, INACTIVITY_TIMEOUT);
    };

    // Listen for user activity events
    const events = ['mousedown', 'mousemove', 'keypress', 'scroll', 'touchstart', 'click'];
    events.forEach(event => {
      document.addEventListener(event, resetTimers, { passive: true });
    });

    // Handle page visibility changes
    const handleVisibilityChange = () => {
      if (document.hidden) {
        // Page is hidden, pause inactivity timer
        if (inactivityTimer.value) {
          clearTimeout(inactivityTimer.value);
          inactivityTimer.value = null;
        }
      } else {
        // Page is visible again, reset timers
        resetTimers();
      }
    };

    // Handle window focus/blur
    const handleWindowFocus = () => {
      resetTimers();
    };

    const handleWindowBlur = () => {
      // Window lost focus, but don't clear timer immediately
      // Timer will continue running unless page becomes hidden
    };

    document.addEventListener('visibilitychange', handleVisibilityChange);
    window.addEventListener('focus', handleWindowFocus);
    window.addEventListener('blur', handleWindowBlur);
  }

  return {
    // State
    user,
    accessToken,
    refreshToken,
    isLoading,
    isInitialized,
    
    // Getters
    isAuthenticated,
    token,
    userEmail,
    userName,
    
    // Actions
    login,
    register,
    logout,
    refreshTokens,
    fetchProfile,
    updateProfile,
    changePassword,
    uploadAvatar,
    deleteAvatar,
    initializeAuth,
    clearAuthData,
  };
});