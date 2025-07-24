import axios, { type AxiosInstance, type AxiosRequestConfig, type AxiosResponse } from 'axios';
import { useAuthStore } from '../stores/auth';

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
        
        if (error.response?.status === 401) {
          // Try to refresh token
          const refreshed = await authStore.refreshToken();
          if (refreshed && error.config) {
            // Retry original request with new token
            return this.client.request(error.config);
          } else {
            // Logout user if refresh failed
            authStore.logout();
            window.location.href = '/login';
          }
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