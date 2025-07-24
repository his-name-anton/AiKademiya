import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from 'axios';
import { useAuthStore } from '@/stores/auth';

// API client configuration
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000/api';

class ApiClient {
  private client: AxiosInstance;

  constructor() {
    this.client = axios.create({
      baseURL: API_BASE_URL,
      timeout: 30000,
      headers: {
        'Content-Type': 'application/json',
      },
    });

    this.setupInterceptors();
  }

  private setupInterceptors() {
    // Request interceptor to add auth token
    this.client.interceptors.request.use(
      (config) => {
        // Get auth store inside interceptor to ensure reactivity
        const authStore = useAuthStore();
        const token = authStore.token;
        
        if (token) {
          config.headers.Authorization = `Bearer ${token}`;
        }

        // Add CSRF token for non-GET requests
        if (config.method !== 'get') {
          const csrfToken = this.getCSRFToken();
          if (csrfToken) {
            config.headers['X-CSRFToken'] = csrfToken;
          }
        }

        return config;
      },
      (error) => {
        return Promise.reject(error);
      }
    );

    // Response interceptor to handle auth errors
    this.client.interceptors.response.use(
      (response) => {
        return response;
      },
      async (error) => {
        const authStore = useAuthStore();
        
        // Only handle 401 errors for authenticated requests
        if (error.response?.status === 401 && error.config?.headers?.Authorization) {
          console.log('401 error with Authorization header, attempting token refresh...');
          
          // Prevent infinite retry loops
          if (error.config._retry) {
            console.log('Request already retried, not attempting again');
            await authStore.logout();
            const currentPath = window.location.pathname;
            if (currentPath !== '/login' && currentPath !== '/') {
              console.log('Redirecting to login page after retry failure...');
              window.location.href = '/login';
            }
            return Promise.reject(error);
          }
          
          // Mark request as retried
          error.config._retry = true;
          
          // Try to refresh token
          const refreshed = await authStore.refreshTokens();
          if (refreshed && error.config) {
            console.log('Token refreshed, retrying original request...');
            // Update Authorization header with new token
            error.config.headers.Authorization = `Bearer ${authStore.token}`;
            // Retry original request with new token
            return this.client.request(error.config);
          } else {
            console.log('Token refresh failed, logging out user...');
            // Logout user if refresh failed
            await authStore.logout();
            // Only redirect if we're not already on login page and not on home page
            const currentPath = window.location.pathname;
            if (currentPath !== '/login' && currentPath !== '/') {
              console.log('Redirecting to login page...');
              window.location.href = '/login';
            }
          }
        } else if (error.response?.status === 401) {
          // 401 without Authorization header - user is not authenticated
          // Don't redirect, just let the error propagate
          console.log('401 error without Authorization header - user not authenticated');
        } else if (!error.response) {
          // Network error - don't logout user for network issues
          console.error('Network error:', error.message);
        }

        return Promise.reject(error);
      }
    );
  }

  private getCSRFToken(): string | null {
    return document.cookie
      .split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1] || null;
  }

  // HTTP methods
  async get<T = any>(url: string, config?: AxiosRequestConfig): Promise<AxiosResponse<T>> {
    return this.client.get(url, config);
  }

  async post<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<AxiosResponse<T>> {
    return this.client.post(url, data, config);
  }

  async put<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<AxiosResponse<T>> {
    return this.client.put(url, data, config);
  }

  async patch<T = any>(url: string, data?: any, config?: AxiosRequestConfig): Promise<AxiosResponse<T>> {
    return this.client.patch(url, data, config);
  }

  async delete<T = any>(url: string, config?: AxiosRequestConfig): Promise<AxiosResponse<T>> {
    return this.client.delete(url, config);
  }

  // Upload file with progress
  async upload<T = any>(
    url: string, 
    formData: FormData, 
    onProgress?: (progress: number) => void
  ): Promise<AxiosResponse<T>> {
    return this.client.post(url, formData, {
      headers: {
        'Content-Type': 'multipart/form-data',
      },
      onUploadProgress: (progressEvent) => {
        if (onProgress && progressEvent.total) {
          const progress = Math.round((progressEvent.loaded * 100) / progressEvent.total);
          onProgress(progress);
        }
      },
    });
  }
}

// Export singleton instance
export const apiClient = new ApiClient();
export default apiClient;