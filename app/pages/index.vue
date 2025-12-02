<script setup lang="ts">
import { ref, computed, watch, nextTick } from "vue";
import { io } from "socket.io-client";
import PageHeader from "~/components/PageHeader.vue";
import ProcessInput from "~/components/ProcessInput.vue";
import ExtractStatus from "~/components/ExtractStatus.vue";
import JsonDisplay from "~/components/JsonDisplay.vue";
import ActionButtons from "~/components/ActionButton.vue";
import NodeSelection from "~/components/NodeSelection.vue";
import DeviationSelection from "~/components/DeviationSelection.vue";
import AnalysisControl from "~/components/AnalysisControl.vue";
import type { Connection } from "~/components/PipelineGraphModal.vue";

// ----------------- types -----------------
type Stage =
  | "initial"
  | "input"
  | "extract"
  | "json"
  | "node"
  | "deviation"
  | "analysis";
type InputMode = "full" | "search";

interface NodeItem {
  id: string | number;
  name: string;
  range?: string;
  context?: string;
}

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
  | "After";

const deviationTypes: DeviationType[] = [
  "Flow",
  "Pressure",
  "Temperature",
  "Level",
  "Concentration",
  "Composition",
];

const allParams: ParamName[] = [
  ...deviationTypes,
  "Phase",
  "Utility",
  "Power",
  "Instrument",
  "Human Action",
  "Maintenance",
  "Operation Timing",
];

// helper: empty selections for ALL parameters (main + additional)
const createEmptyDeviationSelections = (): Record<ParamName, GuideWord[]> => {
  return allParams.reduce(
    (acc, p) => {
      acc[p] = [];
      return acc;
    },
    {} as Record<ParamName, GuideWord[]>
  );
};

// ----------------- basic state -----------------
const stage = ref<Stage>("initial");
const API_BASE = "http://localhost:5000";

const inputMode = ref<InputMode>("search");
const processName = ref("");
const processDescription = ref("");

// extract + JSON state
const isExtracting = ref(false);
const extractLabel = ref("Idle");
const extractError = ref<string | null>(null);
const jsonData = ref<any | null>(null);
const jsonFileName = ref<string | null>(null);
const hasCalledHazop = ref(false);
let extractStartedAt: number | null = null;

// action state
type ActionState = "idle" | "ready" | "running";
const actionState = ref<ActionState>("idle");

// ✅ analysis config from DeviationSelection (file name + output folder)
const analysisFileName = ref<string>("");
const outputFolder = ref<string>("");

// ----------------- Socket.IO -----------------
const socket = io(API_BASE);

// file_status for ExtractStatus
socket.on(
  "file_status",
  (payload: { status: string; file_name?: string; error?: string }) => {
    const fileName = payload.file_name ?? "";

    if (payload.status === "working") {
      isExtracting.value = true;
      extractError.value = null;
      extractLabel.value = fileName ? `processing ${fileName}…` : "processing…";
    } else if (payload.status === "loading_complete") {
      isExtracting.value = false;
      extractError.value = null;
      extractLabel.value = `loading ${fileName} complete`;
    } else if (payload.status === "error") {
      isExtracting.value = false;
      extractError.value = payload.error || "Error loading file";
      extractLabel.value = extractError.value;
    }
  }
);

