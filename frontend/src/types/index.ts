// User and Authentication
export interface User {
  id: number;
  email: string;
  username?: string;
  firstName?: string;
  lastName?: string;
  first_name?: string;
  last_name?: string;
  avatar?: string;
  isActive: boolean;
  dateJoined: string;
  date_joined?: string;
  // Extended profile fields
  country?: string;
  city?: string;
  address?: string;
  phone?: string;
  birth_date?: string;
  birthDate?: string;
  organization?: string;
  role?: string;
  department?: string;
  zip_code?: string;
  zipCode?: string;
  occupation?: string;
  // Preferences
  language?: string;
  timezone?: string;
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
  username: string;
  password: string;
  password_confirm: string;
  firstName?: string;
  lastName?: string;
}

// Password change
export interface PasswordChangeData {
  oldPassword: string;
  newPassword: string;
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
  // For learning page
  image?: string;
  lessons_count?: number;
  completed_lessons?: number;
  estimated_duration?: number;
  lessons?: Lesson[];
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
  completed?: boolean;
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
  errors?: Record<string, string[]>;
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

// Settings
export interface NotificationSettings {
  key: string;
  title: string;
  description: string;
  enabled: boolean;
}

export interface EmailSettings {
  key: string;
  title: string;
  description: string;
  enabled: boolean;
}

export interface LanguageSettings {
  language: string;
  timezone: string;
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