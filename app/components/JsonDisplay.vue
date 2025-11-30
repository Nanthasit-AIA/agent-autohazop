<script setup lang="ts">
import { toRefs, withDefaults } from 'vue'

// ✅ type-based defineProps + withDefaults
const props = withDefaults(
  defineProps<{
    message?: string
  }>(),
  {
    message: 'showing result JSON extract file'
  }
)

const { message } = toRefs(props)
</script>

<template>
  <div class="flex items-center gap-3 mb-6 mt-12">
    <span class="text-gray-600">{{ message }}</span>
  </div>
</template>
