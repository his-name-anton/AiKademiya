import apiClient from './client';
import type { 
  User, 
  AuthTokens, 
  LoginCredentials, 
  RegisterData, 
  ApiResponse 
} from '@/types';

export const authApi = {
  // Login user
  async login(credentials: LoginCredentials): Promise<{ user: User; tokens: AuthTokens }> {
    const response = await apiClient.post<ApiResponse<{ user: User; tokens: AuthTokens }>>('/v1/auth/login/', credentials);
    return response.data.data!;
  },

  // Register user
  async register(data: RegisterData): Promise<{ user: User; tokens: AuthTokens }> {
    const response = await apiClient.post<ApiResponse<{ user: User; tokens: AuthTokens }>>('/v1/auth/register/', data);
    return response.data.data!;
  },

  // Refresh token
  async refreshToken(refreshToken: string): Promise<{ access: string }> {
    const response = await apiClient.post<ApiResponse<{ access: string }>>('/v1/auth/token/refresh/', {
      refresh: refreshToken,
    });
    return response.data.data!;
  },

  // Logout user
  async logout(refreshToken: string): Promise<void> {
    await apiClient.post('/v1/auth/logout/', {
      refresh: refreshToken,
    });
  },

  // Get current user profile
  async getProfile(): Promise<User> {
    const response = await apiClient.get<ApiResponse<User>>('/v1/auth/profile/');
    return response.data.data!;
  },

  // Update user profile
  async updateProfile(data: Partial<User>): Promise<User> {
    const response = await apiClient.patch<ApiResponse<User>>('/v1/auth/profile/', data);
    return response.data.data!;
  },

  // Change password
  async changePassword(data: {
    oldPassword: string;
    newPassword: string;
  }): Promise<void> {
    await apiClient.post('/v1/auth/change-password/', {
      old_password: data.oldPassword,
      new_password: data.newPassword,
    });
  },

  // Request password reset
  async requestPasswordReset(email: string): Promise<void> {
    await apiClient.post('/v1/auth/password-reset/', { email });
  },

  // Confirm password reset
  async confirmPasswordReset(data: {
    token: string;
    newPassword: string;
  }): Promise<void> {
    await apiClient.post('/v1/auth/password-reset-confirm/', {
      token: data.token,
      new_password: data.newPassword,
    });
  },

  // Upload avatar
  async uploadAvatar(file: File, onProgress?: (progress: number) => void): Promise<User> {
    const formData = new FormData();
    formData.append('avatar', file);
    
    const response = await apiClient.upload<ApiResponse<User>>('/v1/auth/avatar/', formData, onProgress);
    return response.data.data!;
  },

  // Delete avatar
  async deleteAvatar(): Promise<User> {
    const response = await apiClient.delete<ApiResponse<User>>('/v1/auth/avatar/');
    return response.data.data!;
  },
};