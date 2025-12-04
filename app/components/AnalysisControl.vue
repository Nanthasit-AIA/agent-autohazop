<script setup lang="ts">
import { computed, toRefs, withDefaults, ref } from "vue";

interface HazopRun {
  line_id: string;
  parameter: string;
  guide_word: string;
  tokens_used?: number;
}

const props = withDefaults(
  defineProps<{
    active?: boolean;
    label?: string;
    errorMessage?: string;
    runs?: HazopRun[];
    outputFolder?: string;
    fileName?: string;
    processInputs?: string[];
    processOutputs?: string[];
  }>(),
  {
    active: false,
    label: "waiting to analysis",
    runs: () => [],
    processInputs: () => [],
    processOutputs: () => [],
  }
);

const emit = defineEmits<{
  (e: "start"): void;
  (e: "exit"): void;
}>();

const {
  active,
  label,
  errorMessage,
  runs,
  outputFolder,
  fileName,
  processInputs,
  processOutputs,
} = toRefs(props);

const indicatorClass = computed(() => {
  if (errorMessage.value) return "bg-red-500";
  if (active.value) return "bg-blue-400 animate-pulse";
  if (label.value && label.value.toLowerCase().includes("complete")) {
    return "bg-green-400";
  }
  return "bg-gray-300";
});

const showSpinner = computed(() => active.value);
const hasRuns = computed(() => (runs.value?.length ?? 0) > 0);

const fullPath = computed(() => {
  if (!outputFolder.value && !fileName.value) return "";
  if (!outputFolder.value) return fileName.value;
  if (!fileName.value) return outputFolder.value;
  return `${outputFolder.value}/${fileName.value}`;
});

// ---- Output analysis table example modal ----
const showOutputExampleModal = ref(false);

const outputTableHeaders = [
  "Node",
  "Guide word",
  "Parameter",
  "Deviation",
  "Cause",
  "Consequence",
  "Unmitigated risk category",
  "S before safeguard",
  "L before safeguard",
  "RR before safeguard",
  "Overall risk before safeguard",
  "Safeguard",
  "Mitigated risk category",
  "S after safeguard",
  "L after safeguard",
  "RR after safeguard",
  "Overall risk after safeguard",
  "Recommendations",
  "S after recommendations",
  "L after recommendations",
  "RR after recommendations",
  "Responsibility",
];

const outputExampleRows: string[][] = [
  [
    "D60-Storage → D60-Heater",
    "More",
    "Flow",
    "More flow",
    "Control valve FV-101 stuck open",
    "Heater overpressure and tube rupture",
    "High",
    "4",
    "4",
    "5",
    "5",
    "High-high pressure trip + PSV to flare",
    "Medium",
    "3",
    "3",
    "4",
    "4",
    "Install flow-limiting orifice; improve alarm response procedure",
    "2",
    "3",
    "3",
    "Process engineer / Operations supervisor",
  ],
];

// ---- system hazard preview modal ----
const showHazardModal = ref(false);

const openHazardModal = () => {
  showHazardModal.value = true;
};

const closeHazardModal = () => {
  showHazardModal.value = false;
};

// ---------------- Risk matrix modal ----------------
const showRiskMatrixModal = ref(false);
const showRiskSummary = ref(true);

interface LikelihoodCol {
  value: number;
  label: string;
  desc: string;
}
interface SeverityRow {
  value: number;
  desc: string;
  scores: number[]; // 5→1 likelihood order
}

const likelihoodCols: LikelihoodCol[] = [
  { value: 5, label: "5", desc: "Often" },
  { value: 4, label: "4", desc: "Likely" },
  { value: 3, label: "3", desc: "Unlikely" },
  { value: 2, label: "2", desc: "Very unlikely" },
  { value: 1, label: "1", desc: "Extremely unlikely" },
];

const severityRows: SeverityRow[] = [
  {
    value: 5,
    desc: "Major accident disaster / affect operation",
    scores: [5, 5, 4, 3, 2],
  },
  {
    value: 4,
    desc: "Serious injury / equipment damage",
    scores: [5, 4, 4, 3, 2],
  },
  {
    value: 3,
    desc: "Medical treatment impact and activities / equipment failure",
    scores: [4, 4, 3, 3, 2],
  },
  {
    value: 2,
    desc: "Medical treatment / abnormal equipment",
    scores: [3, 3, 3, 2, 1],
  },
  {
    value: 1,
    desc: "Minor injury / equipment does not affect",
    scores: [2, 2, 2, 1, 1],
  },
];

