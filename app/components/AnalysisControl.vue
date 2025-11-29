<script setup lang="ts">
import { toRefs, withDefaults } from 'vue'

// ✅ type-based props + withDefaults
const props = withDefaults(
  defineProps<{
    statusText?: string
  }>(),
  {
    statusText: 'waiting to analysis'
  }
)

// ✅ typed emit
const emit = defineEmits<{
  (e: 'start'): void
}>()

const { statusText } = toRefs(props)
</script>

<template>
  <div class="space-y-6 mb-12">
    <div class="flex items-center gap-3">
      <div class="w-10 h-10 bg-gray-400 rounded-full"></div>
      <span class="text-gray-600">{{ statusText }}</span>
    </div>

    <div class="flex justify-center">
      <button
        @click="emit('start')"
        class="px-8 py-3 bg-black text-white rounded-lg hover:bg-gray-800 transition text-lg font-medium"
      >
        Start analysis
      </button>
    </div>
  </div>
</template>


