<script setup lang="ts">
const emit = defineEmits<{
  (e: 'cta-click'): void
  (e: 'search-click'): void
}>()

const handleCtaClick = () => emit('cta-click')
const handleSearchClick = () => emit('search-click')
</script>

<template>
  <div class="text-center justify-center mb-12">
    <h1 class="text-5xl font-bold text-gray-900 mb-3">
      Agent-Based
    </h1>
    <h1 class="text-5xl font-bold text-gray-900 mb-10">
      Automated HAZOP Analysis
    </h1>
    <p class="text-gray-500 text-lg">Go ahead and Ready when you are.</p>
    <div class="flex gap-3 justify-center mt-10">
      <button class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition" @click="handleCtaClick">
        Call to action
      </button>
      <button class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition" @click="handleSearchClick">
        search
      </button>
    </div>
  </div>
</template>