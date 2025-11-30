<script setup lang="ts">
import { computed, ref } from "vue";

type DeviationType =
  | "Flow"
  | "Pressure"
  | "Temperature"
  | "Level"
  | "Concentration"
  | "Composition";

// options per type
const deviationTypes: DeviationType[] = [
  "Flow",
  "Pressure",
  "Temperature",
  "Level",
  "Concentration",
  "Composition",
];

const deviationOptionsMap: Record<DeviationType, string[]> = {
  Flow: ["More", "Less", "No", "Reverse"],
  Pressure: ["More", "Less"],
  Temperature: ["More", "Less"],
  Level: ["More", "Less", "No"],
  Concentration: ["More", "Less"],
  Composition: ["Other than"],
};

interface PreviewNode {
  id: string | number;
  name: string;
  range?: string;
  context?: string;
}

const props = defineProps<{
  // v-model for CURRENT node (per-page)
  modelValue: Record<DeviationType, string[]>;

  // pagination for nodes
  currentNode?: number;
  totalNodes?: number;

  // current node display info
  nodeTitle?: string;
  nodeLine?: string;
  nodeContext?: string;

  // all selected nodes and their full selections (for popup)
  allNodes: PreviewNode[];
  allSelections: Record<string | number, Record<DeviationType, string[]>>;

  // 🔹 new: analysis configuration
  analysisFileName?: string;
  outputFolder?: string;
}>();

const emit = defineEmits<{
  "update:modelValue": [Record<DeviationType, string[]>];
  "update:currentNode": [number];
  "update:analysisFileName": [string];
  "update:outputFolder": [string];
  preview: [];
  next: [];
}>();

// ---------- v-model wrappers for analysis config ----------
const analysisFile = computed<string>({
  get() {
    return props.analysisFileName ?? "";
  },
  set(val: string) {
    emit("update:analysisFileName", val);
  },
});

const outputFolder = computed<string>({
  get() {
    return props.outputFolder ?? "";
  },
  set(val: string) {
    emit("update:outputFolder", val);
  },
});

// ---------- pagination ----------
const currentNode = computed(() => props.currentNode ?? 1);
const totalNodes = computed(() => props.totalNodes ?? 1);

const pages = computed<number[]>(() => {
  const total = totalNodes.value;
  if (total <= 0) return [];
  return Array.from({ length: total }, (_, i) => i + 1);
});

const changePage = (page: number) => {
  emit("update:currentNode", page);
};

const goPrev = () => {
  if (currentNode.value > 1) {
    emit("update:currentNode", currentNode.value - 1);
  }
};

const goNext = () => {
  if (currentNode.value < totalNodes.value) {
    emit("update:currentNode", currentNode.value + 1);
  }
};

// ---------- selection helpers for CURRENT node ----------
const setSelections = (devType: DeviationType, options: string[]) => {
  emit("update:modelValue", {
    ...props.modelValue,
    [devType]: options,
  });
};

const getSelectionsForType = (devType: DeviationType): string[] => {
  return props.modelValue[devType] ?? [];
};

const hasSelectionsForType = (devType: DeviationType): boolean => {
  return getSelectionsForType(devType).length > 0;
};

const isSelected = (devType: DeviationType, option: string) => {
  return getSelectionsForType(devType).includes(option);
};

const toggleOption = (devType: DeviationType, option: string) => {
  const current = getSelectionsForType(devType);
  const next = current.includes(option)
    ? current.filter((o) => o !== option)
    : [...current, option];
  setSelections(devType, next);
};

const toggleAll = (devType: DeviationType) => {
  const allOptions = deviationOptionsMap[devType];
  const current = getSelectionsForType(devType);
  const allSelected = allOptions.every((o) => current.includes(o));
  const next = allSelected ? [] : [...allOptions];
  setSelections(devType, next);
};

const selectAll = () => {
  const next: Record<DeviationType, string[]> = {} as any;
  deviationTypes.forEach((devType) => {
    next[devType] = [...deviationOptionsMap[devType]];
  });
  emit("update:modelValue", next);
};

const deleteAll = () => {
  const empty: Record<DeviationType, string[]> = {} as any;
  deviationTypes.forEach((devType) => {
    empty[devType] = [];
  });
  emit("update:modelValue", empty);
};

// ---------- preview modal (all nodes) ----------
const showPreview = ref(false);

const handlePreviewClick = () => {
  showPreview.value = true;
  emit("preview");
};

const closePreview = () => {
  showPreview.value = false;
};

const handleNextClick = () => {
  emit("next");
};

// safe getter for any node + type from allSelections
const getNodeDeviation = (
  nodeId: string | number,
  devType: DeviationType
): string[] => {
  const nodeSel = props.allSelections?.[nodeId];
  if (!nodeSel) return [];
  return nodeSel[devType] ?? [];
};

const hasAnyDeviationForNode = (nodeId: string | number): boolean => {
  return deviationTypes.some((dt) => getNodeDeviation(nodeId, dt).length > 0);
};

const hasAnyDeviationSomeNode = computed(() =>
  props.allNodes.some((node: PreviewNode) => hasAnyDeviationForNode(node.id))
);
</script>