const resetAllState = () => {
  stage.value = "initial";
  inputMode.value = "search";

  processName.value = "";
  processDescription.value = "";

  // extract / json
  isExtracting.value = false;
  extractLabel.value = "Idle";
  extractError.value = null;
  jsonData.value = null;
  jsonFileName.value = null;
  extractStartedAt = null;

  // action / HAZOP
  actionState.value = "idle";
  hasCalledHazop.value = false;

  nodes.value = [];
  selectedNodes.value = [];
  deviationCurrentNode.value = 1;
  nodeDeviationSelections.value = {};

  hazopRuns.value = [];
  analysisLabel.value = "waiting to analysis";
  analysisError.value = "";
  hazopRunning.value = false;
  analysisFileName.value = "";
  outputFolder.value = "";

  if (typeof window !== "undefined") {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
};

const handleExit = () => {
  resetAllState();
};

// ---- system inputs / outputs for hazards popup ----
const systemInputs = computed<string[]>(() => {
  const data = jsonData.value;
  if (!data) return [];

  // handle both { system_inputs: [...] } and { pid_data: { system_inputs: [...] } }
  const root = Array.isArray((data as any).system_inputs)
    ? (data as any)
    : (data as any).pid_data &&
        Array.isArray((data as any).pid_data.system_inputs)
      ? (data as any).pid_data
      : null;

  if (!root) return [];

  return (root.system_inputs as any[]).map((item, idx) => {
    if (typeof item === "string") return item;
    // common schema: { name: "...", id: "...", type: "...", ... }
    return item.name ?? item.id ?? `input_${idx}`;
  });
});

const systemOutputs = computed<string[]>(() => {
  const data = jsonData.value;
  if (!data) return [];

  const root = Array.isArray((data as any).system_outputs)
    ? (data as any)
    : (data as any).pid_data &&
        Array.isArray((data as any).pid_data.system_outputs)
      ? (data as any).pid_data
      : null;

  if (!root) return [];

  return (root.system_outputs as any[]).map((item, idx) => {
    if (typeof item === "string") return item;
    return item.name ?? item.id ?? `output_${idx}`;
  });
});
const showConnectionPreview = ref(false);

const connectionPreview = computed<Connection[]>(() => {
  const d = jsonData.value;
  if (!d || typeof d !== "object") return [];

  const root = Array.isArray((d as any).connections)
    ? (d as any)
    : (d as any).pid_data && Array.isArray((d as any).pid_data.connections)
      ? (d as any).pid_data
      : null;

  if (!root) return [];

  return (root.connections as any[]).map(
    (c, idx): Connection => ({
      line_id: String(c.line_id ?? `L${idx + 1}`),
      from_id: String(c.from_id ?? ""),
      to_id: String(c.to_id ?? ""),
      context: c.context ? String(c.context) : "",
    })
  );
});


// ----------------- HAZOP analysis status + runs -----------------
interface HazopRun {
  line_id: string;
  parameter: string;
  guide_word: string;
  tokens_used?: number;
}

const analysisLabel = ref<string>("waiting to analysis");
const analysisError = ref<string>("");
const hazopRunning = ref<boolean>(false);
const hazopRuns = ref<HazopRun[]>([]);

const displayLabel = computed<string>(() => {
  if (hazopRunning.value && hazopRuns.value.length > 0) {
    const lastIndex = hazopRuns.value.length - 1;
    const last = hazopRuns.value[lastIndex];

    if (last) {
      return `Running ${last.line_id} - ${last.parameter} - ${last.guide_word}...`;
    }
  }

  // fallback: generic status text
  return analysisLabel.value;
});

// ✅ progress: update label + append run row
socket.on(
  "hazop_progress",
  (msg: {
    line_id: string;
    parameter: string;
    guide_word: string;
    tokens_used?: number;
  }) => {
    hazopRunning.value = true;

    // 🔹 show what is running now
    analysisLabel.value = `Running ${msg.line_id} - ${msg.parameter} - ${msg.guide_word}...`;

    hazopRuns.value.push({
      line_id: msg.line_id,
      parameter: msg.parameter,
      guide_word: msg.guide_word,
      tokens_used: msg.tokens_used,
    });
  }
);

// ✅ complete: update label + error + saved path (folder + file name)
socket.on(
  "hazop_complete",
  (msg: {
    ok: boolean;
    error?: string;
    folder?: string;
    file_name?: string;
  }) => {
    hazopRunning.value = false;

    if (msg.folder) outputFolder.value = msg.folder;
    if (msg.file_name) analysisFileName.value = msg.file_name;

    if (msg.ok) {
      analysisLabel.value = "analysis complete";
      analysisError.value = "";
    } else {
      analysisLabel.value = "analysis finished with error";
      analysisError.value = msg.error || "Unknown error";
    }
  }
);

// ----------------- CTA / search -----------------
const handleCtaClick = () => {
  stage.value = "input";
  inputMode.value = "full";
  processName.value = "";
  processDescription.value = "";
  jsonData.value = null;
  jsonFileName.value = null;
  extractLabel.value = "Idle";
  actionState.value = "idle";
};

const handleSearchClick = () => {
  stage.value = "input";
  inputMode.value = "search";
  processDescription.value = "";
  jsonData.value = null;
  jsonFileName.value = null;
  extractLabel.value = "Idle";
  actionState.value = "idle";
};

// ----------------- extract flow -----------------
type StartExtractPayload =
  | {
      mode: "full";
      name: string;
      description: string;
      file: File | null;
      fileName: string | null;
      files?: File[];
    }
  | { mode: "search"; name: string };

const goToJsonAfterMinSpin = async () => {
  const started = extractStartedAt ?? Date.now();
  const elapsed = Date.now() - started;
  const remaining = 2000 - elapsed;

  const doTransition = async () => {
    isExtracting.value = false;
    stage.value = "json";
    actionState.value = "ready";

    await nextTick();
    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: "smooth",
    });
  };

  if (remaining > 0) {
    setTimeout(() => {
      void doTransition();
    }, remaining);
  } else {
    await doTransition();
  }
};

