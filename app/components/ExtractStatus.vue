<script setup lang="ts">
import { computed } from 'vue'

const props = withDefaults(
  defineProps<{
    active?: boolean
    label?: string
    errorMessage?: string | null
  }>(),
  {
    active: false,
    label: 'Waiting for search…',
    errorMessage: null
  }
)

// dot color logic
const indicatorClass = computed(() => {
  if (props.errorMessage) return 'bg-red-500'
  if (props.active) return 'bg-blue-400 animate-pulse'
  if (props.label.toLowerCase().includes('complete')) return 'bg-green-400'
  return 'bg-gray-300'
})

const showSpinner = computed(() => props.active)
</script>

<template>
  <div class="rounded-2xl px-5 py-4 flex items-center gap-3 text-sm text-gray-700">
    <!-- status dot + optional spinner -->
    <div class="relative">
      <div class="w-4 h-4 rounded-full" :class="indicatorClass"></div>

      <!-- spinner overlay when loading -->
      <div
        v-if="showSpinner"
        class="absolute -top-1 -left-1 w-6 h-6 border-2 border-gray-300 border-t-black rounded-full animate-spin"
      ></div>
    </div>

    <div class="flex flex-col">
      <span>{{ label }}</span>
      <span
        v-if="errorMessage"
        class="text-xs text-red-500 mt-0.5"
      >
        {{ errorMessage }}
      </span>
    </div>
  </div>
</template>