<template>
  <div class="bg-white border-2 border-gray-300 rounded-2xl px-8 py-6 mb-6">
    <!-- Title only -->
    <div class="mb-2">
      <h3 class="font-semibold text-gray-800">Choose perform deviation</h3>
    </div>

    <!-- 🔹 Analysis settings: file name + folder (JUST under title) -->
    <div class="mb-4 grid gap-4 md:grid-cols-2">
      <div class="flex flex-col gap-1">
        <label class="text-xs font-medium text-gray-700">
          Analysis file name
        </label>
        <input
          v-model="analysisFile"
          type="text"
          placeholder="e.g. hazop_L1_L2_run01.xlsx"
          class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-gray-500"
        />
      </div>

      <div class="flex flex-col gap-1">
        <label class="text-xs font-medium text-gray-700"> Output folder </label>
        <input
          v-model="outputFolder"
          type="text"
          placeholder="e.g. static/hazop_runs/2025-12-01"
          class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-gray-500"
        />
      </div>
    </div>

    <!-- Node info + pagination UNDER the analysis settings -->
    <div class="flex items-start justify-between mb-6 gap-6">
      <div class="text-sm text-gray-600 leading-snug space-y-1">
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

        <button
          type="button"
          class="px-1 disabled:opacity-40"
          @click="goNext"
          :disabled="currentNode === totalNodes"
        >
          →
        </button>
      </div>
    </div>

    <!-- Main: left actions + right deviation list -->
    <div class="flex gap-8">
      <!-- Left column: select/delete all -->
      <div class="w-52 flex flex-col gap-4">
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

      <!-- Right column: deviation items in 2-column grid -->
      <div class="flex-1">
        <div class="grid md:grid-cols-2 gap-x-8 gap-y-3">
          <div
            v-for="devType in deviationTypes"
            :key="devType"
            class="w-full flex items-center gap-3"
          >
            <!-- dot + deviation name -->
            <div
              class="flex items-center gap-2 cursor-pointer"
              @click="toggleAll(devType)"
            >
              <span
                class="w-3 h-3 rounded-full"
                :class="
                  hasSelectionsForType(devType) ? 'bg-black' : 'bg-gray-300'
                "
              ></span>

              <span class="text-sm text-gray-700 hover:underline">
                {{ devType }}
              </span>
            </div>

            <!-- options pill -->
            <div
              class="inline-flex flex-wrap items-center gap-1 bg-gray-200 rounded-full px-3 py-1"
            >
              <button
                v-for="opt in deviationOptionsMap[devType]"
                :key="opt"
                type="button"
                class="px-2 py-0.5 rounded-full text-xs transition"
                :class="
                  isSelected(devType, opt)
                    ? 'bg-black text-white'
                    : 'bg-transparent text-gray-800'
                "
                @click.stop="toggleOption(devType, opt)"
              >
                {{ opt }}
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom-right: Preview + Next -->
    <div class="mt-6 flex items-center justify-end">
      <div class="flex gap-3">
        <button
          class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition"
          @click="handlePreviewClick"
        >
          Preview
        </button>
        <button
          class="w-10 h-10 bg-white border border-gray-300 rounded-lg flex items-center justify-center hover:bg-gray-50 transition"
          @click="handleNextClick"
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

    <!-- Preview popup: all lines summary -->
    <transition name="fade">
      <div
        v-if="showPreview"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/40"
      >
        <div
          class="bg-white rounded-2xl shadow-xl max-w-3xl w-full p-6 max-h-[80vh] overflow-y-auto"
        >
          <h3 class="text-lg font-semibold text-gray-800 mb-2">
            Deviation preview for all selected lines
          </h3>
          <p class="text-sm text-gray-600 mb-4">
            Review selected deviations for each line before submitting.
          </p>

          <!-- If nothing selected at all -->
          <div
            v-if="!hasAnyDeviationSomeNode"
            class="text-sm text-gray-500 italic mb-4"
          >
            No deviations selected for any line yet.
          </div>

          <!-- For each line/node -->
          <template v-for="node in allNodes" :key="node.id">
            <div
              v-if="hasAnyDeviationForNode(node.id)"
              class="mb-4 p-4 rounded-xl border border-gray-200 bg-gray-50"
            >
              <!-- Header: L1 (D60-Storage → D60-Heater) -->
              <h4 class="font-semibold text-gray-800 mb-1">
                {{ node.name }}
              </h4>

              <!-- optional line info -->
              <div class="text-xs text-gray-600 mb-2 space-y-1">
                <div v-if="node.range">
                  <span class="font-medium">Range:</span> {{ node.range }}
                </div>
                <div v-if="node.context">
                  <span class="font-medium">Context:</span> {{ node.context }}
                </div>
              </div>

              <!-- deviation summary for THIS line -->
              <div class="text-sm space-y-1">
                <template v-for="devType in deviationTypes" :key="devType">
                  <div v-if="getNodeDeviation(node.id, devType).length > 0">
                    <span class="font-semibold">{{ devType }}:</span>
                    {{ getNodeDeviation(node.id, devType).join(", ") }}
                  </div>
                </template>
              </div>
            </div>
          </template>

          <!-- Footer buttons -->
          <div class="mt-4 flex justify-end gap-3">
            <button
              type="button"
              class="px-4 py-2 rounded-lg border border-gray-300 text-gray-700 hover:bg-gray-50 transition"
              @click="closePreview"
            >
              Close
            </button>
            <button
              type="button"
              class="px-4 py-2 rounded-lg bg-black text-white hover:bg-gray-800 transition"
              @click="
                () => {
                  closePreview();
                  handleNextClick();
                }
              "
            >
              Confirm &amp; Next
            </button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
