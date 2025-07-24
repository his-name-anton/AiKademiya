import * as yup from 'yup';

// Common validation rules
export const validationRules = {
  email: yup.string()
    .email('Введите корректный email адрес')
    .required('Email обязателен'),
  
  password: yup.string()
    .min(8, 'Пароль должен содержать минимум 8 символов')
    .matches(
      /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)/,
      'Пароль должен содержать минимум одну заглавную букву, одну строчную букву и одну цифру'
    )
    .required('Пароль обязателен'),
  
  confirmPassword: (passwordField: string = 'password') => 
    yup.string()
      .oneOf([yup.ref(passwordField)], 'Пароли должны совпадать')
      .required('Подтверждение пароля обязательно'),
  
  firstName: yup.string()
    .min(2, 'Имя должно содержать минимум 2 символа')
    .max(50, 'Имя не должно превышать 50 символов')
    .matches(/^[a-zA-Zа-яА-Я\s]+$/, 'Имя может содержать только буквы'),
  
  lastName: yup.string()
    .min(2, 'Фамилия должна содержать минимум 2 символа')
    .max(50, 'Фамилия не должна превышать 50 символов')
    .matches(/^[a-zA-Zа-яА-Я\s]+$/, 'Фамилия может содержать только буквы'),
  
  courseTopic: yup.string()
    .min(5, 'Тема курса должна содержать минимум 5 символов')
    .max(200, 'Тема курса не должна превышать 200 символов')
    .required('Тема курса обязательна'),
  
  courseDifficulty: yup.string()
    .oneOf(['beginner', 'intermediate', 'advanced'], 'Выберите уровень сложности')
    .required('Уровень сложности обязателен'),
  
  courseStyle: yup.string()
    .oneOf(['default', 'academic', 'rebel'], 'Выберите стиль курса')
    .required('Стиль курса обязателен'),
};

// Validation schemas
export const authSchemas = {
  login: yup.object({
    email: validationRules.email,
    password: yup.string().required('Пароль обязателен'),
  }),
  
  register: yup.object({
    email: validationRules.email,
    password: validationRules.password,
    confirmPassword: validationRules.confirmPassword(),
    firstName: validationRules.firstName.optional(),
    lastName: validationRules.lastName.optional(),
  }),
  
  forgotPassword: yup.object({
    email: validationRules.email,
  }),
  
  resetPassword: yup.object({
    newPassword: validationRules.password,
    confirmPassword: validationRules.confirmPassword('newPassword'),
  }),
  
  changePassword: yup.object({
    oldPassword: yup.string().required('Текущий пароль обязателен'),
    newPassword: validationRules.password,
    confirmPassword: validationRules.confirmPassword('newPassword'),
  }),
};

export const courseSchemas = {
  generate: yup.object({
    topic: validationRules.courseTopic,
    difficulty: validationRules.courseDifficulty,
    style: validationRules.courseStyle,
  }),
  
  update: yup.object({
    title: yup.string()
      .min(5, 'Название должно содержать минимум 5 символов')
      .max(200, 'Название не должно превышать 200 символов'),
    description: yup.string()
      .max(1000, 'Описание не должно превышать 1000 символов'),
  }),
};

export const profileSchemas = {
  update: yup.object({
    firstName: validationRules.firstName.optional(),
    lastName: validationRules.lastName.optional(),
    email: validationRules.email,
  }),
  
  avatar: yup.object({
    file: yup.mixed()
      .required('Выберите файл')
      .test('fileSize', 'Размер файла не должен превышать 2MB', (value: any) => {
        return value && value.size <= 2 * 1024 * 1024;
      })
      .test('fileType', 'Поддерживаются только JPG, PNG и GIF файлы', (value: any) => {
        return value && ['image/jpeg', 'image/png', 'image/gif'].includes(value.type);
      }),
  }),
};

// Helper function to format validation errors
export function formatValidationError(error: yup.ValidationError): Record<string, string> {
  const errors: Record<string, string> = {};
  
  if (error.inner) {
    error.inner.forEach((err) => {
      if (err.path) {
        errors[err.path] = err.message;
      }
    });
  } else if (error.path) {
    errors[error.path] = error.message;
  }
  
  return errors;
}

// Helper function to validate form data
export async function validateFormData<T>(
  schema: yup.Schema<T>, 
  data: any
): Promise<{ isValid: boolean; errors: Record<string, string>; data?: T }> {
  try {
    const validData = await schema.validate(data, { abortEarly: false });
    return { isValid: true, errors: {}, data: validData };
  } catch (error) {
    if (error instanceof yup.ValidationError) {
      return { isValid: false, errors: formatValidationError(error) };
    }
    throw error;
  }
}