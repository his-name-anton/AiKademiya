import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { authApi } from '@/api/auth';
import type { User, LoginCredentials, RegisterData } from '@/types';

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
    if (!refreshToken.value) {
      console.log('No refresh token available for refresh');
      return false;
    }

    try {
      console.log('Attempting to refresh token...');
      const { access } = await authApi.refreshToken(refreshToken.value);
      
      // Update tokens
      accessToken.value = access;
      localStorage.setItem('access_token', access);
      
      console.log('Token refreshed successfully');
      
      // Set up automatic token refresh for new token
      setupTokenRefreshTimer();
      
      return true;
    } catch (error) {
      console.error('Token refresh failed:', error);
      // Don't call logout() here to avoid infinite loops
      // Just clear the data and don't set up activity monitoring
      clearAuthData();
      return false;
    }
  }

  async function logout(): Promise<void> {
    try {
      // Only call logout API if we have a refresh token
      if (refreshToken.value) {
        console.log('Calling logout API...');
        await authApi.logout(refreshToken.value);
      } else {
        console.log('No refresh token available, skipping logout API call');
      }
    } catch (error) {
      console.error('Logout API call failed:', error);
      // Continue with clearing local data even if API call fails
    } finally {
      // Clear state regardless of API call success
      console.log('Clearing auth data...');
      clearAuthData();
    }
  }

  // Store references to event listeners for proper cleanup
  const activityListeners = ref<{ [key: string]: () => void }>({});
  const visibilityListener = ref<(() => void) | null>(null);
  const focusListener = ref<(() => void) | null>(null);
  const blurListener = ref<(() => void) | null>(null);

  function clearAuthData(): void {
    console.log('Clearing all auth data...');
    
    // Clear state
    user.value = null;
    accessToken.value = null;
    refreshToken.value = null;
    
    // Clear localStorage
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    
    // Clear token refresh timer
    if (tokenRefreshTimer.value) {
      console.log('Clearing token refresh timer...');
      clearTimeout(tokenRefreshTimer.value);
      tokenRefreshTimer.value = null;
    }
    
    // Clear inactivity timer
    if (inactivityTimer.value) {
      console.log('Clearing inactivity timer...');
      clearTimeout(inactivityTimer.value);
      inactivityTimer.value = null;
    }
    
    // Remove activity event listeners
    Object.entries(activityListeners.value).forEach(([event, listener]) => {
      document.removeEventListener(event, listener, { passive: true } as any);
    });
    activityListeners.value = {};
    
    // Remove visibility and window event listeners
    if (visibilityListener.value) {
      document.removeEventListener('visibilitychange', visibilityListener.value);
      visibilityListener.value = null;
    }
    if (focusListener.value) {
      window.removeEventListener('focus', focusListener.value);
      focusListener.value = null;
    }
    if (blurListener.value) {
      window.removeEventListener('blur', blurListener.value);
      blurListener.value = null;
    }
    
    console.log('Auth data cleared successfully');
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
    if (isInitialized.value) {
      console.log('Auth already initialized, skipping...');
      return;
    }
    
    console.log('Starting auth initialization...');
    
    try {
      // Read tokens from localStorage
      const storedAccessToken = localStorage.getItem('access_token');
      const storedRefreshToken = localStorage.getItem('refresh_token');
      
      console.log('Stored tokens:', {
        hasAccessToken: !!storedAccessToken,
        hasRefreshToken: !!storedRefreshToken
      });
      
      // Update reactive values
      accessToken.value = storedAccessToken;
      refreshToken.value = storedRefreshToken;
      
      // Check if we have tokens
      if (accessToken.value && refreshToken.value) {
        console.log('Tokens found, checking validity...');
        
        // Check if access token is expired
        if (isTokenExpired(accessToken.value)) {
          console.log('Access token expired, attempting refresh...');
          // Try to refresh the token
          const refreshed = await refreshTokens();
          if (!refreshed) {
            console.log('Token refresh failed during initialization, clearing auth data');
            clearAuthData();
            isInitialized.value = true;
            return;
          }
          console.log('Token refreshed successfully during initialization');
        }
        
        // Fetch user profile to verify token is still valid
        try {
          console.log('Fetching user profile to verify token...');
          await fetchProfile();
          console.log('Profile fetched successfully, user is authenticated');
          
          // Set up automatic token refresh
          setupTokenRefreshTimer();
          // Set up activity monitoring
          setupActivityMonitoring();
          
          console.log('Auth initialization completed successfully');
        } catch (error) {
          console.error('Failed to fetch profile during initialization:', error);
          
          // If profile fetch fails, try to refresh token one more time
          console.log('Attempting one more token refresh...');
          const refreshed = await refreshTokens();
          if (refreshed) {
            try {
              console.log('Retrying profile fetch after token refresh...');
              await fetchProfile();
              console.log('Profile fetched successfully after token refresh');
              
              // Set up automatic token refresh
              setupTokenRefreshTimer();
              // Set up activity monitoring
              setupActivityMonitoring();
              
              console.log('Auth initialization completed after retry');
            } catch (profileError) {
              console.error('Failed to fetch profile after token refresh:', profileError);
              console.log('Clearing auth data due to persistent profile fetch failure');
              clearAuthData();
            }
          } else {
            console.log('Token refresh failed after profile fetch error, clearing auth data');
            clearAuthData();
          }
        }
      } else {
        console.log('No tokens found in localStorage, user not authenticated');
        clearAuthData();
      }
    } catch (error) {
      console.error('Auth initialization failed with error:', error);
      clearAuthData();
    } finally {
      isInitialized.value = true;
      console.log('Auth initialization process completed, isInitialized =', isInitialized.value);
    }
  }

  // Helper function to set up activity monitoring
  function setupActivityMonitoring(): void {
    // Clear existing listeners first
    Object.entries(activityListeners.value).forEach(([event, listener]) => {
      document.removeEventListener(event, listener, { passive: true } as any);
    });
    activityListeners.value = {};
    
    if (visibilityListener.value) {
      document.removeEventListener('visibilitychange', visibilityListener.value);
    }
    if (focusListener.value) {
      window.removeEventListener('focus', focusListener.value);
    }
    if (blurListener.value) {
      window.removeEventListener('blur', blurListener.value);
    }

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
      activityListeners.value[event] = resetTimers;
      document.addEventListener(event, resetTimers, { passive: true });
    });

    // Handle page visibility changes
    visibilityListener.value = () => {
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
    focusListener.value = () => {
      resetTimers();
    };

    blurListener.value = () => {
      // Window lost focus, but don't clear timer immediately
      // Timer will continue running unless page becomes hidden
    };

    document.addEventListener('visibilitychange', visibilityListener.value);
    window.addEventListener('focus', focusListener.value);
    window.addEventListener('blur', blurListener.value);
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