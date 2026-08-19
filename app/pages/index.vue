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
import type { Connection } from "~/components/SelectedPipelineGraph.vue";

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
  nodeBoundary?: string;
  flowDirection?: string;
  source?: "connections" | "line_level_connections";
  equipmentSummary?: string;
  valveSummary?: string;
  instrumentSummary?: string;
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
const processNodeDefine = ref("");
const processIntention = ref("");

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

// LLM provider/model chosen during full extraction, reused for HAZOP
const selectedLlmProvider = ref("own_api");
const selectedLlmModel = ref("");

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
  processNodeDefine.value = "";
  processIntention.value = "";

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

// ---- JSON normalization helpers ----
const unwrapPidRoot = (data: any): any | null => {
  if (!data || typeof data !== "object") return null;

  // OpenAI parsed response wrapper: { choices: [{ message: { parsed: {...} } }] }
  const choicesParsed = data?.choices?.[0]?.message?.parsed;
  if (choicesParsed && typeof choicesParsed === "object") return choicesParsed;

  // Backend search/full wrapper: { pid_data: {...}, metadata: {...} }
  if (data.pid_data && typeof data.pid_data === "object") return data.pid_data;

  // Generic wrapper used by some extraction scripts: { parsed: {...} }
  if (data.parsed && typeof data.parsed === "object") return data.parsed;

  return data;
};

const pidRoot = computed<any | null>(() => unwrapPidRoot(jsonData.value));

const toDisplayText = (value: any, fallback = ""): string => {
  if (value === null || value === undefined || value === "") return fallback;
  if (typeof value === "string") return value;
  if (typeof value === "number" || typeof value === "boolean") return String(value);
  if (Array.isArray(value)) {
    return value
      .map((item) => toDisplayText(item))
      .filter(Boolean)
      .join("; ");
  }
  if (typeof value === "object") {
    return (
      value.name ??
      value.id ??
      value.tag ??
      value.type ??
      value.utility_type ??
      JSON.stringify(value)
    );
  }
  return String(value);
};

const idListToDetails = (ids: any[], catalog: any[]): any[] => {
  if (!Array.isArray(ids)) return [];
  if (!Array.isArray(catalog)) return ids;

  const byId = new Map(
    catalog
      .filter((item) => item && typeof item === "object" && item.id)
      .map((item) => [String(item.id), item])
  );

  return ids.map((id) => {
    const key = String(id);
    return byId.get(key) ?? id;
  });
};

const getPidConnections = (root: any | null): any[] => {
  if (!root || typeof root !== "object") return [];
  return Array.isArray(root.connections) ? root.connections : [];
};

const getPidLineLevelConnections = (root: any | null): any[] => {
  if (!root || typeof root !== "object") return [];
  return Array.isArray(root.line_level_connections) ? root.line_level_connections : [];
};

const buildConnectionTitle = (conn: any, index: number, source: "connections" | "line_level_connections") => {
  const lineId = conn?.line_id ?? `${source === "connections" ? "NODE" : "LINE"}-${index + 1}`;
  const nodeName = conn?.node ?? conn?.name ?? "";
  const from = conn?.from_id ?? "";
  const to = conn?.to_id ?? "";
  const range = from && to ? `${from} → ${to}` : "";

  if (nodeName) return `${lineId} | ${nodeName}`;
  if (range) return `${lineId} | ${range}`;
  return String(lineId);
};

const mapConnectionForGraph = (
  conn: any,
  index: number,
  source: "connections" | "line_level_connections"
): Connection => ({
  line_id: String(conn?.line_id ?? `${source}-${index + 1}`),
  from_id: String(conn?.from_id ?? conn?.node ?? ""),
  to_id: String(conn?.to_id ?? ""),
  context: [
    conn?.node ? `Node: ${conn.node}` : "",
    conn?.node_boundary ? `Boundary: ${conn.node_boundary}` : "",
    conn?.flow_direction ? `Flow: ${conn.flow_direction}` : "",
    conn?.context ? String(conn.context) : "",
  ]
    .filter(Boolean)
    .join("\n"),
});

// ---- system inputs / outputs for hazards popup ----
const systemInputs = computed<string[]>(() => {
  const root = pidRoot.value;
  if (!root || !Array.isArray(root.system_inputs)) return [];
  return root.system_inputs.map((item: any, idx: number) =>
    toDisplayText(item, `input_${idx}`)
  );
});

const systemOutputs = computed<string[]>(() => {
  const root = pidRoot.value;
  if (!root || !Array.isArray(root.system_outputs)) return [];
  return root.system_outputs.map((item: any, idx: number) =>
    toDisplayText(item, `output_${idx}`)
  );
});

const showConnectionPreview = ref(false);

// Modify dialog trigger (forwarded from JsonDisplay graph review → ActionButton)
const modifyPrefill = ref("");
const modifyOpenTs = ref(0);