const onStartExtract = async (payload: StartExtractPayload) => {
  const name = payload.name.trim();
  if (!name) return;

  stage.value = "extract";
  isExtracting.value = true;
  extractError.value = null;
  jsonData.value = null;
  jsonFileName.value = null;
  extractLabel.value = `loading ${name}…`;
  extractStartedAt = Date.now();

  try {
    if (payload.mode === "search") {
      const res = await fetch(
        `${API_BASE}/api/search?name=${encodeURIComponent(name)}`
      );
      const body = await res.json();

      if (!res.ok || !body.ok) {
        extractLabel.value = body.error || "Error loading file";
        return;
      }

      jsonData.value = body.data;
      jsonFileName.value = body.file_name;
      extractLabel.value = `loading ${body.file_name} complete`;

      await goToJsonAfterMinSpin();
      nodes.value = buildNodesFromJson(jsonData.value);
      selectedNodes.value = [];
      nodeDeviationSelections.value = {};
    } else {
      const formData = new FormData();
      formData.append("name", payload.name);
      formData.append("description", payload.description);

      const filesToSend: File[] =
        payload.files && payload.files.length > 0
          ? payload.files
          : payload.file
            ? [payload.file]
            : [];

      if (filesToSend.length === 0) {
        extractLabel.value = "No file selected";
        isExtracting.value = false;
        return;
      }

      for (const f of filesToSend) {
        formData.append("file", f);
      }

      const res = await fetch(`${API_BASE}/api/full`, {
        method: "POST",
        body: formData,
      });

      const body = await res.json();

      if (!res.ok || !body.ok) {
        extractLabel.value = body.error || "Error during full extract";
        isExtracting.value = false;
        return;
      }

      jsonData.value = body.data;
      jsonFileName.value = body.file_name ?? payload.fileName ?? payload.name;
      extractLabel.value = `loading ${jsonFileName.value} complete`;

      await goToJsonAfterMinSpin();
      nodes.value = buildNodesFromJson(jsonData.value);
      selectedNodes.value = [];
      nodeDeviationSelections.value = {};
    }
  } catch (err) {
    console.error(err);
    extractLabel.value = "Network error";

    const started = extractStartedAt ?? Date.now();
    const elapsed = Date.now() - started;
    const remaining = 1000 - elapsed;

    const stop = () => {
      isExtracting.value = false;
    };

    if (remaining > 0) {
      setTimeout(stop, remaining);
    } else {
      stop();
    }
  }
};

// ----------------- NodeSelection data -----------------
const nodes = ref<NodeItem[]>([]);

const buildNodesFromJson = (data: any): NodeItem[] => {
  if (!data || typeof data !== "object") return [];
  const root = Array.isArray(data.connections)
    ? data
    : data.pid_data && Array.isArray(data.pid_data.connections)
      ? data.pid_data
      : null;

  if (!root) return [];

  const connections = root.connections as any[];

  return connections.map((conn: any, index: number): NodeItem => {
    const lineId = conn.line_id ?? `L${index + 1}`;
    const from = conn.from_id ?? "";
    const to = conn.to_id ?? "";
    const range = from && to ? `${from} → ${to}` : undefined;

    return {
      id: lineId,
      name: `${lineId}${range ? ` (${range})` : ""}`,
      range,
      context: conn.context ?? "",
    };
  });
};

const selectedNodes = ref<(string | number)[]>([]);

// ----------------- deviation selection per node -----------------
const deviationCurrentNode = ref(1);

// map: nodeId -> deviations
const nodeDeviationSelections = ref<
  Record<string | number, Record<ParamName, GuideWord[]>>
>({});

const currentNodeId = computed<string | number | undefined>(() => {
  const index = deviationCurrentNode.value - 1;
  return selectedNodes.value[index];
});

