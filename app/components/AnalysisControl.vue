<script setup lang="ts">
import { computed, toRefs, withDefaults } from 'vue'

interface HazopRun {
  line_id: string
  parameter: string
  guide_word: string
  tokens_used?: number
}

const props = withDefaults(
  defineProps<{
    active?: boolean
    label?: string
    errorMessage?: string
    runs?: HazopRun[]
    outputFolder?: string
    fileName?: string
  }>(),
  {
    active: false,
    label: 'waiting to analysis',
    runs: () => []
  }
)

const emit = defineEmits<{
  (e: 'start'): void
}>()

const { active, label, errorMessage, runs, outputFolder, fileName } = toRefs(props)

// dot color
const indicatorClass = computed(() => {
  if (errorMessage.value) return 'bg-red-500'
  if (active.value) return 'bg-blue-400 animate-pulse'
  if (label.value && label.value.toLowerCase().includes('complete')) {
    return 'bg-green-400'
  }
  return 'bg-gray-300'
})

// spinner on top of dot when running
const showSpinner = computed(() => active.value)

// any runs from backend
const hasRuns = computed(() => (runs.value?.length ?? 0) > 0)

// full saved path
const fullPath = computed(() => {
  if (!outputFolder.value && !fileName.value) return ''
  if (!outputFolder.value) return fileName.value
  if (!fileName.value) return outputFolder.value
  return `${outputFolder.value}/${fileName.value}`
})
</script>

<template>
  <div class="space-y-6 mb-12">
    <!-- status row -->
    <div class="flex items-center gap-3 px-5 py-4">
      <!-- indicator + spinner -->
      <div class="relative">
        <div class="w-4 h-4 rounded-full" :class="indicatorClass"></div>

        <!-- spinner overlay when loading -->
        <div
          v-if="showSpinner"
          class="absolute -top-1 -left-1 w-6 h-6 border-2 border-gray-300 border-t-black rounded-full animate-spin"
        ></div>
      </div>

      <!-- text -->
      <span class="text-gray-700 font-medium">
        {{ errorMessage || label || 'waiting to analysis' }}
      </span>
    </div>

    <!-- error message (explicit block as well, in case you want styling) -->
    <div v-if="errorMessage" class="px-5 text-sm text-red-600">
      {{ errorMessage }}
    </div>

    <!-- runs table -->
    <div
      v-if="hasRuns"
      class="bg-white rounded-2xl shadow-sm border border-gray-200 p-4 mx-5"
    >
      <div class="flex items-center justify-between mb-2">
        <h3 class="text-sm font-semibold text-gray-800">
          Analysis details ({{ runs.length }} deviations)
        </h3>
      </div>

      <div class="overflow-x-auto">
        <table class="min-w-full text-xs text-left">
          <thead>
            <tr class="border-b border-gray-200 text-gray-500">
              <th class="py-2 pr-4">Line ID</th>
              <th class="py-2 pr-4">Parameter</th>
              <th class="py-2 pr-4">Guide word</th>
              <th class="py-2 pr-4 text-right">Tokens used</th>
            </tr>
          </thead>
          <tbody>
            <tr
              v-for="(run, idx) in runs"
              :key="`${run.line_id}-${run.parameter}-${run.guide_word}-${idx}`"
              class="border-b border-gray-100 last:border-0"
            >
              <td class="py-1.5 pr-4 font-medium text-gray-800">
                {{ run.line_id }}
              </td>
              <td class="py-1.5 pr-4 text-gray-700">
                {{ run.parameter }}
              </td>
              <td class="py-1.5 pr-4 text-gray-700">
                {{ run.guide_word }}
              </td>
              <td class="py-1.5 pr-4 text-right text-gray-700">
                {{ run.tokens_used ?? '–' }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <!-- saved path -->
      <div v-if="fullPath" class="mt-3 text-xs text-gray-600">
        <span class="font-semibold">Saved to:</span>
        <span class="ml-1 font-mono break-all">
          {{ fullPath }}
        </span>
      </div>
    </div>

    <!-- start button -->
    <div class="flex justify-center">
      <button
        @click="emit('start')"
        class="px-8 py-3 bg-black text-white rounded-lg hover:bg-gray-800 transition text-lg font-medium"
        :disabled="active"
        :class="active ? 'opacity-60 cursor-not-allowed' : ''"
      >
        Start analysis
      </button>
    </div>
  </div>
</template>
