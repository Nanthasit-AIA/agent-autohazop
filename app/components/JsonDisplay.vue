<script setup lang="ts">
import { ref, computed, watch } from "vue";
import PipelineGraph from "~/components/PipelineGraph.vue";

type SectionId =
  | "process_description"
  | "intention"
  | "system_input"
  | "system_inputs"
  | "system_outputs"
  | "equipment"
  | "valves"
  | "instruments"
  | "utility_lines"
  | "connections"
  | "line_level_connections"
  | "metadata"
  | "raw_json";

interface SectionConfig {
  id: SectionId;
  key: string;
  label: string;
}

const props = defineProps<{
  data: any;
  isLoading?: boolean;
  fileName?: string;
}>();

const sectionConfigs: SectionConfig[] = [
  { id: "process_description", key: "process_description", label: "Process Description" },
  { id: "intention", key: "intention", label: "Design Intention" },
  { id: "system_input", key: "system_input", label: "System Input" },
  { id: "system_inputs", key: "system_inputs", label: "System Inputs" },
  { id: "system_outputs", key: "system_outputs", label: "System Outputs" },
  { id: "equipment", key: "equipment", label: "Equipment" },
  { id: "valves", key: "valves", label: "Valves" },
  { id: "instruments", key: "instruments", label: "Instruments" },
  { id: "utility_lines", key: "utility_lines", label: "Utility Lines" },
  { id: "connections", key: "connections", label: "Node Connections" },
  { id: "line_level_connections", key: "line_level_connections", label: "Line-Level Connections" },
  { id: "metadata", key: "metadata", label: "Metadata" },
  { id: "raw_json", key: "raw_json", label: "Raw JSON" },
];

/* -------- Root PID + metadata -------- */

const unwrapPidRoot = (data: any): any | null => {
  if (!data || typeof data !== "object") return null;

  const choicesParsed = data?.choices?.[0]?.message?.parsed;
  if (choicesParsed && typeof choicesParsed === "object") return choicesParsed;

  if (data.pid_data && typeof data.pid_data === "object") return data.pid_data;
  if (data.parsed && typeof data.parsed === "object") return data.parsed;

  return data;
};

const pidRoot = computed<any | null>(() => unwrapPidRoot(props.data));

const metadata = computed<any | null>(() => {
  const d = props.data;
  if (!d || typeof d !== "object") return null;
  return (d as any).metadata ?? null;
});

const sourceFormat = computed(() => {
  const d = props.data;
  if (!d || typeof d !== "object") return "empty";
  if (d?.choices?.[0]?.message?.parsed) return "OpenAI parsed response";
  if (d.pid_data) return "wrapped pid_data";
  if (d.parsed) return "wrapped parsed";
  return "direct topology JSON";
});

const totalTokens = computed<number | null>(() => {
  const m = metadata.value;
  if (!m || !m.tokens) return null;
  const t = m.tokens.total;
  return typeof t === "number" ? t : null;
});

const latencySeconds = computed<number | null>(() => {
  const m = metadata.value;
  if (!m) return null;
  const lat = m.latency_s;
  return typeof lat === "number" ? lat : null;
});

const rootCounts = computed(() => {
  const root = pidRoot.value;
  if (!root || typeof root !== "object") {
    return { equipment: 0, valves: 0, instruments: 0, utility_lines: 0, connections: 0, line_level_connections: 0 };
  }
  return {
    equipment: Array.isArray(root.equipment) ? root.equipment.length : 0,
    valves: Array.isArray(root.valves) ? root.valves.length : 0,
    instruments: Array.isArray(root.instruments) ? root.instruments.length : 0,
    utility_lines: Array.isArray(root.utility_lines) ? root.utility_lines.length : 0,
    connections: Array.isArray(root.connections) ? root.connections.length : 0,
    line_level_connections: Array.isArray(root.line_level_connections) ? root.line_level_connections.length : 0,
  };
});

/* -------- process_description as User Input -------- */

const processDescription = computed(() => {
  const root = pidRoot.value;
  if (!root || typeof root !== "object") return "";
  const val = (root as any).process_description;
  if (val == null) return "";
  return String(val);
});

const hasProcessDescription = computed(
  () => processDescription.value.trim().length > 0
);

/* -------- sections (except process_description) -------- */

