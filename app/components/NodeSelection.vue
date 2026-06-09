<script setup lang="ts">
import { ref, computed } from 'vue'
import SelectedPipelineGraph from '~/components/SelectedPipelineGraph.vue'

export interface Connection {
  line_id: string
  from_id: string
  to_id: string
  context?: string
}

export interface NodeItem {
  id: string | number
  name: string
  range?: string
  context?: string
  nodeBoundary?: string
  flowDirection?: string
  source?: 'connections' | 'line_level_connections'
  equipmentSummary?: string
  valveSummary?: string
  instrumentSummary?: string
}

const props = defineProps<{
  modelValue: (string | number)[]
  nodes: NodeItem[]
  connections: Connection[]
}>()

const emit = defineEmits<{
  'update:modelValue': [(string | number)[]]
  next: []
}>()

const showGraph = ref(false)
const searchText = ref('')
const sourceFilter = ref<'all' | 'connections' | 'line_level_connections'>('all')

const filteredNodes = computed(() => {
  const q = searchText.value.trim().toLowerCase()

  return props.nodes.filter((node) => {
    const sourceMatch = sourceFilter.value === 'all' || node.source === sourceFilter.value
    if (!sourceMatch) return false

    if (!q) return true

    const searchable = [
      node.id,
      node.name,
      node.range,
      node.context,
      node.nodeBoundary,
      node.flowDirection,
      node.equipmentSummary,
      node.valveSummary,
      node.instrumentSummary,
    ]
      .filter(Boolean)
      .join(' ')
      .toLowerCase()

    return searchable.includes(q)
  })
})

const groupedNodeCount = computed(
  () => props.nodes.filter((node) => node.source === 'connections').length
)

const lineLevelNodeCount = computed(
  () => props.nodes.filter((node) => node.source === 'line_level_connections').length
)

const toggleNode = (nodeId: string | number) => {
  const exists = props.modelValue.includes(nodeId)
  const newValue = exists
    ? props.modelValue.filter((id) => id !== nodeId)
    : [...props.modelValue, nodeId]

  emit('update:modelValue', newValue)
}

const handleNextClick = () => {
  emit('next')
}

const handleSelectAll = () => {
  const allIds = filteredNodes.value.map((node) => node.id)
  const merged = Array.from(new Set([...props.modelValue, ...allIds]))
  emit('update:modelValue', merged)
}

const handleClearAll = () => {
  if (!filteredNodes.value.length) {
    emit('update:modelValue', [])
    return
  }

  const filteredIds = new Set(filteredNodes.value.map((node) => String(node.id)))
  emit(
    'update:modelValue',
    props.modelValue.filter((id) => !filteredIds.has(String(id)))
  )
}

const selectedConnections = computed(() => {
  if (!props.connections?.length || !props.modelValue.length) return []

  const selectedIds = new Set(props.modelValue.map((v) => String(v)))

  return props.connections.filter((conn) => selectedIds.has(String(conn.line_id)))
})

const handlePreviewClick = () => {
  if (selectedConnections.value.length === 0) return
  showGraph.value = true
}

const handleCloseGraph = () => {
  showGraph.value = false
}

const sourceLabel = (source?: string) => {
  if (source === 'line_level_connections') return 'Line-level'
  if (source === 'connections') return 'Node group'
  return 'Node'
}
</script>

