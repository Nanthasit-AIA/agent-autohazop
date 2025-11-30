<script setup lang="ts">
const emit = defineEmits<{
  (e: 'call-hazop'): void
}>()
</script>

<template>
  <div class="flex gap-3 justify-center mb-8">
    <button
      @click="emit('call-hazop')"
      class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition"
    >
      Call to HAZOP analysis
    </button>
    <button
      class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition"
    >
      exit
    </button>
  </div>
</template>
