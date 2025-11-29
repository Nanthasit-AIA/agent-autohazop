<script setup lang="ts">
import { computed } from 'vue'

type DeviationType =
  | 'Flow'
  | 'Pressure'
  | 'Temperature'
  | 'Level'
  | 'Concentration'
  | 'Composition'

const deviationTypes: DeviationType[] = [
  'Flow',
  'Pressure',
  'Temperature',
  'Level',
  'Concentration',
  'Composition'
]

const deviationOptionsMap: Record<DeviationType, string[]> = {
  Flow: ['More', 'Less', 'No', 'Reverse'],
  Pressure: ['More', 'Less'],
  Temperature: ['More', 'Less'],
  Level: ['More', 'Less', 'No'],
  Concentration: ['More', 'Less'],
  Composition: ['Other than']
}

const maxPageButtons = 5

const props = defineProps<{
  // Example shape:
  // {
  //   Flow: ['More', 'Less'],
  //   Pressure: [],
  //   ...
  // }
  modelValue: Record<DeviationType, string[]>
  currentNode?: number
  totalNodes?: number

  // Optional node info (you can send from backend)
  nodeTitle?: string        // e.g. "node 1"
  nodeLine?: string         // e.g. "From ST-101 to HT-101"
  nodeContext?: string      // e.g. "context"
}>()

const emit = defineEmits<{
  'update:modelValue': [Record<DeviationType, string[]>]
  'update:currentNode': [number]
  preview: []
  next: []
}>()

const currentNode = computed(() => props.currentNode ?? 1)
const totalNodes = computed(() => props.totalNodes ?? 5)

const pages = computed(() => {
  const count = Math.min(totalNodes.value, maxPageButtons)
  return Array.from({ length: count }, (_, i) => i + 1)
})

const setSelections = (type: DeviationType, options: string[]) => {
  emit('update:modelValue', {
    ...props.modelValue,
    [type]: options
  })
}

const isSelected = (type: DeviationType, option: string) => {
  return props.modelValue[type]?.includes(option) ?? false
}

const toggleOption = (type: DeviationType, option: string) => {
  const current = props.modelValue[type] ?? []
  const next = current.includes(option)
    ? current.filter(o => o !== option)      // unselect one
    : [...current, option]                   // select one

  setSelections(type, next)
}

const toggleAll = (type: DeviationType) => {
  const allOptions = deviationOptionsMap[type]
  const current = props.modelValue[type] ?? []
  const allSelected = allOptions.every(o => current.includes(o))

  const next = allSelected ? [] : [...allOptions] // clear or select all
  setSelections(type, next)
}

const selectAll = () => {
  const next: Record<DeviationType, string[]> = {} as any
  deviationTypes.forEach(type => {
    next[type] = [...deviationOptionsMap[type]]
  })
  emit('update:modelValue', next)
}

const deleteAll = () => {
  const empty: Record<DeviationType, string[]> = {} as any
  deviationTypes.forEach(type => {
    empty[type] = []
  })
  emit('update:modelValue', empty)
}

const changePage = (page: number) => {
  emit('update:currentNode', page)
}

const goPrev = () => {
  if (currentNode.value > 1) {
    emit('update:currentNode', currentNode.value - 1)
  }
}

const goNext = () => {
  if (currentNode.value < totalNodes.value) {
    emit('update:currentNode', currentNode.value + 1)
  }
}
</script>

<template>
  <div class="bg-white border-2 border-gray-300 rounded-2xl px-8 py-6 mb-6">
    <!-- Title -->
    <h3 class="font-semibold text-gray-800 mb-4">
      Choose perform deviation
    </h3>

    <!-- Main: left node info + right deviation list -->
    <div class="flex gap-8">
      <!-- Left column: node info + actions -->
      <div class="w-52 flex flex-col gap-4">
        <div class="text-sm text-gray-600 leading-snug">
          <div class="font-medium">
            {{ nodeTitle || `node ${currentNode}` }} :
          </div>
          <div v-if="nodeLine">
            {{ nodeLine }}
          </div>
          <div v-if="nodeContext">
            {{ nodeContext }}
          </div>
        </div>

        <div class="flex flex-col gap-2">
          <button
            type="button"
            @click="selectAll"
            class="w-28 h-10 rounded-lg bg-black text-white text-sm font-semibold hover:bg-gray-900 transition"
          >
            select all
          </button>
          <button
            type="button"
            @click="deleteAll"
            class="w-28 h-10 rounded-lg bg-white text-gray-900 text-sm font-semibold border border-gray-300 hover:bg-gray-50 transition"
          >
            delete all
          </button>
        </div>
      </div>

      <!-- Right column: deviation items -->
      <div class="flex-1 space-y-2">
        <div
          v-for="type in deviationTypes"
          :key="type"
          class="w-full flex items-center gap-3"
        >
          <!-- dot + deviation name (click => select/clear all options for that type) -->
          <div
            class="flex items-center gap-2 cursor-pointer"
            @click="toggleAll(type)"
          >
            <span
              class="w-3 h-3 rounded-full"
              :class="(modelValue[type]?.length ?? 0) > 0 ? 'bg-black' : 'bg-gray-300'"
            ></span>

            <span class="w-28 text-sm text-gray-700 hover:underline">
              {{ type }}
            </span>
          </div>

          <!-- options pill -->
          <div
            class="inline-flex flex-wrap items-center gap-1 bg-gray-200 rounded-full px-3 py-1"
          >
            <button
              v-for="opt in deviationOptionsMap[type]"
              :key="opt"
              type="button"
              class="px-2 py-0.5 rounded-full text-xs transition"
              :class="
                isSelected(type, opt)
                  ? 'bg-black text-white'
                  : 'bg-transparent text-gray-800'
              "
              @click.stop="toggleOption(type, opt)"
            >
              {{ opt }}
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Footer: pagination + preview/next -->
    <div class="mt-6 flex items-center justify-between">
      <!-- pagination -->
      <div class="flex items-center gap-2 text-sm text-gray-700">
        <button
          type="button"
          class="px-1 disabled:opacity-40"
          @click="goPrev"
          :disabled="currentNode === 1"
        >
          ←
        </button>

        <button
          v-for="page in pages"
          :key="page"
          type="button"
          class="w-7 h-7 flex items-center justify-center rounded-full text-xs"
          :class="
            page === currentNode ? 'bg-black text-white' : 'text-gray-700'
          "
          @click="changePage(page)"
        >
          {{ page }}
        </button>

        <span v-if="totalNodes > maxPageButtons" class="px-1">
          ...
        </span>

        <button
          type="button"
          class="px-1 disabled:opacity-40"
          @click="goNext"
          :disabled="currentNode === totalNodes"
        >
          →
        </button>
      </div>

      <!-- Preview + next -->
      <div class="flex items-center gap-3">
        <button
          type="button"
          class="px-5 py-2 rounded-full bg-black text-white text-sm font-semibold hover:bg-gray-900 transition"
          @click="$emit('preview')"
        >
          Preview
        </button>
        <button
          type="button"
          class="w-10 h-10 rounded-full border border-gray-400 flex items-center justify-center hover:bg-gray-100 transition"
          @click="$emit('next')"
        >
          →
        </button>
      </div>
    </div>
  </div>
</template>
