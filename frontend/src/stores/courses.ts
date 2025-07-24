import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { coursesApi } from '@/api/courses';
import type { 
  Course, 
  CourseGenerationRequest, 
  CourseGenerationResponse,
  PaginatedResponse 
} from '@/types';

export const useCoursesStore = defineStore('courses', () => {
  // State
  const courses = ref<Course[]>([]);
  const currentCourse = ref<Course | null>(null);
  const enrolledCourses = ref<Course[]>([]);
  const publicCourses = ref<Course[]>([]);
  const isLoading = ref(false);
  const generationStatus = ref<{
    workflowId?: string;
    status?: string;
    progress?: number;
    error?: string;
  }>({});

  // Pagination state
  const pagination = ref({
    count: 0,
    next: null as string | null,
    previous: null as string | null,
    currentPage: 1,
    pageSize: 12,
  });

  // Getters
  const totalCourses = computed(() => courses.value.length);
  const completedCourses = computed(() => 
    courses.value.filter(course => course.status === 'completed')
  );
  const draftCourses = computed(() => 
    courses.value.filter(course => course.status === 'draft')
  );
  const generatingCourses = computed(() => 
    courses.value.filter(course => course.status === 'generating')
  );

  // Actions
  async function fetchCourses(params?: {
    page?: number;
    pageSize?: number;
    status?: string;
    search?: string;
  }): Promise<void> {
    isLoading.value = true;
    try {
      const response = await coursesApi.getCourses(params);
      courses.value = response.results;
      pagination.value = {
        count: response.count,
        next: response.next,
        previous: response.previous,
        currentPage: params?.page || 1,
        pageSize: params?.pageSize || 12,
      };
    } catch (error) {
      console.error('Failed to fetch courses:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function fetchCourse(id: number): Promise<Course> {
    isLoading.value = true;
    try {
      const course = await coursesApi.getCourse(id);
      currentCourse.value = course;
      
      // Update course in courses array if it exists
      const index = courses.value.findIndex(c => c.id === id);
      if (index !== -1) {
        courses.value[index] = course;
      }
      
      return course;
    } catch (error) {
      console.error('Failed to fetch course:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function generateCourse(data: CourseGenerationRequest): Promise<CourseGenerationResponse> {
    isLoading.value = true;
    try {
      const response = await coursesApi.generateCourse(data);
      generationStatus.value = {
        workflowId: response.workflowId,
        status: 'generating',
        progress: 0,
      };
      return response;
    } catch (error) {
      console.error('Failed to generate course:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function checkGenerationStatus(workflowId: string): Promise<void> {
    try {
      const status = await coursesApi.getGenerationStatus(workflowId);
      generationStatus.value = {
        workflowId,
        ...status,
      };

      // If generation is complete, refresh courses
      if (status.status === 'completed') {
        await fetchCourses();
      }
    } catch (error) {
      console.error('Failed to check generation status:', error);
      generationStatus.value.error = 'Failed to check status';
    }
  }

  async function updateCourse(id: number, data: Partial<Course>): Promise<Course> {
    try {
      const updatedCourse = await coursesApi.updateCourse(id, data);
      
      // Update course in state
      if (currentCourse.value?.id === id) {
        currentCourse.value = updatedCourse;
      }
      
      const index = courses.value.findIndex(c => c.id === id);
      if (index !== -1) {
        courses.value[index] = updatedCourse;
      }
      
      return updatedCourse;
    } catch (error) {
      console.error('Failed to update course:', error);
      throw error;
    }
  }

  async function deleteCourse(id: number): Promise<void> {
    try {
      await coursesApi.deleteCourse(id);
      
      // Remove from state
      courses.value = courses.value.filter(c => c.id !== id);
      if (currentCourse.value?.id === id) {
        currentCourse.value = null;
      }
    } catch (error) {
      console.error('Failed to delete course:', error);
      throw error;
    }
  }

  async function duplicateCourse(id: number): Promise<Course> {
    try {
      const duplicatedCourse = await coursesApi.duplicateCourse(id);
      courses.value.unshift(duplicatedCourse);
      return duplicatedCourse;
    } catch (error) {
      console.error('Failed to duplicate course:', error);
      throw error;
    }
  }

  async function publishCourse(id: number): Promise<Course> {
    try {
      const publishedCourse = await coursesApi.publishCourse(id);
      return await updateCourse(id, publishedCourse);
    } catch (error) {
      console.error('Failed to publish course:', error);
      throw error;
    }
  }

  async function unpublishCourse(id: number): Promise<Course> {
    try {
      const unpublishedCourse = await coursesApi.unpublishCourse(id);
      return await updateCourse(id, unpublishedCourse);
    } catch (error) {
      console.error('Failed to unpublish course:', error);
      throw error;
    }
  }

  async function fetchPublicCourses(params?: {
    page?: number;
    pageSize?: number;
    difficulty?: string;
    category?: string;
    search?: string;
  }): Promise<void> {
    isLoading.value = true;
    try {
      const response = await coursesApi.getPublicCourses(params);
      publicCourses.value = response.results;
      pagination.value = {
        count: response.count,
        next: response.next,
        previous: response.previous,
        currentPage: params?.page || 1,
        pageSize: params?.pageSize || 12,
      };
    } catch (error) {
      console.error('Failed to fetch public courses:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function fetchEnrolledCourses(params?: {
    page?: number;
    pageSize?: number;
  }): Promise<void> {
    isLoading.value = true;
    try {
      const response = await coursesApi.getEnrolledCourses(params);
      enrolledCourses.value = response.results;
    } catch (error) {
      console.error('Failed to fetch enrolled courses:', error);
      throw error;
    } finally {
      isLoading.value = false;
    }
  }

  async function enrollInCourse(courseId: number): Promise<void> {
    try {
      await coursesApi.enrollInCourse(courseId);
      await fetchEnrolledCourses();
    } catch (error) {
      console.error('Failed to enroll in course:', error);
      throw error;
    }
  }

  async function unenrollFromCourse(courseId: number): Promise<void> {
    try {
      await coursesApi.unenrollFromCourse(courseId);
      enrolledCourses.value = enrolledCourses.value.filter(c => c.id !== courseId);
    } catch (error) {
      console.error('Failed to unenroll from course:', error);
      throw error;
    }
  }

  function clearGenerationStatus(): void {
    generationStatus.value = {};
  }

  function clearCurrentCourse(): void {
    currentCourse.value = null;
  }

  function resetStore(): void {
    courses.value = [];
    currentCourse.value = null;
    enrolledCourses.value = [];
    publicCourses.value = [];
    generationStatus.value = {};
    pagination.value = {
      count: 0,
      next: null,
      previous: null,
      currentPage: 1,
      pageSize: 12,
    };
  }

  return {
    // State
    courses,
    currentCourse,
    enrolledCourses,
    publicCourses,
    isLoading,
    generationStatus,
    pagination,

    // Getters
    totalCourses,
    completedCourses,
    draftCourses,
    generatingCourses,

    // Actions
    fetchCourses,
    fetchCourse,
    generateCourse,
    checkGenerationStatus,
    updateCourse,
    deleteCourse,
    duplicateCourse,
    publishCourse,
    unpublishCourse,
    fetchPublicCourses,
    fetchEnrolledCourses,
    enrollInCourse,
    unenrollFromCourse,
    clearGenerationStatus,
    clearCurrentCourse,
    resetStore,
  };
});