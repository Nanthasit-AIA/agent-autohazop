<script setup lang="ts">
import { computed, toRefs } from 'vue'

const props = defineProps<{
  data: any
  isLoading?: boolean
  fileName?: string
}>()

const { data, isLoading, fileName } = toRefs(props)

const hasData = computed(
  () => data.value !== null && data.value !== undefined
)

const formattedJson = computed(() =>
  hasData.value ? JSON.stringify(data.value, null, 2) : ''
)
</script>

<template>
  <div class="bg-gray-900 text-gray-100 rounded-2xl p-4">
    <div class="flex items-center justify-between mb-3">
      <h2 class="text-sm font-semibold">JSON Result</h2>
      <span v-if="fileName" class="text-xs text-gray-400">
        {{ fileName }}
      </span>
    </div>

    <!-- Loading -->
    <div v-if="isLoading" class="flex flex-col items-center justify-center h-40">
      <div class="w-10 h-10 border-4 border-gray-600 border-t-transparent rounded-full animate-spin"></div>
      <p class="text-sm text-gray-300 mt-3">Loading JSON…</p>
    </div>

    <!-- Empty -->
    <div v-else-if="!hasData" class="flex items-center justify-center h-40 text-gray-500 text-sm">
      No data. Search a file to view JSON.
    </div>

    <!-- Data -->
    <transition name="fade">
      <pre v-if="hasData && !isLoading"
        class="text-xs whitespace-pre-wrap wrap-break-words overflow-auto max-h-[420px] border border-gray-700 rounded-xl p-4 bg-black/60">{{ formattedJson }}</pre>
    </transition>
  </div>



</template>
<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>