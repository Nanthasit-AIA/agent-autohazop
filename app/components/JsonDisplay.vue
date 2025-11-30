<script setup lang="ts">
import { ref, computed, watch } from 'vue'

type SectionId =
  | 'process_description'
  | 'system_input'
  | 'equipment'
  | 'valves'
  | 'instruments'
  | 'utility_lines'
  | 'connections'

interface SectionConfig {
  id: SectionId
  key: string
  label: string
}

const props = defineProps<{
  data: any
  isLoading?: boolean
  fileName?: string
}>()

// 🔢 define desired order
const sectionConfigs: SectionConfig[] = [
  { id: 'process_description', key: 'process_description', label: 'Process Description' },
  { id: 'system_input',        key: 'system_input',        label: 'System Input' },
  { id: 'equipment',           key: 'equipment',           label: 'Equipment' },
  { id: 'valves',              key: 'valves',              label: 'Valves' },
  { id: 'instruments',         key: 'instruments',         label: 'Instruments' },
  { id: 'utility_lines',       key: 'utility_lines',       label: 'Utility Lines' },
  { id: 'connections',         key: 'connections',         label: 'Connections' }
]

// only keep sections that actually exist in data
const availableSections = computed(() => {
  if (!props.data || typeof props.data !== 'object') return []
  return sectionConfigs.filter(sec => sec.key in props.data && props.data[sec.key] !== undefined)
})

const currentSectionId = ref<SectionId | null>(null)

watch(
  availableSections,
  (secs) => {
    if (!secs.length) {
      currentSectionId.value = null
      return
    }
    // default to first section if none selected or current no longer exists
    if (!currentSectionId.value || !secs.some(s => s.id === currentSectionId.value)) {
      currentSectionId.value = secs[0].id
    }
  },
  { immediate: true }
)

const currentSection = computed(() =>
  availableSections.value.find(s => s.id === currentSectionId.value) ?? null
)

const currentIndex = computed(() => {
  if (!currentSection.value) return -1
  return availableSections.value.findIndex(s => s.id === currentSection.value!.id)
})

const sectionData = computed(() => {
  if (!currentSection.value || !props.data) return null
  return props.data[currentSection.value.key]
})

const isPrimitiveSection = computed(() => {
  const val = sectionData.value
  const t = typeof val
  return val == null || t === 'string' || t === 'number' || t === 'boolean'
})

const isArrayOfObjects = computed(() => {
  return Array.isArray(sectionData.value) && sectionData.value.length > 0 && typeof sectionData.value[0] === 'object'
})

const prettySectionJson = computed(() =>
  sectionData.value != null ? JSON.stringify(sectionData.value, null, 2) : ''
)

const switchSection = (id: SectionId) => {
  currentSectionId.value = id
}

const goPrev = () => {
  if (currentIndex.value <= 0) return
  const prev = availableSections.value[currentIndex.value - 1]
  currentSectionId.value = prev.id
}

const goNext = () => {
  if (currentIndex.value < 0 || currentIndex.value >= availableSections.value.length - 1) return
  const next = availableSections.value[currentIndex.value + 1]
  currentSectionId.value = next.id
}
</script>

<template>
  <div class="bg-white rounded-2xl p-6 shadow-lg w-full max-w-6xl mx-auto">
    <!-- Header: file name + section buttons -->
    <div class="flex flex-col gap-3 md:flex-row md:items-center md:justify-between mb-4">
      <div class="text-sm text-gray-500" v-if="fileName">
        File: <span class="font-medium text-gray-700">{{ fileName }}</span>
      </div>

      <div
        v-if="availableSections.length"
        class="flex flex-wrap gap-2"
      >
        <button
          v-for="sec in availableSections"
          :key="sec.id"
          class="px-3 py-1.5 rounded-full text-xs font-medium border transition"
          :class="
            sec.id === currentSectionId
              ? 'bg-black text-white border-black'
              : 'bg-gray-100 text-gray-700 border-gray-300 hover:bg-gray-200'
          "
          @click="switchSection(sec.id)"
        >
          {{ sec.label }}
        </button>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="isLoading" class="text-sm text-gray-500">
      Loading JSON…
    </div>

    <!-- No data -->
    <div
      v-else-if="!data || !availableSections.length"
      class="text-sm text-gray-500"
    >
      No structured sections found in JSON data.
    </div>

    <!-- Current section view -->
    <div v-else>
      <div class="flex items-center justify-between mb-2">
        <h2 class="text-lg font-semibold text-gray-800">
          {{ currentSection?.label }}
        </h2>
        <span class="text-xs text-gray-500">
          Section {{ currentIndex + 1 }} / {{ availableSections.length }}
        </span>
      </div>

      <!-- Content box -->
      <div class="border border-gray-200 rounded-2xl p-4 bg-slate-50">
        <!-- simple string / number / boolean -->
        <p
          v-if="isPrimitiveSection"
          class="text-sm text-gray-800 whitespace-pre-line"
        >
          {{ sectionData }}
        </p>

        <!-- array of objects: show cards -->
        <div
          v-else-if="isArrayOfObjects"
          class="grid gap-3 md:grid-cols-2"
        >
          <div
            v-for="(item, idx) in sectionData"
            :key="idx"
            class="bg-white rounded-xl border border-gray-200 p-3 text-xs text-gray-800"
          >
            <div
              v-for="(val, key) in item"
              :key="String(key)"
              class="flex justify-between gap-2"
            >
              <span class="text-gray-500">{{ key }}</span>
              <span class="font-medium break-all">{{ val }}</span>
            </div>
          </div>
        </div>

        <!-- fallback: pretty JSON -->
        <pre
          v-else
          class="text-xs text-gray-800 whitespace-pre overflow-x-auto"
        >{{ prettySectionJson }}</pre>
      </div>

      <!-- Navigation buttons -->
      <div
        v-if="availableSections.length > 1"
        class="flex items-center justify-between mt-4 text-xs"
      >
        <button
          class="px-3 py-1.5 rounded-full border border-gray-300 text-gray-700 disabled:opacity-40 disabled:cursor-not-allowed"
          :disabled="currentIndex <= 0"
          @click="goPrev"
        >
          ← Previous
        </button>

        <div class="text-gray-500">
          Use the buttons above to jump to any section.
        </div>

        <button
          class="px-3 py-1.5 rounded-full border border-gray-300 text-gray-700 disabled:opacity-40 disabled:cursor-not-allowed"
          :disabled="currentIndex >= availableSections.length - 1"
          @click="goNext"
        >
          Next →
        </button>
      </div>
    </div>
  </div>
</template>
