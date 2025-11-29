<template>
  <div class="min-h-screen bg-linear-to-br from-slate-50 to-slate-100 flex items-center justify-center p-8">
    <div class="w-full max-w-6xl">
      <PageHeader />

      <!-- Process Input Section -->
      <ProcessInput v-model:name="processName" v-model:description="processDescription" />

      <!-- Extract Status -->
      <ExtractStatus :active="isExtracting" />

      <!-- JSON Result Display -->
      <JsonResultDisplay />

      <!-- Action Buttons -->
      <ActionButtons @extract="handleExtract" />

      <!-- Node Selection -->
      <NodeSelection v-model="selectedNodes" :nodes="nodes" />

      <!-- Deviation Selection -->
      <DeviationSelection v-model="selectedDeviations" />

      <!-- Analysis Status -->
      <AnalysisControls />
    </div>
  </div>
</template>

<script setup>
import ActionButtons from "../components/ActionButton.vue"
import ExtractStatus from "../components/ExtractStatus.vue"
import JsonResultDisplay from "../components/JsonDisplay.vue"
import PageHeader from "../components/PageHeader.vue"
import ProcessInput from "../components/ProcessInput.vue"
import NodeSelection from "../components/NodeSelection.vue"
import DeviationSelection from "../components/DeviationSelection.vue"
import AnalysisControls from "../components/AnalysisControl.vue"
const processName = ref('')
const processDescription = ref('')
const selectedNodes = ref([])
const selectedDeviations = ref({})
const isExtracting = ref(false)

const nodes = [
  { id: 1, name: 'node 1', range: 'From ST-101 to HT-101', context: 'context' },
  { id: 2, name: 'node 2', range: 'From ST-101 to HT-101', context: 'context' },
  { id: 3, name: 'node 3', range: 'From ST-101 to HT-101', context: 'context' },
  { id: 4, name: 'node 4', range: 'From ST-101 to HT-101', context: 'context' }
]

const handleExtract = () => {
  isExtracting.value = true
  setTimeout(() => {
    isExtracting.value = false
  }, 2000)
}
</script>