const currentNode = computed<NodeItem | undefined>(() => {
  const id = currentNodeId.value;
  if (id == null) return undefined;
  return nodes.value.find((n: NodeItem) => n.id === id);
});

const currentDeviationModel = computed<Record<ParamName, GuideWord[]>>({
  get() {
    const id = currentNodeId.value;
    if (id == null) return createEmptyDeviationSelections();

    if (!nodeDeviationSelections.value[id]) {
      nodeDeviationSelections.value[id] = createEmptyDeviationSelections();
    }
    return nodeDeviationSelections.value[id];
  },
  set(val) {
    const id = currentNodeId.value;
    if (id == null) return;

    nodeDeviationSelections.value = {
      ...nodeDeviationSelections.value,
      [id]: val,
    };
  },
});

const selectedNodesDetailed = computed<NodeItem[]>(() => {
  const result = nodes.value.filter((n) => selectedNodes.value.includes(n.id));
  return result.sort((a, b) => {
    const aa = isNaN(Number(a.id)) ? String(a.id) : Number(a.id);
    const bb = isNaN(Number(b.id)) ? String(b.id) : Number(b.id);
    return aa < bb ? -1 : aa > bb ? 1 : 0;
  });
});

// flatten selections → [{ line_id, parameter, guide_word }]
const buildHazopSelections = () => {
  const payload: {
    line_id: string;
    parameter: ParamName;
    guide_word: string;
  }[] = [];

  for (const nodeId of selectedNodes.value) {
    const sel = nodeDeviationSelections.value[nodeId];
    if (!sel) continue;

    for (const param of allParams) {
      const chosen = sel[param] ?? [];
      for (const gw of chosen) {
        payload.push({
          line_id: String(nodeId),
          parameter: param,
          guide_word: gw,
        });
      }
    }
  }

  return payload;
};

// ----------------- scrolling + layout -----------------
watch(stage, async (newStage) => {
  if (typeof window === "undefined") return;
  await nextTick();

  if (["json", "node", "deviation", "analysis"].includes(newStage)) {
    window.scrollTo({
      top: document.documentElement.scrollHeight,
      behavior: "smooth",
    });
  }

  if (newStage === "input") {
    window.scrollTo({ top: 0, behavior: "smooth" });
  }
});

const mainPaddingClass = computed(() => {
  switch (stage.value) {
    case "initial":
      return "pt-90";
    case "input":
      return "pt-40";
    default:
      return "pt-40";
  }
});

const handleSearchFromHeader = (query: string) => {
  if (!query) return;
  stage.value = "input";
  processName.value = query;
  processDescription.value = "";
  nextTick(() => {
    window.scrollTo({ top: 200, behavior: "smooth" });
  });
};

// ----------------- stage transitions -----------------
const handleCallHazop = () => {
  if (hasCalledHazop.value) return;
  hasCalledHazop.value = true;

  actionState.value = "running";
  stage.value = "node";
};

const handleNodeNext = () => {
  if (selectedNodes.value.length === 0) return;
  deviationCurrentNode.value = 1;
  stage.value = "deviation";
};

const handleDeviationNext = () => {
  stage.value = "analysis";
};

const handleDeviationPreview = () => {
  // preview handled inside DeviationSelection modal
};

// ----------------- Start analysis (button in AnalysisControl) -----------------
const handleStartAnalysis = async () => {
  if (!jsonData.value) {
    analysisError.value = "No PID data loaded";
    return;
  }

  // build selections (line_id, parameter, guide_word) for ALL params
  const selections = buildHazopSelections();

  if (!selections.length) {
    analysisError.value = "Please select at least one deviation.";
    return;
  }

  // reset run state
  hazopRuns.value = [];
  analysisError.value = "";
  analysisLabel.value = "starting analysis...";
  hazopRunning.value = true; // indicator -> blue
  stage.value = "analysis";

  await new Promise((resolve) => setTimeout(resolve, 2000));

  // emit to backend via Socket.IO ✅
  socket.emit("hazop_start", {
    pid_data: jsonData.value,
    selections,
    file_name: analysisFileName.value,
    output_folder: outputFolder.value,
  });
};
</script>