<template>
  <div class="bg-white rounded-2xl p-6 shadow-lg mb-6">
    <div class="flex flex-col gap-4 mb-6 mt-2 lg:flex-row lg:items-center lg:justify-between">
      <div>
        <h3 class="font-black text-gray-800 text-2xl">
          Choose HAZOP Nodes: {{ modelValue.length }}/{{ nodes.length }}
        </h3>
        <p class="text-sm text-gray-500 mt-1">
          Node groups: {{ groupedNodeCount }} · Line-level nodes: {{ lineLevelNodeCount }}
        </p>
      </div>

      <div class="flex flex-wrap gap-2">
        <button
          type="button"
          class="px-3 py-1 text-sm font-semibold rounded-lg border border-gray-300 text-white bg-black hover:bg-gray-900 transition disabled:opacity-40"
          :disabled="filteredNodes.length === 0"
          @click="handleSelectAll"
        >
          Select shown
        </button>
        <button
          type="button"
          class="px-3 py-1 text-sm font-semibold rounded-lg border border-gray-300 bg-white hover:bg-gray-50 transition disabled:opacity-40"
          :disabled="modelValue.length === 0"
          @click="handleClearAll"
        >
          Clear shown
        </button>
      </div>
    </div>

    <div class="grid grid-cols-1 gap-3 mb-5 md:grid-cols-[1fr_auto]">
      <input
        v-model="searchText"
        type="text"
        placeholder="Search node; equipment; valve; instrument; boundary; context..."
        class="w-full rounded-xl border border-gray-300 px-4 py-2 text-sm focus:outline-none focus:ring-2 focus:ring-black/10"
      />
      <select
        v-model="sourceFilter"
        class="rounded-xl border border-gray-300 px-3 py-2 text-sm bg-white focus:outline-none focus:ring-2 focus:ring-black/10"
      >
        <option value="all">All node sources</option>
        <option value="connections">Node groups only</option>
        <option value="line_level_connections">Line-level only</option>
      </select>
    </div>

    <div
      class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4"
      :class="filteredNodes.length > 4 ? 'max-h-[560px] overflow-y-auto pr-2' : ''"
    >
      <label
        v-for="node in filteredNodes"
        :key="node.id"
        class="flex items-start gap-3 cursor-pointer rounded-2xl border border-gray-200 p-4 hover:bg-slate-50 transition"
        :class="modelValue.includes(node.id) ? 'border-black bg-slate-50' : ''"
      >
        <input
          type="checkbox"
          :checked="modelValue.includes(node.id)"
          @change="toggleNode(node.id)"
          class="mt-1"
        />
        <div class="flex-1 min-w-0">
          <div class="flex flex-wrap items-center gap-2 mb-1">
            <span class="text-[11px] font-black uppercase tracking-wide rounded-full bg-gray-100 px-2 py-0.5 text-gray-600">
              {{ sourceLabel(node.source) }}
            </span>
            <span class="text-xs font-black text-gray-500 break-all">
              {{ node.id }}
            </span>
          </div>

          <div class="font-bold text-gray-800 wrap-break-word">
            {{ node.name }}
          </div>

          <div v-if="node.range" class="text-sm text-gray-600 mt-1">
            <span class="font-black">connection:</span>
            {{ node.range }}
          </div>

          <div v-if="node.flowDirection" class="text-sm text-gray-600 mt-1">
            <span class="font-black">flow:</span>
            {{ node.flowDirection }}
          </div>

          <div v-if="node.nodeBoundary" class="text-sm text-gray-600 mt-1 line-clamp-3">
            <span class="font-black">boundary:</span>
            {{ node.nodeBoundary }}
          </div>

          <div v-if="node.context" class="text-sm text-gray-500 mt-1 line-clamp-3">
            <span class="font-black">description:</span>
            {{ node.context }}
          </div>

          <div class="mt-3 grid gap-1 text-xs text-gray-500">
            <div v-if="node.equipmentSummary">
              <span class="font-black text-gray-600">equipment:</span>
              {{ node.equipmentSummary }}
            </div>
            <div v-if="node.valveSummary">
              <span class="font-black text-gray-600">valves:</span>
              {{ node.valveSummary }}
            </div>
            <div v-if="node.instrumentSummary">
              <span class="font-black text-gray-600">instruments:</span>
              {{ node.instrumentSummary }}
            </div>
          </div>
        </div>
      </label>
    </div>

    <div v-if="nodes.length && filteredNodes.length === 0" class="text-sm text-gray-500 border rounded-xl p-4 bg-slate-50">
      No nodes match the current filter.
    </div>

    <div class="flex items-center justify-end mt-4">
      <div class="flex gap-3">
        <button
          class="px-6 py-2 bg-white border border-gray-300 text-gray-800 rounded-lg hover:bg-gray-50 transition disabled:opacity-40 disabled:cursor-not-allowed"
          type="button"
          :disabled="modelValue.length === 0 || selectedConnections.length === 0"
          @click="handlePreviewClick"
        >
          Preview selected graph
        </button>
        <button
          class="w-10 h-10 bg-black text-white border border-black rounded-lg flex items-center justify-center hover:bg-gray-800 transition disabled:opacity-40 disabled:cursor-not-allowed"
          type="button"
          :disabled="modelValue.length === 0"
          @click="handleNextClick"
          title="Continue to deviation selection"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            width="20"
            height="20"
            viewBox="0 0 24 24"
            fill="none"
            stroke="currentColor"
            stroke-width="2"
            stroke-linecap="round"
            stroke-linejoin="round"
          >
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>
  </div>

  <SelectedPipelineGraph
    :show="showGraph"
    :connections="selectedConnections"
    @close="handleCloseGraph"
  />
</template>
