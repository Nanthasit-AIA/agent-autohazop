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

const deviationTypes: DeviationType[] = [
  "Flow",
  "Pressure",
  "Temperature",
  "Level",
  "Concentration",
  "Composition",
];

const createEmptyDeviationSelections = (): Record<DeviationType, string[]> => ({
  Flow: [],
  Pressure: [],
  Temperature: [],
  Level: [],
  Concentration: [],
  Composition: [],
});

// ----------------- basic state -----------------
const stage = ref<Stage>("initial");
const API_BASE = "http://localhost:5000";

const inputMode = ref<InputMode>("search");
const processName = ref("");
const processDescription = ref("");

// extract + JSON state
const isExtracting = ref(false);
const extractLabel = ref("Idle");
const jsonData = ref<any | null>(null);
const jsonFileName = ref<string | null>(null);
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
    if (payload.status === "loading_complete") {
      extractLabel.value = `loading ${payload.file_name ?? ""} complete`;
    } else if (payload.status === "error") {
      extractLabel.value = payload.error || "Error loading file";
    }
  }
);

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
    }
  | { mode: "search"; name: string };

const goToJsonAfterMinSpin = async () => {
  const started = extractStartedAt ?? Date.now();
  const elapsed = Date.now() - started;
  const remaining = 2000 - elapsed; // 2 sec spinner

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
    } else {
      const formData = new FormData();
      formData.append("name", payload.name);
      formData.append("description", payload.description);
      if (payload.file) {
        formData.append("file", payload.file);
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
  if (!data || !Array.isArray(data.connections)) return [];

  return data.connections.map((conn: any, index: number): NodeItem => {
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
  Record<string | number, Record<DeviationType, string[]>>
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

const currentDeviationModel = computed<Record<DeviationType, string[]>>({
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

const selectedNodesDetailed = computed<NodeItem[]>(() =>
  nodes.value.filter((n: NodeItem) => selectedNodes.value.includes(n.id))
);

// flatten selections → [{ line_id, parameter, guide_word }]
const buildHazopSelections = () => {
  const payload: {
    line_id: string;
    parameter: DeviationType;
    guide_word: string;
  }[] = [];

  for (const nodeId of selectedNodes.value) {
    const sel = nodeDeviationSelections.value[nodeId];
    if (!sel) continue;

    for (const param of deviationTypes) {
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

  // build selections (line_id, parameter, guide_word)
  const selections: {
    line_id: string;
    parameter: string;
    guide_word: string;
  }[] = [];

  for (const nodeId of selectedNodes.value) {
    const devs = nodeDeviationSelections.value[nodeId];
    if (!devs) continue;

    for (const param of deviationTypes) {
      const list = devs[param] || [];
      list.forEach((guide) => {
        selections.push({
          line_id: String(nodeId),
          parameter: param,
          guide_word: guide,
        });
      });
    }
  }

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
    <div class="fixed inset-x-0 top-0 z-50 bg-slate-50">
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
        <span class="ml-3 text-gray-600 font-bold">KU ChE</span>
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
          />
        </Transition>

        <!-- JSON result -->
        <Transition name="fade-slide">
          <JsonDisplay
            v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)"
            class="mt-4"
            :data="jsonData"
            :file-name="jsonFileName ?? undefined"
          />
        </Transition>

        <!-- Action buttons -->
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

        <!-- DeviationSelection -->
        <Transition name="fade-slide">
          <DeviationSelection
            v-if="stage === 'deviation' || stage === 'analysis'"
            v-model="currentDeviationModel"
            v-model:currentNode="deviationCurrentNode"
            v-model:analysisFileName="analysisFileName"
            v-model:outputFolder="outputFolder"
            :total-nodes="selectedNodes.length"
            :node-title="currentNode?.name || `node ${deviationCurrentNode}`"
            :node-line="currentNode?.range"
            :node-context="currentNode?.context"
            :all-nodes="selectedNodesDetailed"
            :all-selections="nodeDeviationSelections"
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
            @start="handleStartAnalysis"
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
