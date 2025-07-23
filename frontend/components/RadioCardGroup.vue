<template>
  <RadioGroup v-model="model">
    <div class="space-y-2">
      <RadioGroupOption
        as="template"
        v-for="o in options"
        :key="o.value"
        :value="o.value"
        v-slot="{ active, checked }"
      >
        <div
          :class="[
            'flex cursor-pointer rounded-lg px-5 py-4 shadow-md',
            checked ? 'bg-sky-900 text-white' : 'bg-white text-gray-900',
            active ? 'ring-2 ring-offset-2 ring-sky-300' : '',
          ]"
        >
          <div class="w-full">
            <RadioGroupLabel as="p" class="font-medium">
              {{ o.title }}
            </RadioGroupLabel>
            <RadioGroupDescription class="text-sm">
              {{ o.description }}
            </RadioGroupDescription>
          </div>
          <div v-show="checked" class="ml-auto text-white">
            <svg class="h-5 w-5" viewBox="0 0 24 24" fill="none">
              <path d="M7 13l3 3 7-7" stroke="white" stroke-width="2" />
            </svg>
          </div>
        </div>
      </RadioGroupOption>
    </div>
  </RadioGroup>
</template>

<script setup>
import { ref, watch } from 'vue'
import {
  RadioGroup,
  RadioGroupLabel,
  RadioGroupDescription,
  RadioGroupOption,
} from '@headlessui/vue'

const props = defineProps({
  modelValue: String,
  options: { type: Array, default: () => [] }
})
const emit = defineEmits(['update:modelValue'])

const model = ref(props.modelValue)
watch(() => props.modelValue, v => model.value = v)
watch(model, v => emit('update:modelValue', v))
</script>
