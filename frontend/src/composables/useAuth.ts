import { computed } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import { useToast } from 'vue-toastification';
import type { LoginCredentials, RegisterData } from '@/types';

export function useAuth() {
  const authStore = useAuthStore();
  const router = useRouter();
  const toast = useToast();

  // Computed properties
  const isAuthenticated = computed(() => authStore.isAuthenticated);
  const user = computed(() => authStore.user);
  const isLoading = computed(() => authStore.isLoading);
  const userName = computed(() => authStore.userName);
  const userEmail = computed(() => authStore.userEmail);

  // Login function
  async function login(credentials: LoginCredentials, redirectTo?: string) {
    try {
      await authStore.login(credentials);
      toast.success('Добро пожаловать!');
      
      // Redirect after successful login
      const redirect = redirectTo || '/dashboard';
      await router.push(redirect);
    } catch (error: any) {
      const message = error.response?.data?.message || 'Ошибка входа';
      toast.error(message);
      throw error;
    }
  }

  // Register function
  async function register(data: RegisterData, redirectTo?: string) {
    try {
      await authStore.register(data);
      toast.success('Регистрация успешна! Добро пожаловать!');
      
      // Redirect after successful registration
      const redirect = redirectTo || '/dashboard';
      await router.push(redirect);
    } catch (error: any) {
      const message = error.response?.data?.message || 'Ошибка регистрации';
      toast.error(message);
      throw error;
    }
  }

  // Logout function
  async function logout() {
    try {
      await authStore.logout();
      toast.info('Вы вышли из системы');
      await router.push('/');
    } catch (error: any) {
      console.error('Logout error:', error);
      // Clear auth data even if API call fails
      authStore.clearAuthData();
      await router.push('/');
    }
  }

  // Update profile function
  async function updateProfile(data: Partial<typeof authStore.user>) {
    try {
      await authStore.updateProfile(data);
      toast.success('Профиль обновлен');
    } catch (error: any) {
      const message = error.response?.data?.message || 'Ошибка обновления профиля';
      toast.error(message);
      throw error;
    }
  }

  // Change password function
  async function changePassword(oldPassword: string, newPassword: string) {
    try {
      await authStore.changePassword(oldPassword, newPassword);
      toast.success('Пароль изменен');
    } catch (error: any) {
      const message = error.response?.data?.message || 'Ошибка изменения пароля';
      toast.error(message);
      throw error;
    }
  }

  // Upload avatar function
  async function uploadAvatar(file: File, onProgress?: (progress: number) => void) {
    try {
      await authStore.uploadAvatar(file, onProgress);
      toast.success('Аватар обновлен');
    } catch (error: any) {
      const message = error.response?.data?.message || 'Ошибка загрузки аватара';
      toast.error(message);
      throw error;
    }
  }

  // Delete avatar function
  async function deleteAvatar() {
    try {
      await authStore.deleteAvatar();
      toast.success('Аватар удален');
    } catch (error: any) {
      const message = error.response?.data?.message || 'Ошибка удаления аватара';
      toast.error(message);
      throw error;
    }
  }

  // Check if user has permission
  function hasPermission(permission: string): boolean {
    // Implement permission checking logic based on your requirements
    if (!user.value) return false;
    
    // For now, just check if user is active
    return user.value.isActive;
  }

  // Require authentication
  function requireAuth() {
    if (!isAuthenticated.value) {
      router.push('/login');
      return false;
    }
    return true;
  }

  // Initialize auth state
  async function initializeAuth() {
    try {
      await authStore.initializeAuth();
    } catch (error) {
      console.error('Failed to initialize auth:', error);
    }
  }

  return {
    // State
    isAuthenticated,
    user,
    isLoading,
    userName,
    userEmail,

    // Actions
    login,
    register,
    logout,
    updateProfile,
    changePassword,
    uploadAvatar,
    deleteAvatar,
    hasPermission,
    requireAuth,
    initializeAuth,
  };
}