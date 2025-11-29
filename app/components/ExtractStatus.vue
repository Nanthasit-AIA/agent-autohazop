<template>
  <div class="flex items-center gap-3 mb-6 mt-12">
    <div :class="['w-4 h-4 rounded-full', active ? 'bg-green-500' : 'bg-gray-300']"></div>
    <span class="text-gray-600">{{ label }}</span>
  </div>
</template>

<script setup lang="ts">
import { toRefs, withDefaults } from 'vue'

const props = withDefaults(
  defineProps<{
    active?: boolean
    label?: string
  }>(),
  {
    active: false,
    label: 'extract complete'
  }
)

const { active, label } = toRefs(props)
</script>
