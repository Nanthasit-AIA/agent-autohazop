<script setup lang="ts">
import { computed, ref } from "vue";

//
// ---------- Types ----------
//
type DeviationType =
  | "Flow"
  | "Pressure"
  | "Temperature"
  | "Level"
  | "Concentration"
  | "Composition";

type AdditionalParam =
  | "Phase"
  | "Utility"
  | "Power"
  | "Instrument"
  | "Human Action"
  | "Maintenance"
  | "Operation Timing";

type ParamName = DeviationType | AdditionalParam;
type GuideWord =
  | "No"
  | "More"
  | "Less"
  | "As well as"
  | "Part of"
  | "Reverse"
  | "Other than"
  | "Early"
  | "Late"
  | "Before"
  | "After"
  | "No/Low";

const deviationTypes: DeviationType[] = [
  "Flow",
  "Pressure",
  "Temperature",
  "Level",
  "Concentration",
  "Composition",
];

const additionalParams: AdditionalParam[] = [
  "Phase",
  "Utility",
  "Power",
  "Instrument",
  "Human Action",
  "Maintenance",
  "Operation Timing",
];

const allParams: ParamName[] = [...deviationTypes, ...additionalParams];

const validGuideWords: GuideWord[] = [
  "No",
  "More",
  "Less",
  "As well as",
  "Part of",
  "Reverse",
  "Other than",
  "Early",
  "Late",
  "Before",
  "After",
  "No/Low",
];

// base options for main 6 parameters
const deviationOptionsMap: Record<DeviationType, GuideWord[]> = {
  Flow: ["More", "Less", "No", "Reverse"],
  Pressure: ["More", "Less"],
  Temperature: ["More", "Less"],
  Level: ["More", "Less", "No"],
  Concentration: ["More", "Less"],
  Composition: ["Other than"],
};

const extraGuideWordsFor = (devType: DeviationType): GuideWord[] => {
  const base = deviationOptionsMap[devType];
  return validGuideWords.filter((gw) => !base.includes(gw));
};

interface PreviewNode {
  id: string | number;
  name: string;
  range?: string;
  context?: string;
}

const props = defineProps<{
  // v-model for CURRENT node (per-page): includes BOTH main + additional params
  modelValue: Record<ParamName, GuideWord[]>;

  currentNode?: number;
  totalNodes?: number;

  nodeTitle?: string;
  nodeLine?: string;
  nodeContext?: string;

  allNodes: PreviewNode[];
  allSelections: Record<string | number, Record<ParamName, GuideWord[]>>;

  analysisFileName?: string;
  outputFolder?: string;
}>();

const emit = defineEmits<{
  "update:modelValue": [Record<ParamName, GuideWord[]>];
  "update:currentNode": [number];
  "update:analysisFileName": [string];
  "update:outputFolder": [string];
  "update:allSelections": [
    Record<string | number, Record<ParamName, GuideWord[]>>,
  ];
  preview: [];
  next: [];
}>();

//
// ---------- v-model wrappers for analysis config ----------
//
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

//
// ---------- pagination ----------
//
type PageItem = number | "dots";

const currentNode = computed(() => props.currentNode ?? 1);
const totalNodes = computed(() => props.totalNodes ?? 1);

