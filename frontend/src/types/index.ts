// User and Authentication
export interface User {
  id: number;
  email: string;
  firstName?: string;
  lastName?: string;
  avatar?: string;
  isActive: boolean;
  dateJoined: string;
}

export interface AuthTokens {
  access: string;
  refresh: string;
}

export interface LoginCredentials {
  email: string;
  password: string;
}

export interface RegisterData {
  email: string;
  password: string;
  firstName?: string;
  lastName?: string;
}

// Course related types
export interface Course {
  id: number;
  title: string;
  description: string;
  difficulty: CourseDifficulty;
  style: CourseStyle;
  status: CourseStatus;
  createdAt: string;
  updatedAt: string;
  author: User;
  modules: CourseModule[];
}

export interface CourseModule {
  id: number;
  title: string;
  description: string;
  order: number;
  lessons: Lesson[];
}

export interface Lesson {
  id: number;
  title: string;
  content: string;
  order: number;
  type: LessonType;
  duration?: number;
}

export type CourseDifficulty = 'beginner' | 'intermediate' | 'advanced';
export type CourseStyle = 'default' | 'academic' | 'rebel';
export type CourseStatus = 'draft' | 'generating' | 'completed' | 'failed';
export type LessonType = 'text' | 'video' | 'quiz' | 'exercise';

// Course generation
export interface CourseGenerationRequest {
  topic: string;
  difficulty: CourseDifficulty;
  style: CourseStyle;
}

export interface CourseGenerationResponse {
  workflowId: string;
  message: string;
}

// API Response types
export interface ApiResponse<T = any> {
  success: boolean;
  data?: T;
  error?: string;
  message?: string;
}

export interface PaginatedResponse<T> {
  count: number;
  next?: string;
  previous?: string;
  results: T[];
}

// Form validation
export interface ValidationError {
  field: string;
  message: string;
}

// Navigation
export interface NavigationItem {
  name: string;
  href: string;
  icon?: string;
  current?: boolean;
  children?: NavigationItem[];
}

// Theme
export type Theme = 'light' | 'dark' | 'system';

// Toast notifications
export interface ToastOptions {
  title: string;
  description?: string;
  type: 'success' | 'error' | 'warning' | 'info';
  duration?: number;
}