// simple color map by score
const riskCellClass = (score: number) => {
  if (score >= 5) return "bg-red-500 text-white";
  if (score === 4) return "bg-orange-400 text-white";
  if (score === 3) return "bg-yellow-300 text-gray-900";
  if (score === 2) return "bg-green-400 text-white";
  return "bg-emerald-500 text-white";
};

const riskLevels = [
  {
    level: 1,
    degree: "Acceptable risk",
    color: "bg-emerald-100 text-emerald-800",
  },
  {
    level: 2,
    degree: "Acceptable risk",
    color: "bg-emerald-100 text-emerald-800",
  },
  {
    level: 3,
    degree: "Significant risk and needs to be improved",
    color: "bg-yellow-100 text-yellow-800",
  },
  {
    level: 4,
    degree: "Significant risk and needs to be improved",
    color: "bg-orange-100 text-orange-800",
  },
  {
    level: 5,
    degree: "Significant risk and needs to be improved",
    color: "bg-red-100 text-red-800",
  },
];
</script>

<template>
  <div class="space-y-6 mb-20">
    <div class="flex justify-start px-5 mb-5">
      <!-- system hazard preview button -->
      <button type="button"
        class="inline-flex items-center gap-2 px-3 py-1.5 rounded-lg border border-amber-200 bg-amber-50 text-sm font-black text-amber-900 hover:bg-amber-100 transition"
        @click="openHazardModal">
        <i class="fi fi-br-triangle-warning text-md flex items-center justify-center"/>
        <span> System Hazards : preview</span>
      </button>
      <button type="button" @click="showRiskMatrixModal = true"
        class=" ml-5 gap-2 px-4 py-1.5 bg-sky-100 text-sky-700 border border-sky-300 rounded-lg text-sm font-black hover:bg-sky-200 transition flex items-center gap-1">
        <i class="fi fi-br-chart-simple text-md flex items-center justify-center"/>
        <span>Risk Matrix : preview</span>
      </button>
      <button type="button" @click="showOutputExampleModal = true"
        class="flex gap-2 ml-5 px-4 py-1.5 bg-green-100 text-green-700 border border-green-300 rounded-lg text-sm font-black hover:bg-green-200 transition items-center gap-1">
        <i class="fi fi-br-stats text-lg flex items-center justify-center" />
        <span>Output HAZOP Table : preview</span>
      </button>
    </div>
    <!-- status row -->
    <div class="flex items-center gap-3 px-5 py-4">
      <!-- indicator + spinner -->
      <div class="relative">
        <div class="w-4 h-4 rounded-full" :class="indicatorClass"></div>

        <!-- spinner overlay when loading -->
        <div v-if="showSpinner"
          class="absolute -top-1 -left-1 w-6 h-6 border-2 border-gray-300 border-t-black rounded-full animate-spin">
        </div>
      </div>

      <!-- text -->
      <span class="text-gray-700 font-medium">
        {{ errorMessage || label || "waiting to analysis" }}
      </span>
    </div>

    <!-- error message (explicit block as well, in case you want styling) -->
    <div v-if="errorMessage" class="px-5 text-sm text-red-600">
      {{ errorMessage }}
    </div>

    <!-- runs table -->
    <div v-if="hasRuns" class="bg-white rounded-2xl shadow-sm border border-gray-200 p-4 mx-5">
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
            <tr v-for="(run, idx) in runs" :key="`${run.line_id}-${run.parameter}-${run.guide_word}-${idx}`"
              class="border-b border-gray-100 last:border-0">
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
                {{ run.tokens_used ?? "–" }}
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

    <!-- start / exit buttons -->
    <div class="flex gap-3 justify-center mb-8">
      <button @click="emit('start')"
        class="px-8 py-3 bg-black text-white rounded-lg hover:bg-gray-800 transition text-lg font-medium"
        :disabled="active" :class="active ? 'opacity-60 cursor-not-allowed' : ''">
        Start analysis
      </button>

      <button @click="emit('exit')"
        class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition">
        exit
      </button>
    </div>

    <!-- ================== SYSTEM HAZARD MODAL ================== -->
    <transition name="fade-overlay">
      <div v-if="showHazardModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
        <div class="relative bg-white rounded-3xl shadow-2xl max-w-5xl w-full mx-4 p-6 md:p-8">
          <!-- close button -->
          <button type="button"
            class="absolute top-4 right-4 w-8 h-8 rounded-full border border-gray-200 flex items-center justify-center text-gray-500 hover:bg-gray-100"
            @click="closeHazardModal">
            ✕
          </button>

          <!-- title -->
          <div class="flex items-center gap-3 border-b border-gray-100 py-2">
            <div class="w-10 h-10 rounded-xl bg-amber-100 text-amber-700 flex items-center justify-center text-2xl">
              <i class="fi fi-br-triangle-warning text-lg flex items-center justify-center"/>
            </div>
            <div>
              <h2 class="text-2xl text-gray-900 font-black">
                Chemical / Material Hazards Analysis
              </h2>
              <p class="text-xs text-gray-500">
                Identifies substance-related hazards and evaluates their potential consequences
              </p>
            </div>
          </div>
          <h2 class="text-xl md:text-2xl font-bold text-gray-900 mb-4">

          </h2>

          <div class="flex flex-col md:flex-row gap-8">
            <!-- LEFT: process inputs / outputs -->
            <div class="md:w-2/5 space-y-4">
              <div class="rounded-2xl border border-gray-200 bg-gray-100 px-4 py-3">
                <div class="text-xs font-semibold text-gray-600 uppercase tracking-wide">
                  System hazards analysis
                </div>
              </div>

              <!-- Inputs -->
              <div class="rounded-2xl bg-lime-200/60 p-3 space-y-3">
                <div class="rounded-xl bg-white px-4 py-3">
                  <div class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1">
                    Input substances
                  </div>
                  <ul class="text-sm text-gray-900 space-y-0.5">
                    <li v-if="!processInputs || processInputs.length === 0" class="italic text-gray-400">
                      No inputs detected from JSON
                    </li>
                    <li v-for="(inp, idx) in processInputs" :key="`in-${idx}-${inp}`">
                      • {{ inp }}
                    </li>
                  </ul>
                </div>

                <!-- Outputs -->
                <div class="rounded-xl bg-white px-4 py-3">
                  <div class="text-xs font-semibold text-gray-500 uppercase tracking-wide mb-1">
                    Output substances
                  </div>
                  <ul class="text-sm text-gray-900 space-y-0.5">
                    <li v-if="!processOutputs || processOutputs.length === 0" class="italic text-gray-400">
                      No outputs detected from JSON
                    </li>
                    <li v-for="(out, idx) in processOutputs" :key="`out-${idx}-${out}`">
                      • {{ out }}
                    </li>
                  </ul>
                </div>
              </div>
            </div>

            <!-- RIGHT: hazard tiles with emoji -->
            <div class="md:flex-1 grid sm:grid-cols-2 gap-3 ">
              <div class="rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-flask-poison text-md flex items-center justify-center" />
                <span>Personnel poisoning</span>
              </div>

              <div class="rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-flask text-md flex items-center justify-center" />
                <span>Corrosion</span>
              </div>

              <div class="rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-volcano text-md flex items-center justify-center" />
                <span>Explosion</span>
              </div>

              <div class="rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-bolt text-md flex items-center justify-center" />
                <span>Runaway reaction</span>
              </div>

              <div class="rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-fire-flame-curved text-md flex items-center justify-center" />
                <span>Fire</span>
              </div>

              <div class="rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-wind text-md flex items-center justify-center" />
                <span>Asphyxiation</span>
              </div>

              <div
                class="sm:col-span-2 rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-engine-warning text-md flex items-center justify-center" />
                <span>Process equipment damage / failure</span>
              </div>

              <div
                class="sm:col-span-2 rounded-xl bg-amber-50 px-4 py-3 text-sm font-semibold text-gray-900 flex items-center gap-2">
                <i class="fi fi-br-smog text-md flex items-center justify-center" />
                <span>Environmental pollution (air / water / soil)</span>
              </div>
            </div>
          </div>

          <!-- footer -->
          <div class="mt-6 flex justify-end border-t border-gray-100 py-2">
            <button type="button"
              class="px-4 py-2 rounded-lg border border-gray-300 text-sm text-gray-700 hover:bg-gray-50 transition"
              @click="closeHazardModal">
              Close
            </button>
          </div>
        </div>
      </div>
    </transition>
    <!-- =============== Risk MATRIX MODAL =============== -->
    <transition name="fade-overlay">
      <div v-if="showRiskMatrixModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
        <div class="relative bg-white rounded-3xl shadow-2xl max-w-5xl w-full mx-4 p-6 md:p-6">
          <!-- header -->
          <div class="flex items-center justify-between px-6 py-4 border-b border-gray-100">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-sky-100 text-sky-700 flex items-center justify-center text-2xl">
                <i class="fi fi-br-chart-simple text-lg flex items-center justify-center"/>
              </div>
              <div>
                <h2 class="text-2xl text-gray-900 font-black">
                  Risk Assessment Matrix
                </h2>
                <p class="text-xs text-gray-500">
                  Severity × Likelihood → Risk level for each scenario.
                </p>
              </div>
            </div>

            <button type="button"
              class="w-8 h-8 rounded-full border border-gray-200 flex items-center justify-center text-gray-500 hover:bg-gray-100"
              @click="showRiskMatrixModal = false">
              ✕
            </button>
          </div>

          <!-- body -->
          <div class="flex flex-1 overflow-hidden bg-white">
            <!-- matrix left -->
            <div class="flex-1 overflow-auto p-6 px-20">
              <div class="mb-4">
                <div class="rounded-2xl border border-gray-200 bg-gray-100 px-4 py-3 w-60 mb-3">
                  <div class="text-xs font-semibold text-gray-600 uppercase tracking-wide">
                    Risk Level Table
                  </div>
                </div>
                <p class="text-xs text-gray-500 ml-4">
                  Use this table as a visual guide when assigning risk levels to each
                  HAZOP deviation.
                </p>
              </div>

              <div class="inline-block border border-gray-200 rounded-xl bg-white">
                <table class="text-xs">
                  <thead>
                    <tr>
                      <th class="bg-orange-100 text-gray-900 px-3 py-2 align-bottom" rowspan="2">
                        Severity
                      </th>
                      <th class="bg-orange-100 text-gray-900 px-8 py-1 text-center border-l border-gray-200"
                        :colspan="likelihoodCols.length">
                        Likelihood
                      </th>
                    </tr>
                    <tr>
                      <th v-for="col in likelihoodCols" :key="col.value"
                        class="bg-orange-50 border-l border-gray-200 px-3 py-1 text-center">
                        <div class="font-semibold">{{ col.value }}</div>
                        <div class="text-[10px] text-gray-600">
                          {{ col.desc }}
                        </div>
                      </th>
                    </tr>
                  </thead>

                  <tbody>
                    <tr v-for="row in severityRows" :key="row.value" class="border-t border-gray-200">
                      <!-- severity description -->
                      <td class="bg-orange-50 px-3 py-2 align-top w-56">
                        <div class="font-semibold text-gray-900 mb-0.5">
                          {{ row.value }}
                        </div>
                        <div class="text-[11px] text-gray-700 leading-snug">
                          {{ row.desc }}
                        </div>
                      </td>

                      <!-- risk scores -->
                      <td v-for="(score, idx) in row.scores" :key="idx"
                        class="w-16 h-14 border-l border-gray-200 text-center align-middle">
                        <div class="mx-auto w-10 h-10 rounded-md flex items-center justify-center text-sm font-semibold"
                          :class="riskCellClass(score)">
                          {{ score }}
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </div>

            <!-- summary right -->
            <div class="w-72 border-l border-gray-100 bg-white flex flex-col">
              <button type="button"
                class="flex items-center justify-between px-4 py-3 border-b border-gray-100 text-xs font-semibold text-gray-800 bg-amber-50"
                @click="showRiskSummary = !showRiskSummary">
                <span>Risk level summary</span>
                <span class="transition-transform" :class="showRiskSummary ? 'rotate-180' : ''">
                  ▼
                </span>
              </button>

              <div v-if="showRiskSummary" class="flex-1 overflow-auto px-4 py-3 space-y-2 text-xs">
                <div v-for="item in riskLevels" :key="item.level" class="rounded-lg border border-gray-200 p-2">
                  <div class="flex items-center justify-between mb-1">
                    <div
                      class="inline-flex items-center justify-center px-2 py-0.5 rounded-full text-[11px] font-semibold"
                      :class="item.color">
                      Risk level {{ item.level }}
                    </div>
                  </div>
                  <p class="text-[11px] text-gray-700 leading-snug">
                    {{ item.degree }}
                  </p>
                </div>
              </div>
            </div>
          </div>

          <!-- footer -->
          <div class="px-6 py-3 border-t border-gray-100 bg-white flex justify-end">
            <button type="button"
              class="px-4 py-2 rounded-lg border border-gray-300 text-sm text-gray-700 hover:bg-gray-50"
              @click="showRiskMatrixModal = false">
              Close
            </button>
          </div>
        </div>
      </div>
    </transition>
    <!-- =============== OUTPUT ANALYSIS TABLE EXAMPLE MODAL =============== -->
    <transition name="fade-overlay">
      <div v-if="showOutputExampleModal" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
        <div class="relative bg-white rounded-3xl shadow-2xl max-w-369 w-full mx-4 p-6 md:p-6">
          <!-- header -->
          <div class="flex items-center justify-between px-6 py-4 border-b border-gray-100">
            <div class="flex items-center gap-3">
              <div class="w-10 h-10 rounded-xl bg-green-100 text-green-700 flex items-center justify-center text-2xl">
                <i class="fi fi-br-stats text-lg flex items-center justify-center" />
              </div>
              <div>
                <h2 class="text-2xl text-gray-900 font-black">
                  Output HAZOP Analysis Table : example
                </h2>
                <p class="text-xs text-gray-500">
                  Example of HAZOP deviation row showing risk before and after
                  safeguards and recommendations
                </p>
              </div>
            </div>

            <button type="button"
              class="w-8 h-8 rounded-full border border-gray-200 flex items-center justify-center text-gray-500 hover:bg-gray-100"
              @click="showOutputExampleModal = false">
              ✕
            </button>
          </div>

          <!-- body -->
          <div class="flex-1 overflow-auto p-6">
            <div class="rounded-2xl border border-gray-200 bg-yellow-50 px-4 py-3 mb-4 inline-block">
              <div class="text-xs font-semibold text-gray-600 uppercase tracking-wide">
                Header Table for HAZOP analysis
              </div>
            </div>

            <div class="overflow-x-auto">
              <table class="min-w-max text-xs text-left border border-gray-100 rounded-xl bg-white">
                <thead>
                  <tr class="bg-yellow-50 border-b border-gray-100">
                    <th v-for="head in outputTableHeaders" :key="head"
                      class="px-3 py-5 align-top text-[11px] text-gray-800 border-r last:border-r-0 border-gray-200 whitespace-normal wrap-break-word max-w-[126px]">
                      {{ head }}
                    </th>
                  </tr>
                </thead>

                <tbody>
                  <tr v-for="(row, rIdx) in outputExampleRows" :key="rIdx" class="border-t border-gray-200">
                    <td v-for="(cell, cIdx) in row" :key="cIdx"
                      class="px-3 py-5 align-top text-[11px] text-gray-800 border-r last:border-r-0 border-gray-200 whitespace-normal wrap-break-word max-w-[126px]">
                      {{ cell }}
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- footer -->
          <div class="px-6 py-3 border-t border-gray-100 bg-white flex justify-end">
            <button type="button"
              class="px-4 py-2 rounded-lg border border-gray-300 text-sm text-gray-700 hover:bg-gray-50"
              @click="showOutputExampleModal = false">
              Close
            </button>
          </div>
        </div>
      </div>
    </transition>
  </div>
</template>

<style scoped>
.fade-overlay-enter-active,
.fade-overlay-leave-active {
  transition: opacity 0.7s ease;
}

.fade-overlay-enter-from,
.fade-overlay-leave-to {
  opacity: 0;
  transform: translateY(12px);
}
</style>
