<script setup lang="ts">
import { ref, computed, watch, nextTick } from 'vue'
import PageHeader from '~/components/PageHeader.vue'
import ProcessInput from '~/components/ProcessInput.vue'
import ExtractStatus from '~/components/ExtractStatus.vue'
import JsonDisplay from '~/components/JsonDisplay.vue'
import ActionButtons from '~/components/ActionButton.vue'
import NodeSelection from '~/components/NodeSelection.vue'
import DeviationSelection from '~/components/DeviationSelection.vue'
import AnalysisControl from '~/components/AnalysisControl.vue' 

import type { NodeItem } from '~/components/NodeSelection.vue'
import type { DeviationItem } from '~/components/DeviationSelection.vue'

// ---- Stage control ----
type Stage = 'initial' | 'input' | 'extract' | 'json' | 'node' | 'deviation' | 'analysis'
const stage = ref<Stage>('initial')

// v-model fields
const processName = ref('')
const processDescription = ref('')

// Extract label
const extractLabel = ref('Extracting...')

// ⚠️ you still need to change this to the proper Record<DeviationType, string[]>
// leaving as-is because your question is about scrolling
const deviationSelections = ref(1)
const deviationCurrentNode = ref(1)
const totalDeviationNodes = ref(5)

// Action state
type ActionState = 'idle' | 'ready' | 'running'
const actionState = ref<ActionState>('idle')

// NodeSelection data
const nodes = ref<NodeItem[]>([
  { id: 'N1', label: 'Node 1 - Feed' },
  { id: 'N2', label: 'Node 2 - Heater' },
  { id: 'N3', label: 'Node 3 - Column' },
  { id: 'N4', label: 'Node 4 - Product' }
])

const selectedNodes = ref<(string | number)[]>([])

// DeviationSelection data (mock)
const deviations = ref<DeviationItem[]>([
  { id: 'D1', label: 'More Flow' },
  { id: 'D2', label: 'Less Flow' },
  { id: 'D3', label: 'No Flow' },
  { id: 'D4', label: 'Reverse Flow' }
])

const selectedDeviations = ref<(string | number)[]>([])

// 🔁 When label becomes "Complete" → show JSON + enable actions
watch(extractLabel, (newVal) => {
  if (newVal === 'Complete') {
    stage.value = 'json'
    actionState.value = 'ready'
  }
})

// ✅ Auto-scroll when stage changes
watch(stage, async (newStage) => {
  if (typeof window === 'undefined') return

  // wait until DOM has updated with new components
  await nextTick()

  // when we go deeper in the flow, scroll to bottom
  if (['json', 'node', 'deviation', 'analysis'].includes(newStage)) {
    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: 'smooth'
    })
  }

  // when going back to input (if you ever do), scroll to top
  if (newStage === 'input') {
    window.scrollTo({ top: 0, behavior: 'smooth' })
  }
})

// Top padding
const mainPaddingClass = computed(() => {
  switch (stage.value) {
    case 'initial':
      return 'pt-90'        // pt-90 is not a valid Tailwind class
    case 'input':
      return 'pt-28'
    case 'extract':
    case 'json':
    case 'node':
    case 'deviation':
    case 'analysis':
    default:
      return 'pt-28'
  }
})

// CTA from PageHeader → show ProcessInput
const handleCtaClick = () => {
  stage.value = 'input'
}

// Button inside ProcessInput → show ExtractStatus, move everything up
const handleStartExtract = () => {
  stage.value = 'extract'
  extractLabel.value = 'Extracting…'

  // mock backend call
  setTimeout(() => {
    extractLabel.value = 'Complete'
  }, 2000)
}

// ActionButtons: Call to HAZOP → show NodeSelection
const handleCallHazop = () => {
  actionState.value = 'running'
  stage.value = 'node'
}

// NodeSelection → show DeviationSelection
const handleNodeNext = () => {
  stage.value = 'deviation'
}

// DeviationSelection → show AnalysisControl
const handleDeviationNext = () => {
  stage.value = 'analysis'
}

const handleDeviationPreview = () => {
  // later: open preview dialog/panel
}
</script>




<template>
  <div class="min-h-screen bg-linear-to-br from-slate-50 to-slate-100">

    <!-- ✅ Fixed KU Che bar (always at top, doesn’t move when scroll) -->
    <div class="w-full max-w-6xl fixed top-5 left-20 z-50 bg-slate-50">
      <div class="max-w-6xl mx-auto flex items-center justify-start px-8 py-4">
        <div class="w-10 h-10 bg-gray-300 rounded-full"></div>
        <span class="ml-3 text-gray-600 font-semibold">KU Che</span>
      </div>
    </div>

    <!-- ✅ Main content, pushed down so it’s not under the bar -->
    <div class="pt-20 px-8 flex justify-center transition-all duration-500 ease-out"
         :class="mainPaddingClass">
      <div class="w-full max-w-6xl">
        <!-- PageHeader, ProcessInput, ExtractStatus, JsonDisplay, ActionButtons, NodeSelection, DeviationSelection, etc. -->
        <PageHeader
          class="mb-6"
          @cta-click="handleCtaClick"
        />

        <!-- ProcessInput -->
        <Transition name="fade-slide">
          <ProcessInput
            v-if="stage !== 'initial'"
            v-model:name="processName"
            v-model:description="processDescription"
            class="mb-4"
            @start-extract="handleStartExtract"
          />
        </Transition>

        <!-- ExtractStatus -->
        <Transition name="fade-slide">
          <ExtractStatus
            v-if="['extract', 'json', 'node', 'deviation', 'analysis'].includes(stage)"
            class="mt-4"
            :active="stage === 'extract'"
            :label="extractLabel"
          />
        </Transition>

        <!-- JSON result -->
        <Transition name="fade-slide">
          <JsonDisplay
            v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)"
            class="mt-4"
          />
        </Transition>

        <!-- ActionButtons -->
        <Transition name="fade-slide">
          <ActionButtons
            v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)"
            class="mt-6"
            :state="actionState"
            @call-hazop="handleCallHazop"
          />
        </Transition>

        <!-- NodeSelection -->
        <Transition name="fade-slide">
          <NodeSelection
            v-if="['node', 'deviation', 'analysis'].includes(stage)"
            v-model="selectedNodes"
            :nodes="nodes"
            class="mt-4"
             @next="handleNodeNext" 
          />
        </Transition>

        <!-- ✅ DeviationSelection -->
        <Transition name="fade-slide">
          <DeviationSelection
            v-if="stage === 'deviation' || stage === 'analysis'"
            v-model="deviationSelections"          
            :current-node="deviationCurrentNode"
            :total-nodes="deviationTotalNodes"
            :node-title="`node ${deviationCurrentNode}`"
            class="mt-4"
            @preview="handleDeviationPreview"
            @next="handleDeviationNext"
          />

        </Transition>

        <!-- ✅ AnalysisControl appears AFTER deviation confirm -->
        <Transition name="fade-slide">
          <AnalysisControl
            v-if="stage === 'analysis'"
            class="mt-4"
          />
        </Transition>
      </div>
    </div>
  </div>
</template>

<style scoped>
.fade-slide-enter-active,
.fade-slide-leave-active {
  transition: all 1s ease;
}

.fade-slide-enter-from,
.fade-slide-leave-to {
  opacity: 0;
  transform: translateY(12px);
}
</style>