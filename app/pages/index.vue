<template>
  <div class="min-h-screen bg-gradient-to-br from-slate-50 to-slate-100 flex items-center justify-center p-8">
    <div class="w-full max-w-3xl">
      <!-- Header -->
      <div class="text-center mb-12">
        <div class="flex items-center justify-start mb-6">
          <div class="w-10 h-10 bg-gray-300 rounded-full"></div>
          <span class="ml-3 text-gray-600">KU Che</span>
        </div>
        <h1 class="text-5xl font-bold text-gray-900 mb-3">
          Agent-Based<br />Automated HAZOP Analysis
        </h1>
        <p class="text-gray-500 text-lg">Go ahead and Ready when you are.</p>
        <div class="flex gap-3 justify-center mt-6">
          <button class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition">
            Call to action
          </button>
          <button class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition">
            search
          </button>
        </div>
      </div>

      <!-- Process Input Section -->
      <ProcessInput v-model:name="processName" v-model:description="processDescription" />

      <!-- Extract Status -->
      <div class="flex items-center gap-3 mb-6 mt-12">
        <div :class="['w-4 h-4 rounded-full', isExtracting ? 'bg-green-500' : 'bg-gray-300']"></div>
        <span class="text-gray-600">extract complete</span>
      </div>

      <!-- JSON Result Display -->
      <div class="bg-gray-200 rounded-2xl p-8 mb-6 h-64 flex items-center justify-center">
        <p class="text-gray-500">showing result JSON extract file</p>
      </div>

      <!-- Action Buttons -->
      <div class="flex gap-3 justify-center mb-8">
        <button @click="handleExtract" class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition">
          Call to HAZOP analysis
        </button>
        <button class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition">
          exit
        </button>
      </div>

      <!-- Node Selection -->
      <NodeSelection v-model="selectedNodes" :nodes="nodes" />

      <!-- Deviation Selection -->
      <DeviationSelection v-model="selectedDeviations" />

      <!-- Analysis Status -->
      <div class="flex items-center gap-3 mb-6">
        <div class="w-10 h-10 bg-gray-400 rounded-full"></div>
        <span class="text-gray-600">waiting to analysis</span>
      </div>

      <!-- Start Analysis Button -->
      <div class="flex justify-center">
        <button class="px-8 py-3 bg-black text-white rounded-lg hover:bg-gray-800 transition text-lg font-medium">
          Start analysis
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import ProcessInput from "../components/ProcessInput.vue"
import NodeSelection from "../components/NodeSelection.vue"
import DeviationSelection from "../components/DeviationSelection.vue"
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