<template>
  <div class="min-h-screen bg-linear-to-br from-slate-50 to-slate-100">
    <!-- fixed top bar -->
    <div class="fixed inset-x-0 top-0 z-40 bg-slate-50">
      <div class="mx-auto flex items-center justify-start px-30 py-10">
        <div class="flex gap-2 items-center justify-center">
          <img
            src="~/assets/logo/logo_ku.png"
            alt="IDEKTEP Logo"
            class="w-17 h-17 rounded-full"
          />
          <img
            src="~/assets/logo/logo_che.png"
            alt="IDEKTEP Logo"
            class="w-20 h-20 rounded-full"
          />
        </div>
        <span class="ml-3 text-gray-600 font-bold">KU ChE / CNP LAB</span>
      </div>
    </div>

    <!-- main content -->
    <div
      class="pt-20 px-8 flex justify-center transition-all duration-500 ease-out"
      :class="mainPaddingClass"
    >
      <div class="w-full max-w-6xl">
        <PageHeader
          class="mb-6"
          @cta-click="handleCtaClick"
          @search-click="handleSearchClick"
          @search-from-header="handleSearchFromHeader"
        />

        <!-- ProcessInput -->
        <Transition name="fade-slide">
          <ProcessInput
            v-if="stage !== 'initial'"
            v-model:name="processName"
            v-model:description="processDescription"
            :mode="inputMode"
            :busy="isExtracting"
            @start-extract="onStartExtract"
          />
        </Transition>

        <!-- ExtractStatus -->
        <Transition name="fade-slide">
          <ExtractStatus
            v-if="
              ['extract', 'json', 'node', 'deviation', 'analysis'].includes(
                stage
              )
            "
            class="mt-4"
            :active="isExtracting"
            :label="extractLabel"
            :error-message="extractError"
          />
        </Transition>

        <!-- JSON result -->
        <Transition name="fade-slide">
          <JsonDisplay
            v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)"
            class="mt-4"
            :data="jsonData"
            :file-name="jsonFileName ?? undefined"
            @preview-connections="showConnectionPreview = true"
          />
        </Transition>

        <!-- Action buttons -->
        <Transition name="fade-slide">
          <ActionButtons
            v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)"
            class="mt-6"
            :state="actionState"
            :disabled="hasCalledHazop"
            @call-hazop="handleCallHazop"
            @exit="handleExit"
          />
        </Transition>

        <!-- NodeSelection -->
        <Transition name="fade-slide">
          <NodeSelection
            v-if="['node', 'deviation', 'analysis'].includes(stage)"
            v-model="selectedNodes"
            :nodes="nodes"
            class="mt-4"
            :connections="connectionPreview"
            @next="handleNodeNext"
          />
        </Transition>

        <!-- DeviationSelection -->
        <Transition name="fade-slide">
          <DeviationSelection
            v-if="stage === 'deviation' || stage === 'analysis'"
            v-model="currentDeviationModel"
            v-model:currentNode="deviationCurrentNode"
            v-model:analysisFileName="analysisFileName"
            v-model:outputFolder="outputFolder"
            v-model:allSelections="nodeDeviationSelections"
            :allNodes="selectedNodesDetailed"
            :totalNodes="selectedNodesDetailed.length"
            :nodeTitle="selectedNodesDetailed[deviationCurrentNode - 1]?.name"
            :nodeLine="selectedNodesDetailed[deviationCurrentNode - 1]?.range"
            :nodeContext="
              selectedNodesDetailed[deviationCurrentNode - 1]?.context
            "
            class="mt-4"
            @preview="handleDeviationPreview"
            @next="handleDeviationNext"
          />
        </Transition>

        <!-- AnalysisControl -->
        <Transition name="fade-slide">
          <AnalysisControl
            v-if="stage === 'analysis'"
            class="mt-4"
            :active="hazopRunning"
            :label="displayLabel"
            :error-message="analysisError"
            :runs="hazopRuns"
            :output-folder="outputFolder"
            :file-name="analysisFileName"
            :process-inputs="systemInputs"
            :process-outputs="systemOutputs"
            @start="handleStartAnalysis"
            @exit="handleExit"
          />
        </Transition>
        <!-- Connections LEGO preview popup -->
        <transition name="fade-slide">
          <div
            v-if="showConnectionPreview && connectionPreview.length"
            class="fixed inset-0 z-50 flex items-center justify-center bg-black/40"
          >
            <div
              class="bg-white rounded-2xl shadow-2xl max-w-5xl w-full mx-4 p-6 max-h-[90vh] overflow-y-auto"
            >
              <ConnectionPreview
                :connections="connectionPreview"
                @close="showConnectionPreview = false"
              />
            </div>
          </div>
        </transition>
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