const handleOpenModify = (instruction: string) => {
  modifyPrefill.value = instruction;
  modifyOpenTs.value = Date.now();
};

const handleModifyDone = (payload: { data: any; fileName: string }) => {
  jsonData.value = payload.data;
  jsonFileName.value = payload.fileName;
  nodes.value = buildNodesFromJson(payload.data);
};

const connectionPreview = computed<Connection[]>(() => {
  const root = pidRoot.value;
  const grouped = getPidConnections(root).map((conn, idx) =>
    mapConnectionForGraph(conn, idx, "connections")
  );
  const lineLevel = getPidLineLevelConnections(root).map((conn, idx) =>
    mapConnectionForGraph(conn, idx, "line_level_connections")
  );

  const seen = new Set<string>();
  return [...grouped, ...lineLevel].filter((conn) => {
    const key = String(conn.line_id);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
  });
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
  processNodeDefine.value = "";
  processIntention.value = "";
  jsonData.value = null;
  jsonFileName.value = null;
  extractLabel.value = "Idle";
  actionState.value = "idle";
};

const handleSearchClick = () => {
  stage.value = "input";
  inputMode.value = "search";
  processDescription.value = "";
  processNodeDefine.value = "";
  processIntention.value = "";
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
    nodeDefine: string;
    intention: string;
    file: File | null;
    fileName: string | null;
    files?: File[];
    llm_provider: string;
    llm_model: string;
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
      selectedLlmProvider.value = payload.llm_provider ?? "own_api";
      selectedLlmModel.value = payload.llm_model ?? "";

      const formData = new FormData();
      formData.append("name", payload.name);
      formData.append("description", payload.description);
      formData.append("node_define", payload.nodeDefine ?? "");
      formData.append("intention", payload.intention ?? "");
      formData.append("llm_provider", payload.llm_provider ?? "own_api");
      if (payload.llm_model) formData.append("llm_model", payload.llm_model);

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
  const root = unwrapPidRoot(data);
  if (!root || typeof root !== "object") return [];

  const equipmentCatalog = Array.isArray(root.equipment) ? root.equipment : [];
  const valveCatalog = Array.isArray(root.valves) ? root.valves : [];
  const instrumentCatalog = Array.isArray(root.instruments) ? root.instruments : [];

  const toNodeItem = (
    conn: any,
    index: number,
    source: "connections" | "line_level_connections"
  ): NodeItem => {
    const lineId = conn?.line_id ?? `${source === "connections" ? "NODE" : "LINE"}-${index + 1}`;
    const from = conn?.from_id ?? "";
    const to = conn?.to_id ?? "";
    const range = from && to ? `${from} → ${to}` : undefined;

    const includedEquipment = Array.isArray(conn?.included_equipment)
      ? conn.included_equipment
      : [from, to].filter(Boolean);

    const valveIds = Array.isArray(conn?.valves) ? conn.valves : [];
    const instrumentIds = Array.isArray(conn?.instruments) ? conn.instruments : [];

    const equipmentSummary = toDisplayText(
      idListToDetails(includedEquipment, equipmentCatalog)
    );
    const valveSummary = toDisplayText(idListToDetails(valveIds, valveCatalog));
    const instrumentSummary = toDisplayText(
      idListToDetails(instrumentIds, instrumentCatalog)
    );

    const displayName = buildConnectionTitle(conn, index, source);

    return {
      id: String(lineId),
      name: displayName,
      range,
      context: conn?.context ?? "",
      nodeBoundary: conn?.node_boundary ?? "",
      flowDirection: conn?.flow_direction ?? "",
      source,
      equipmentSummary,
      valveSummary,
      instrumentSummary,
    };
  };

  const groupedNodes = getPidConnections(root).map((conn, idx) =>
    toNodeItem(conn, idx, "connections")
  );
  const lineLevelNodes = getPidLineLevelConnections(root).map((conn, idx) =>
    toNodeItem(conn, idx, "line_level_connections")
  );

  const seen = new Set<string>();
  return [...groupedNodes, ...lineLevelNodes].filter((node) => {
    const key = String(node.id);
    if (seen.has(key)) return false;
    seen.add(key);
    return true;
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


const currentNodeContextForDeviation = computed(() => {
  const node = currentNode.value;
  if (!node) return "";

  return [
    node.context ? `Context: ${node.context}` : "",
    node.nodeBoundary ? `Boundary: ${node.nodeBoundary}` : "",
    node.flowDirection ? `Flow direction: ${node.flowDirection}` : "",
    node.equipmentSummary ? `Equipment: ${node.equipmentSummary}` : "",
    node.valveSummary ? `Valves: ${node.valveSummary}` : "",
    node.instrumentSummary ? `Instruments: ${node.instrumentSummary}` : "",
  ]
    .filter(Boolean)
    .join("\n");
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
    llm_provider: selectedLlmProvider.value,
    llm_model: selectedLlmModel.value,
  });
};
</script>

<template>
  <div class="min-h-screen bg-linear-to-br from-slate-50 to-slate-100 overflow-y-auto">
    <!-- fixed top bar -->
    <div class="fixed inset-x-0 top-0 z-40 bg-white">
      <div class="mx-auto flex items-center justify-start px-30 py-10">
        <div class="flex gap-2 items-center justify-center">
          <img src="~/assets/logo/logo_ku.png" alt="IDEKTEP Logo" class="w-17 h-17 rounded-full" />
          <img src="~/assets/logo/logo_che.png" alt="IDEKTEP Logo" class="w-20 h-20 rounded-full" />
          <img src="~/assets/logo/logo_scgc.png" alt="IDEKTEP Logo" class="w-35 h-20 " />
        </div>
        <span class="ml-3 text-gray-400 font-black"></span>
      </div>
    </div>

    <!-- main content -->
    <div class="pt-20 px-8 flex justify-center transition-all duration-500 ease-out" :class="mainPaddingClass">
      <div class="w-full max-w-6xl">
        <PageHeader class="mb-6" @cta-click="handleCtaClick" @search-click="handleSearchClick"
          @search-from-header="handleSearchFromHeader" />

        <!-- ProcessInput -->
        <Transition name="fade-slide">
          <ProcessInput v-if="stage !== 'initial'" v-model:name="processName" v-model:description="processDescription"
            v-model:nodeDefine="processNodeDefine" v-model:intention="processIntention"
            :mode="inputMode" :busy="isExtracting" @start-extract="onStartExtract" />
        </Transition>

        <!-- ExtractStatus -->
        <Transition name="fade-slide">
          <ExtractStatus v-if="
            ['extract', 'json', 'node', 'deviation', 'analysis'].includes(
              stage
            )
          " class="mt-4" :active="isExtracting" :label="extractLabel" :error-message="extractError" />
        </Transition>

        <!-- JSON result -->
        <Transition name="fade-slide">
          <JsonDisplay v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)" class="mt-4" :data="jsonData"
            :file-name="jsonFileName ?? undefined" @preview-connections="showConnectionPreview = true"
            @open-modify="handleOpenModify" />
        </Transition>

        <!-- Action buttons -->
        <Transition name="fade-slide">
          <ActionButtons v-if="['json', 'node', 'deviation', 'analysis'].includes(stage)" class="mt-6"
            :state="actionState" :disabled="hasCalledHazop"
            :json-file-name="jsonFileName"
            :prefill-instruction="modifyPrefill"
            :open-trigger="modifyOpenTs"
            @call-hazop="handleCallHazop" @exit="handleExit"
            @modify-done="handleModifyDone" />
        </Transition>

        <!-- NodeSelection -->
        <Transition name="fade-slide">
          <NodeSelection v-if="['node', 'deviation', 'analysis'].includes(stage)" v-model="selectedNodes" :nodes="nodes"
            class="mt-4" :connections="connectionPreview" @next="handleNodeNext" />
        </Transition>

        <!-- DeviationSelection -->
        <Transition name="fade-slide">
          <DeviationSelection v-if="stage === 'deviation' || stage === 'analysis'" v-model="currentDeviationModel"
            v-model:currentNode="deviationCurrentNode" v-model:analysisFileName="analysisFileName"
            v-model:outputFolder="outputFolder" v-model:allSelections="nodeDeviationSelections"
            :allNodes="selectedNodesDetailed" :totalNodes="selectedNodesDetailed.length"
            :nodeTitle="selectedNodesDetailed[deviationCurrentNode - 1]?.name"
            :nodeLine="selectedNodesDetailed[deviationCurrentNode - 1]?.range" :nodeContext="currentNodeContextForDeviation"
              class="mt-4" @preview="handleDeviationPreview" @next="handleDeviationNext" />
        </Transition>

        <!-- AnalysisControl -->
        <Transition name="fade-slide">
          <AnalysisControl v-if="stage === 'analysis'" class="mt-4" :active="hazopRunning" :label="displayLabel"
            :error-message="analysisError" :runs="hazopRuns" :output-folder="outputFolder" :file-name="analysisFileName"
            :process-inputs="systemInputs" :process-outputs="systemOutputs" @start="handleStartAnalysis"
            @exit="handleExit" />
        </Transition>
        <!-- Connections LEGO preview popup -->
        <transition name="fade-slide">
          <div v-if="showConnectionPreview && connectionPreview.length"
            class="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
            <div class="bg-white rounded-2xl shadow-2xl max-w-5xl w-full mx-4 p-6 max-h-[90vh] overflow-y-auto">
              <ConnectionPreview :connections="connectionPreview" @close="showConnectionPreview = false" />
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
