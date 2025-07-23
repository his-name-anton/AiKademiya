<template>
  <section class="bg-gray-50 dark:bg-gray-900 min-h-screen flex items-center justify-center px-6 py-8">
    <div class="w-full md:w-1/2 max-w-md bg-white rounded-lg shadow p-6 md:p-8 dark:bg-gray-800 dark:border dark:border-gray-700">
      <GenerateCourseForm @submit="onSubmit" :apiError="error" />
    </div>
  </section>
</template>
<script setup>
import { ref } from 'vue'
import GenerateCourseForm from './GenerateCourseForm.vue'

const error = ref('')

function getCSRFToken() {
  return document.cookie.split('; ').find(r => r.startsWith('csrftoken='))?.split('=')[1]
}

async function onSubmit(payload) {
  try {
    const resp = await fetch('/api/create_course/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': getCSRFToken()
      },
      body: JSON.stringify(payload)
    })
    if (!resp.ok) {
      throw new Error('Ошибка при создании курса')
    }
    const data = await resp.json()
    try {
      const statusResp = await fetch(`/api/status/${data.workflow_id}/`)
      if (statusResp.ok) {
        window.location.href = `/api/status/${data.workflow_id}/`
        return
      }
      const info = await statusResp.json().catch(() => ({}))
      if (statusResp.status === 504 || info.error === 'timeout') {
        error.value = 'Превышено время ожидания. Попробуйте позже.'
        return
      }
      throw new Error('Не удалось получить статус')
    } catch (e) {
      error.value = 'Ошибка при проверке статуса: ' + e.message
    }
  } catch (e) {
    error.value = 'Ошибка: ' + e.message
  }
}
</script>