const availableSections = computed(() => {
  const root = pidRoot.value;
  if (!root || typeof root !== "object") return [];

  return sectionConfigs.filter((sec) => {
    if (sec.id === "process_description") return false;
    if (sec.id === "metadata") return metadata.value != null;
    if (sec.id === "raw_json") return props.data != null;
    return sec.key in root && (root as any)[sec.key] !== undefined;
  });
});

const currentSectionId = ref<SectionId | null>(null);

watch(
  availableSections,
  (secs) => {
    if (!secs.length) {
      currentSectionId.value = null;
      return;
    }
    const first = secs[0];
    if (
      !currentSectionId.value ||
      !secs.some((s) => s.id === currentSectionId.value)
    ) {
      if (first) currentSectionId.value = first.id;
    }
  },
  { immediate: true }
);

const currentSection = computed(
  () =>
    availableSections.value.find((s) => s.id === currentSectionId.value) ?? null
);

const currentIndex = computed(() => {
  const id = currentSection.value?.id;
  if (!id) return -1;
  return availableSections.value.findIndex((s) => s.id === id);
});

const sectionData = computed(() => {
  const root = pidRoot.value;
  if (!currentSection.value || !root) return null;

  if (currentSection.value.id === "metadata") return metadata.value;
  if (currentSection.value.id === "raw_json") return props.data;

  return (root as any)[currentSection.value.key];
});

const isPrimitiveSection = computed(() => {
  const val = sectionData.value;
  const t = typeof val;
  return val == null || t === "string" || t === "number" || t === "boolean";
});

const isArrayOfObjects = computed(() => {
  return (
    Array.isArray(sectionData.value) &&
    sectionData.value.length > 0 &&
    typeof sectionData.value[0] === "object"
  );
});

const currentCount = computed(() => {
  const val = sectionData.value;

  if (Array.isArray(val)) return val.length;
  if (val && typeof val === "object") return Object.keys(val).length;
  if (val === null || val === undefined) return 0;
  return 1;
});

const prettySectionJson = computed(() =>
  sectionData.value != null ? JSON.stringify(sectionData.value, null, 2) : ""
);

const fieldOrderBySection: Partial<Record<SectionId, string[]>> = {
  equipment: ["id", "name", "type", "context"],
  valves: ["id", "type", "location", "context"],
  instruments: ["id", "function", "location", "context"],
  utility_lines: ["utility_type", "valves", "flow_direction", "context"],
  connections: [
    "line_id",
    "node",
    "node_boundary",
    "from_id",
    "to_id",
    "included_equipment",
    "included_lines",
    "valves",
    "instruments",
    "flow_direction",
    "context",
  ],
  line_level_connections: [
    "line_id",
    "from_id",
    "to_id",
    "valves",
    "instruments",
    "flow_direction",
    "context",
  ],
};

const getSortedEntries = (
  item: Record<string, unknown>,
  sectionId: SectionId | null
) => {
  const keys = Object.keys(item);
  const preferred = sectionId ? (fieldOrderBySection[sectionId] ?? []) : [];

  return keys
    .slice()
    .sort((a, b) => {
      const aIndex = preferred.indexOf(a);
      const bIndex = preferred.indexOf(b);
      const aPreferred = aIndex !== -1;
      const bPreferred = bIndex !== -1;

      if (aPreferred && bPreferred) return aIndex - bIndex;
      if (aPreferred) return -1;
      if (bPreferred) return 1;

      return a.localeCompare(b);
    })
    .map((key) => ({
      key,
      value: (item as any)[key],
    }));
};


const formatCellValue = (value: unknown): string => {
  if (value === null || value === undefined || value === "") return "—";
  if (typeof value === "string") return value;
  if (typeof value === "number" || typeof value === "boolean") return String(value);
  if (Array.isArray(value)) {
    return value
      .map((item) => {
        if (item && typeof item === "object") {
          return (item as any).id ?? (item as any).name ?? (item as any).type ?? JSON.stringify(item);
        }
        return String(item);
      })
      .join("; ");
  }
  if (typeof value === "object") return JSON.stringify(value, null, 2);
  return String(value);
};

const switchSection = (id: SectionId) => {
  currentSectionId.value = id;
};

const goPrev = () => {
  if (currentIndex.value <= 0) return;
  const prev = availableSections.value[currentIndex.value - 1];
  if (!prev) return;
  currentSectionId.value = prev.id;
};

