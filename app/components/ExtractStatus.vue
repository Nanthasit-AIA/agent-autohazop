<script setup lang="ts">
import { toRefs, watch } from 'vue'

const props = defineProps<{
  label: string;   // 👈 assume this is the text like "Extracting..." / "Complete"
  active: boolean;
}>()

const { label } = toRefs(props)

const emit = defineEmits<{
  (e: 'completed'): void
}>()

// 🔍 watch label, fire when it becomes "Complete"
watch(label, (newVal) => {
  if (newVal === 'Complete') {
    emit('completed')
  }
})
</script>

<template>
  <div class="flex items-center gap-3 mb-6 mt-12">
    <div :class="['w-4 h-4 rounded-full', active ? 'bg-green-500' : 'bg-gray-300']"></div>
    <span class="text-gray-600">{{ label }}</span>
  </div>
</template>


