import apiClient from './client';
import type { 
  Course, 
  CourseGenerationRequest, 
  CourseGenerationResponse,
  ApiResponse,
  PaginatedResponse
} from '@/types';

export const coursesApi = {
  // Get user's courses
  async getCourses(params?: {
    page?: number;
    pageSize?: number;
    status?: string;
    search?: string;
  }): Promise<PaginatedResponse<Course>> {
    const response = await apiClient.get<PaginatedResponse<Course>>('/courses/', { params });
    return response.data;
  },

  // Get course by ID
  async getCourse(id: number): Promise<Course> {
    const response = await apiClient.get<ApiResponse<Course>>(`/courses/${id}/`);
    return response.data.data!;
  },

  // Create/Generate new course
  async generateCourse(data: CourseGenerationRequest): Promise<CourseGenerationResponse> {
    const response = await apiClient.post<CourseGenerationResponse>('/create_course/', data);
    return response.data;
  },

  // Get course generation status
  async getGenerationStatus(workflowId: string): Promise<{
    status: string;
    progress?: number;
    error?: string;
    courseId?: number;
  }> {
    const response = await apiClient.get(`/status/${workflowId}/`);
    return response.data;
  },

  // Update course
  async updateCourse(id: number, data: Partial<Course>): Promise<Course> {
    const response = await apiClient.patch<ApiResponse<Course>>(`/courses/${id}/`, data);
    return response.data.data!;
  },

  // Delete course
  async deleteCourse(id: number): Promise<void> {
    await apiClient.delete(`/courses/${id}/`);
  },

  // Duplicate course
  async duplicateCourse(id: number): Promise<Course> {
    const response = await apiClient.post<ApiResponse<Course>>(`/courses/${id}/duplicate/`);
    return response.data.data!;
  },

  // Publish course
  async publishCourse(id: number): Promise<Course> {
    const response = await apiClient.post<ApiResponse<Course>>(`/courses/${id}/publish/`);
    return response.data.data!;
  },

  // Unpublish course
  async unpublishCourse(id: number): Promise<Course> {
    const response = await apiClient.post<ApiResponse<Course>>(`/courses/${id}/unpublish/`);
    return response.data.data!;
  },

  // Get public courses catalog
  async getPublicCourses(params?: {
    page?: number;
    pageSize?: number;
    difficulty?: string;
    category?: string;
    search?: string;
  }): Promise<PaginatedResponse<Course>> {
    const response = await apiClient.get<PaginatedResponse<Course>>('/catalog/', { params });
    return response.data;
  },

  // Enroll in course
  async enrollInCourse(courseId: number): Promise<void> {
    await apiClient.post(`/courses/${courseId}/enroll/`);
  },

  // Unenroll from course
  async unenrollFromCourse(courseId: number): Promise<void> {
    await apiClient.post(`/courses/${courseId}/unenroll/`);
  },

  // Get enrolled courses
  async getEnrolledCourses(params?: {
    page?: number;
    pageSize?: number;
  }): Promise<PaginatedResponse<Course>> {
    const response = await apiClient.get<PaginatedResponse<Course>>('/enrolled/', { params });
    return response.data;
  },

  // Mark lesson as completed
  async completeLession(courseId: number, lessonId: number): Promise<void> {
    await apiClient.post(`/courses/${courseId}/lessons/${lessonId}/complete/`);
  },

  // Get course progress
  async getCourseProgress(courseId: number): Promise<{
    completedLessons: number;
    totalLessons: number;
    progressPercentage: number;
  }> {
    const response = await apiClient.get(`/courses/${courseId}/progress/`);
    return response.data;
  },
};