const goNext = () => {
  if (
    currentIndex.value < 0 ||
    currentIndex.value >= availableSections.value.length - 1
  )
    return;
  const next = availableSections.value[currentIndex.value + 1];
  if (!next) return;
  currentSectionId.value = next.id;
};

/* -------- graph preview modal -------- */

const showGraph = ref(false);

const hasConnections = computed(() => {
  const root = pidRoot.value;
  if (!root || typeof root !== "object") return false;
  const conns = (root as any).connections;
  const lineConns = (root as any).line_level_connections;
  return (Array.isArray(conns) && conns.length > 0) ||
    (Array.isArray(lineConns) && lineConns.length > 0);
});

const openGraph = () => {
  if (hasConnections.value) showGraph.value = true;
};
const closeGraph = () => {
  showGraph.value = false;
};
</script>

<template>
  <div class="bg-white rounded-2xl p-6 shadow-lg w-full max-w-6xl mx-auto">
    <!-- Header: file + tokens/latency -->
    <div v-if="fileName || totalTokens !== null || latencySeconds !== null"
      class="mb-3 flex flex-col gap-1 md:flex-row md:items-center md:justify-between">
      <div v-if="fileName" class="text-sm text-gray-800 font-black">
        File:
        <span class="font-medium text-gray-700">{{ fileName }}</span>
      </div>

      <div v-if="totalTokens !== null || latencySeconds !== null"
        class="text-xs text-gray-500 flex flex-wrap gap-3 md:justify-end">
        <span v-if="totalTokens !== null">
          Tokens:
          <span class="font-medium text-gray-700 ">{{ totalTokens }}</span>
        </span>
        <span v-if="latencySeconds !== null">
          Latency:
          <span class="font-medium text-gray-700">
            {{ latencySeconds.toFixed(1) }} s
          </span>
        </span>
      </div>
    </div>

    <div v-if="pidRoot" class="mb-4 grid grid-cols-2 gap-2 md:grid-cols-6">
      <div class="rounded-xl bg-slate-50 border border-slate-200 p-2 text-xs">
        <div class="font-black text-gray-500">Format</div>
        <div class="text-gray-800 wrap-break-word">{{ sourceFormat }}</div>
      </div>
      <div class="rounded-xl bg-slate-50 border border-slate-200 p-2 text-xs">
        <div class="font-black text-gray-500">Equipment</div>
        <div class="text-gray-800">{{ rootCounts.equipment }}</div>
      </div>
      <div class="rounded-xl bg-slate-50 border border-slate-200 p-2 text-xs">
        <div class="font-black text-gray-500">Valves</div>
        <div class="text-gray-800">{{ rootCounts.valves }}</div>
      </div>
      <div class="rounded-xl bg-slate-50 border border-slate-200 p-2 text-xs">
        <div class="font-black text-gray-500">Instruments</div>
        <div class="text-gray-800">{{ rootCounts.instruments }}</div>
      </div>
      <div class="rounded-xl bg-slate-50 border border-slate-200 p-2 text-xs">
        <div class="font-black text-gray-500">Nodes</div>
        <div class="text-gray-800">{{ rootCounts.connections }}</div>
      </div>
      <div class="rounded-xl bg-slate-50 border border-slate-200 p-2 text-xs">
        <div class="font-black text-gray-500">Line-level</div>
        <div class="text-gray-800">{{ rootCounts.line_level_connections }}</div>
      </div>
    </div>

    <!-- User Input: process_description -->
    <div v-if="hasProcessDescription" class="mb-6">
      <span class="text-xl font-black text-gray-700 ml-3">Input Description</span>
      <div class="border border-gray-200 rounded-2xl p-4 bg-slate-50 mt-2">
        <p class="text-sm text-gray-800 whitespace-pre-line">
          {{ processDescription }}
        </p>
      </div>
    </div>

    <!-- Loading -->
    <div v-if="isLoading" class="text-sm text-gray-500">Loading JSON…</div>

    <!-- No data -->
    <div v-else-if="!pidRoot || !availableSections.length" class="text-sm text-gray-500">
      No structured output sections found in JSON data.
    </div>

    <!-- Output sections -->
    <div v-else>
      <!-- Output header: section buttons -->
      <div
        class="flex flex-col gap-3 md:flex-row md:items-center md:justify-between mb-2 py-2 border-b border-gray-200">
        <h3 class="text-xl font-black text-gray-700 ml-3">Process Output Sections</h3>

        <div v-if="availableSections.length" class="flex flex-wrap gap-2">
          <button v-for="sec in availableSections" :key="sec.id"
            class="px-3 py-1.5 rounded-lg text-xs font-medium border transition" :class="sec.id === currentSectionId
                ? 'bg-black text-white border-black'
                : 'bg-gray-100 text-gray-700 border-gray-300 hover:bg-gray-200'
              " @click="switchSection(sec.id)">
            {{ sec.label }}
          </button>
        </div>
      </div>

      <!-- Section header (current section info + graph button) -->
      <div class="flex items-center justify-between mb-2 mt-3">
        <div class="flex items-center gap-2">
          <h2 class="text-lg font-black text-gray-600 ml-3">
            {{ currentSection?.label }}
          </h2>

          <span v-if="currentCount > 1"
            class="inline-flex items-center justify-center px-2 py-0.5 text-sm font-semibold rounded-full bg-gray-200 text-gray-700">
            {{ currentCount }}
          </span>
        </div>

        <div class="flex items-center gap-3">
          <span class="text-xs text-gray-500">
            Section {{ currentIndex + 1 }} / {{ availableSections.length }}
          </span>

          <button v-if="hasConnections" type="button"
            class="px-3 py-1.5 rounded-lg text-xs font-medium border border-gray-300 bg-white hover:bg-gray-50 transition"
            @click="openGraph">
            Preview graph
          </button>
        </div>
      </div>

      <!-- Content box -->
      <div class="border border-gray-200 rounded-2xl p-4 bg-slate-50">
        <!-- simple string / number / boolean -->
        <p v-if="isPrimitiveSection" class="text-sm text-gray-800 whitespace-pre-line">
          {{ sectionData }}
        </p>

        <!-- array of objects: show cards -->
        <div v-else-if="isArrayOfObjects" class="grid gap-3 md:grid-cols-2">
          <div v-for="(item, idx) in sectionData" :key="idx"
            class="bg-white rounded-lg border border-gray-200 p-3 text-xs text-gray-800">
            <div v-for="entry in getSortedEntries(
              item as Record<string, unknown>,
              currentSection?.id ?? null
            )" :key="entry.key" class="flex justify-between gap-2">
              <span class="text-gray-500">{{ entry.key }}</span>
              <span class="font-medium wrap-break-word whitespace-pre-line text-right">{{ formatCellValue(entry.value) }}</span>
            </div>
          </div>
        </div>

        <!-- fallback: pretty JSON -->
        <pre v-else class="text-xs text-gray-800 whitespace-pre overflow-x-auto">{{ prettySectionJson }}
        </pre>
      </div>

      <!-- Navigation buttons -->
      <div v-if="availableSections.length > 1" class="flex items-center justify-between mt-4 text-xs">
        <button
          class="px-3 py-1.5 rounded-lg border border-gray-300 text-gray-700 disabled:opacity-40 disabled:cursor-not-allowed"
          :disabled="currentIndex <= 0" @click="goPrev">
          ← Previous
        </button>

        <div class="text-gray-500">
          Use the buttons above to jump to any output section.
        </div>

        <button
          class="px-3 py-1.5 rounded-lg border border-gray-300 text-gray-700 disabled:opacity-40 disabled:cursor-not-allowed"
          :disabled="currentIndex >= availableSections.length - 1" @click="goNext">
          Next →
        </button>
      </div>
    </div>

    <!-- 🔍 Graph modal -->
    <transition name="fade">
      <div v-if="showGraph" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40"
        @click.self="closeGraph">
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-5xl max-h-[80vh] p-4 overflow-hidden">
          <div class="flex items-center justify-between mb-3">
            <h3 class="text-sm font-semibold text-gray-800">
              Connection graph
            </h3>
            <button type="button"
              class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center hover:bg-gray-200 transition"
              @click="closeGraph">
              <span class="text-sm font-bold text-gray-600">×</span>
            </button>
          </div>

          <div class="border rounded-xl overflow-hidden bg-white">
            <!-- pidRoot is computed; template auto-unwraps -->
            <PipelineGraph v-if="pidRoot" :data="pidRoot" />
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
