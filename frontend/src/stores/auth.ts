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
  }

  async function fetchProfile(): Promise<void> {
    if (!isAuthenticated.value) return;

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
    if (accessToken.value) {
      try {
        await fetchProfile();
      } catch (error) {
        // If fetching profile fails, clear auth data
        clearAuthData();
      }
    }
  }

  return {
    // State
    user,
    accessToken,
    refreshToken,
    isLoading,
    
    // Getters
    isAuthenticated,
    token,
    userEmail,
    userName,
    
    // Actions
    login,
    register,
    logout,
    refreshToken: refreshTokens,
    fetchProfile,
    updateProfile,
    changePassword,
    uploadAvatar,
    deleteAvatar,
    initializeAuth,
    clearAuthData,
  };
});