const pages = computed<PageItem[]>(() => {
  const total = totalNodes.value;
  const current = currentNode.value;

  if (total <= 0) return [];

  // show all if <= 6
  if (total <= 6) {
    return Array.from({ length: total }, (_, i) => i + 1);
  }

  const result: PageItem[] = [];
  const first = 1;
  const second = 2;
  result.push(first, second);

  const windowSize = 2;
  const minStart = 3;
  const maxStart = total - 2 - (windowSize - 1);

  let midStart = current;
  if (midStart < minStart) midStart = minStart;
  if (midStart > maxStart) midStart = maxStart;
  const midEnd = midStart + windowSize - 1;

  if (midStart > second + 1) {
    result.push("dots");
  }

  for (let p = midStart; p <= midEnd; p++) {
    if (p >= total - 1) break;
    result.push(p);
  }

  if (midEnd < total - 2) {
    result.push("dots");
  }

  result.push(total - 1, total);

  return result;
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

//
// ---------- selection helpers (generic: ALL params) ----------
//
const setSelections = (param: ParamName, options: GuideWord[]) => {
  emit("update:modelValue", {
    ...props.modelValue,
    [param]: options,
  });
};

const getSelectionsFor = (param: ParamName): GuideWord[] => {
  return props.modelValue[param] ?? [];
};

const hasSelectionsFor = (param: ParamName): boolean => {
  return getSelectionsFor(param).length > 0;
};

const isSelected = (param: ParamName, option: GuideWord) => {
  return getSelectionsFor(param).includes(option);
};

const toggleOption = (param: ParamName, option: GuideWord) => {
  const current = getSelectionsFor(param);
  const next = current.includes(option)
    ? current.filter((o) => o !== option)
    : [...current, option];
  setSelections(param, next);
};

// main "dot" toggle for base options only (6 params)
const toggleAllBaseForType = (devType: DeviationType) => {
  const base = deviationOptionsMap[devType];
  const current = getSelectionsFor(devType);
  const allSelected = base.every((o) => current.includes(o));

  const next = allSelected
    ? current.filter((o) => !base.includes(o)) // clear only base
    : Array.from(new Set([...current, ...base]));

  setSelections(devType, next);
};

// left column buttons: only main 6 params
const selectAllMainForCurrentNode = () => {
  const next: Record<ParamName, GuideWord[]> = { ...props.modelValue };
  deviationTypes.forEach((p) => {
    next[p] = [...deviationOptionsMap[p]];
  });
  emit("update:modelValue", next);
};

const clearAllMainForCurrentNode = () => {
  const next: Record<ParamName, GuideWord[]> = { ...props.modelValue };
  deviationTypes.forEach((p) => {
    next[p] = [];
  });
  emit("update:modelValue", next);
};

//
// ---------- extra guide word popover for main parameters ----------
//
const openExtraFor = ref<DeviationType | null>(null);

const toggleExtraPopover = (devType: DeviationType) => {
  openExtraFor.value = openExtraFor.value === devType ? null : devType;
};

const toggleExtraGuide = (devType: DeviationType, gw: GuideWord) => {
  const base = deviationOptionsMap[devType];
  const current = new Set(getSelectionsFor(devType));

  if (current.has(gw)) {
    current.delete(gw);
  } else {
    current.add(gw);
  }

  const next: GuideWord[] = [
    // keep base in base order
    ...base.filter((b) => current.has(b)),
    // then extra in validGuideWords order
    ...validGuideWords.filter((w) => !base.includes(w) && current.has(w)),
  ];

  setSelections(devType, next);
};

const selectAllExtraForType = (devType: DeviationType) => {
  const base = deviationOptionsMap[devType];
  const extras = extraGuideWordsFor(devType);
  const next: GuideWord[] = [...base, ...extras];
  setSelections(devType, next);
};

const clearAllExtraForType = (devType: DeviationType) => {
  const base = deviationOptionsMap[devType];
  const current = getSelectionsFor(devType);
  const keepBase = current.filter((w) => base.includes(w));
  setSelections(devType, keepBase);
};

//
// ---------- Additional parameters section ----------
//
const showAdditional = ref(false);

const toggleAdditionalSection = () => {
  showAdditional.value = !showAdditional.value;
};

// header buttons: only additional params, current node
const selectAllAdditionalForCurrentNode = () => {
  const next: Record<ParamName, GuideWord[]> = { ...props.modelValue };

  const shouldClear = isAllAdditionalSelected();

  additionalParams.forEach((p) => {
    next[p] = shouldClear ? [] : [...validGuideWords];
  });

  emit("update:modelValue", next);
};


const clearAllAdditionalForCurrentNode = () => {
  const next: Record<ParamName, GuideWord[]> = { ...props.modelValue };
  additionalParams.forEach((p) => {
    next[p] = [];
  });
  emit("update:modelValue", next);
};
const openAdditionalFor = ref<AdditionalParam | null>(null);

const toggleAdditionalPopover = (param: AdditionalParam) => {
  openAdditionalFor.value =
    openAdditionalFor.value === param ? null : param;
};

// ✅ NEW: click param name = select all / clear all validGuideWords
const toggleAllForAdditional = (param: AdditionalParam) => {
  const current = getSelectionsFor(param);
  const allSelected = validGuideWords.every((gw) =>
    current.includes(gw)
  );

  const next = allSelected ? [] : [...validGuideWords];
  setSelections(param, next);
};
const isAllAdditionalSelected = (): boolean => {
  return additionalParams.every((p) =>
    validGuideWords.every((gw) => getSelectionsFor(p).includes(gw))
  );
};



//
// ---------- global “all lines” select/clear (only main params) ----------
//
const makeFullMainDeviations = (): Record<ParamName, GuideWord[]> => {
  const obj = {} as Record<ParamName, GuideWord[]>;
  deviationTypes.forEach((devType) => {
    obj[devType] = [...deviationOptionsMap[devType]];
  });
  return obj;
};

const makeEmptyMainDeviations = (): Record<ParamName, GuideWord[]> => {
  const obj = {} as Record<ParamName, GuideWord[]>;
  deviationTypes.forEach((devType) => {
    obj[devType] = [];
  });
  return obj;
};

const selectAllAllLines = () => {
  const newAll: Record<string | number, Record<ParamName, GuideWord[]>> = {
    ...props.allSelections,
  };

  props.allNodes.forEach((node) => {
    const prev = newAll[node.id] ?? ({} as Record<ParamName, GuideWord[]>);
    newAll[node.id] = {
      ...prev,
      ...makeFullMainDeviations(),
    };
  });

  emit("update:allSelections", newAll);
};

const deleteAllAllLines = () => {
  const newAll: Record<string | number, Record<ParamName, GuideWord[]>> = {
    ...props.allSelections,
  };

  props.allNodes.forEach((node) => {
    const prev = newAll[node.id] ?? ({} as Record<ParamName, GuideWord[]>);
    newAll[node.id] = {
      ...prev,
      ...makeEmptyMainDeviations(),
    };
  });

  emit("update:allSelections", newAll);
};

//
// ---------- preview modal (all nodes) ----------
//
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

const getNodeDeviation = (
  nodeId: string | number,
  param: ParamName
): GuideWord[] => {
  const nodeSel = props.allSelections?.[nodeId];
  if (!nodeSel) return [];
  return nodeSel[param] ?? [];
};

const hasAnyDeviationForNode = (nodeId: string | number): boolean => {
  return allParams.some((p) => getNodeDeviation(nodeId, p).length > 0);
};

const hasAnyDeviationSomeNode = computed(() =>
  props.allNodes.some((node: PreviewNode) => hasAnyDeviationForNode(node.id))
);
</script>

<template>
  <div class="bg-white rounded-2xl p-6 shadow-lg px-8 py-6 mb-6">
    <!-- Title + global all-lines buttons -->
    <div class="mb-4 flex items-center justify-between gap-4 mt-2">
      <h3 class="font-black text-2xl text-gray-800">Choose Perform Deviation</h3>

      <div class="flex items-center gap-2 text-xs">
        <button type="button" @click="selectAllAllLines"
          class="px-3 py-1.5 rounded-lg bg-black text-white font-semibold hover:bg-gray-900 transition">
          select all (all nodes)
        </button>
        <button type="button" @click="deleteAllAllLines"
          class="px-3 py-1.5 rounded-lg bg-white text-gray-900 font-semibold border border-gray-300 hover:bg-gray-50 transition">
          delete all (all nodes)
        </button>
      </div>
    </div>

    <!-- Analysis settings -->
    <div class="mb-4 grid gap-4 md:grid-cols-2">
      <div class="flex flex-col gap-1">
        <label class="text-xs font-medium text-gray-700">
          Analysis file name
        </label>
        <input v-model="analysisFile" type="text" placeholder="e.g. hazop_name_run01.xlsx"
          class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-gray-500" />
      </div>

      <div class="flex flex-col gap-1">
        <label class="text-xs font-medium text-gray-700"> Output folder </label>
        <input v-model="outputFolder" type="text" placeholder="e.g. 2025-12-08"
          class="w-full rounded-lg border border-gray-300 px-3 py-2 text-sm focus:outline-none focus:ring-1 focus:ring-gray-500" />
      </div>
    </div>

    <!-- Node info + pagination -->
    <div class="flex items-start justify-between mb-6 gap-6">
      <div class="px-3 text-sm text-gray-600 leading-snug space-y-1">
        <div
          class="py-2 px-4 justify-center item-center font-medium bg-gray-200 rounded-lg hover:bg-gray-300 transition">
          <span class="text-sm font-black">Node :</span>
          {{ nodeTitle || `node ${currentNode}` }} :
        </div>
        <div v-if="nodeLine" class="text-semibold">
          <span class="text-sm font-black">connection :</span>
          {{ nodeLine }}
        </div>
        <div v-if="nodeContext" class="text-semibold">
          <span class="text-sm font-black">description : </span>
          {{ nodeContext }}
        </div>
      </div>

      <!-- pagination -->
      <div class="flex items-center gap-2 text-sm text-gray-700">
        <button type="button" class="px-1 disabled:opacity-40" @click="goPrev" :disabled="currentNode === 1">
          ←
        </button>

        <template v-for="item in pages" :key="String(item)">
          <button v-if="item !== 'dots'" type="button"
            class="w-7 h-7 flex items-center justify-center rounded-full text-xs" :class="item === currentNode ? 'bg-black text-white' : 'text-gray-700'
              " @click="changePage(item as number)">
            {{ item }}
          </button>
          <span v-else class="px-1 text-xs text-gray-400 select-none"> … </span>
        </template>

        <button type="button" class="px-1 disabled:opacity-40" @click="goNext" :disabled="currentNode === totalNodes">
          →
        </button>
      </div>
    </div>

    <!-- Main row: left buttons + right main deviations -->
    <div class="flex gap-8">
      <!-- left: select/delete current line (main params only) -->
      <div class="w-52 flex flex-col gap-4">
        <div class="flex flex-col gap-2">
          <button type="button" @click="selectAllMainForCurrentNode"
            class="w-28 h-10 rounded-lg bg-black text-white text-sm font-semibold hover:bg-gray-900 transition">
            select all
          </button>
          <button type="button" @click="clearAllMainForCurrentNode"
            class="w-28 h-10 rounded-lg bg-white text-gray-900 text-sm font-semibold border border-gray-300 hover:bg-gray-50 transition">
            delete all
          </button>
        </div>
      </div>

      <!-- right: main deviation rows -->
      <div class="flex-1">
        <div class="grid md:grid-cols-2 gap-x-8 gap-y-3">
          <div v-for="devType in deviationTypes" :key="devType" class="relative w-full flex items-center gap-3">
            <!-- dot + name -->
            <div class="flex items-center gap-2 cursor-pointer" @click="toggleAllBaseForType(devType)">
              <span class="w-3 h-3 rounded-full" :class="hasSelectionsFor(devType) ? 'bg-black' : 'bg-gray-300'"></span>
              <span class="text-sm text-gray-700 hover:underline">
                {{ devType }}
              </span>
            </div>

            <!-- base options + plus button -->
            <div class="inline-flex flex-wrap items-center gap-1 bg-gray-200 rounded-full px-3 py-1">
              <button v-for="opt in deviationOptionsMap[devType]" :key="opt" type="button"
                class="px-2 py-0.5 rounded-full text-xs transition" :class="isSelected(devType, opt)
                  ? 'bg-black text-white'
                  : 'bg-transparent text-gray-800'
                  " @click.stop="toggleOption(devType, opt)">
                {{ opt }}
              </button>

              <!-- plus: extra guide words -->
              <button type="button"
                class="ml-1 w-6 h-6 rounded-full bg-white/80 text-gray-800 text-xs flex items-center justify-center hover:bg-white shadow-sm"
                @click.stop="toggleExtraPopover(devType)">
                +
              </button>
            </div>

            <!-- popover for extra guide words -->
            <div v-if="openExtraFor === devType"
              class="absolute z-20 top-full left-24 mt-2 w-56 rounded-xl bg-white shadow-xl border border-gray-200 py-2 text-xs">
              <div class="px-3 pb-2 font-semibold text-gray-800">
                Additional guide word
              </div>

              <button type="button" class="w-full text-left px-3 py-1 hover:bg-gray-100 text-[11px]"
                @click.stop="selectAllExtraForType(devType)">
                + select all
              </button>
              <button type="button"
                class="w-full text-left px-3 py-1 border-b border-gray-100 hover:bg-gray-100 text-[11px]"
                @click.stop="clearAllExtraForType(devType)">
                − clear all
              </button>

              <div class="mt-1 max-h-48 overflow-y-auto">
                <button v-for="gw in extraGuideWordsFor(devType)" :key="gw" type="button"
                  class="w-full flex items-center justify-between px-3 py-1 hover:bg-gray-100"
                  @click.stop="toggleExtraGuide(devType, gw)">
                  <span>{{ gw }}</span>
                  <span v-if="isSelected(devType, gw)">✓</span>
                </button>
              </div>

              <button type="button"
                class="w-full mt-1 px-3 py-1 text-center text-[11px] text-gray-600 border-t border-gray-100 hover:bg-gray-50"
                @click.stop="openExtraFor = null">
                cancel
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Additional parameters (collapsible) -->
    <div class="mt-8 border-t border-gray-200 pt-4">
      <div class="flex items-center justify-between mb-3">
        <button type="button"
          class="inline-flex items-center gap-2 px-3 py-1.5 rounded-full bg-gray-100 text-xs text-gray-700 hover:bg-gray-200 transition"
          @click="toggleAdditionalSection">
          <span>{{ showAdditional ? "−" : "+" }}</span>
          <span>Additional parameters </span>
        </button>

        <div v-if="showAdditional" class="flex items-center gap-2 text-[11px]">
          <button type="button"
            class="px-3 py-1 rounded-lg bg-black text-white font-semibold hover:bg-gray-900 transition"
            @click="selectAllAdditionalForCurrentNode">
            {{ isAllAdditionalSelected() ? "− delete all" : "+ select all" }}
          </button>
        </div>
      </div>

      <div v-if="showAdditional">
        <div class="grid md:grid-cols-4 gap-x-8 gap-y-3 px-25">
          <div v-for="param in additionalParams" :key="param" class="relative w-full flex items-center gap-3">
            <!-- Click param name: select all / clear all -->
            <div class="flex items-center gap-2 cursor-pointer" @click="toggleAllForAdditional(param)">
              <span class="w-3 h-3 rounded-full" :class="hasSelectionsFor(param) ? 'bg-black' : 'bg-gray-300'"></span>
              <span class="text-sm text-gray-700 hover:underline">
                {{ param }}
              </span>
            </div>

            <!-- Chip + plus button -->
            <div class="inline-flex flex-wrap items-center gap-1 bg-gray-200 rounded-full px-3 py-1">
              <!-- + button to open guide word list -->
              <button type="button"
                class="text-xs font-semibold px-2 py-0.5 rounded-full bg-white hover:bg-white shadow-sm"
                @click.stop="toggleAdditionalPopover(param)">
                {{ openAdditionalFor === param ? "−" : "+" }}
              </button>
            </div>

            <!-- Popover with all guide words for this additional param -->
            <div v-if="openAdditionalFor === param"
              class="absolute z-20 top-full left-0 mt-2 w-56 rounded-xl bg-white shadow-xl border border-gray-200 py-2 text-xs">
              <div class="px-3 pb-2 font-semibold text-gray-800 border-b border-gray-200">
                Guide words
              </div>
              <button type="button"
                class="w-full text-left px-3 py-1 hover:bg-gray-100 text-[11px] border-b border-gray-200"
                @click="selectAllAdditionalForCurrentNode">
                {{ isAllAdditionalSelected() ? "− delete all" : "+ select all" }}
              </button>


              <button v-for="gw in validGuideWords" :key="gw" type="button"
                class="w-full flex items-center justify-between px-3 py-1 hover:bg-gray-100"
                @click.stop="toggleOption(param, gw)">
                <span>{{ gw }}</span>
                <span v-if="isSelected(param, gw)">✓</span>
              </button>

              <button type="button"
                class="w-full mt-1 px-3 py-1 text-center text-[11px] text-gray-600 border-t border-gray-100 hover:bg-gray-50"
                @click.stop="openAdditionalFor = null">
                close
              </button>
            </div>
          </div>
        </div>
      </div>

    </div>

    <!-- Bottom-right: Preview + Next -->
    <div class="mt-6 flex items-center justify-end">
      <div class="flex gap-3">
        <button class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition"
          @click="handlePreviewClick">
          Preview
        </button>
        <button
          class="w-10 h-10 bg-white border border-gray-300 rounded-lg flex items-center justify-center hover:bg-gray-50 transition"
          @click="handleNextClick">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
            stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>

    <!-- Preview popup: all lines summary -->
    <transition name="fade">
      <div v-if="showPreview" class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
        <div class="bg-white rounded-2xl shadow-xl max-w-3xl w-full p-6 max-h-[80vh] overflow-y-auto">
          <h3 class="text-lg font-black text-gray-800 mb-2">
            Deviations preview for All Perform Nodes
          </h3>
          <p class="text-sm text-gray-600 mb-4">
            Review selected deviations for each nodes before submitting.
          </p>

          <div v-if="!hasAnyDeviationSomeNode" class="text-sm text-gray-500 italic mb-4">
            No deviations selected for any line yet.
          </div>

          <template v-for="node in allNodes" :key="node.id">
            <div v-if="hasAnyDeviationForNode(node.id)" class="mb-4 p-4 rounded-xl border border-gray-200 bg-gray-50">

              <h4 class="font-semibold text-gray-800 mb-1">
                <span class="text-sm font-black">Node :</span>
                {{ node.name }}
              </h4>

              <div class="text-xs text-gray-600 mb-2 space-y-1">
                <div v-if="node.range">
                  <span class="font-black">connection:</span> {{ node.range }}
                </div>
                <div v-if="node.context">
                  <span class="font-black">description:</span> {{ node.context }}
                </div>
              </div>

              <div class="text-sm space-y-1">
                <template v-for="p in allParams" :key="p">
                  <div v-if="getNodeDeviation(node.id, p).length > 0">
                    <span class="font-semibold">{{ p }}:</span>
                    {{ getNodeDeviation(node.id, p).join(", ") }}
                  </div>
                </template>
              </div>
            </div>
          </template>

          <div class="mt-4 flex justify-end gap-3">
            <button type="button"
              class="px-4 py-2 rounded-lg border border-gray-300 text-gray-700 hover:bg-gray-50 transition"
              @click="closePreview">
              Close
            </button>
            <button type="button" class="px-4 py-2 rounded-lg bg-black text-white hover:bg-gray-800 transition" @click="
              () => {
                closePreview();
                handleNextClick();
              }
            ">
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
