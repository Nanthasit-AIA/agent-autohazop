<script setup lang="ts">
import { computed, nextTick, onBeforeUnmount, onMounted, ref } from "vue";

const { hazopApiBase: API_BASE, demoToken: DEMO_TOKEN } = useRuntimeConfig().public;
const authHeaders = (): Record<string, string> =>
  DEMO_TOKEN ? { "X-Demo-Token": DEMO_TOKEN as string } : {};

type AssistantMode = "ask" | "check" | "improve" | "missing";

interface NodeItem {
  id: string | number;
  name: string;
  range?: string;
  context?: string;
}

interface CurrentDeviation {
  parameter: string;
  guide_word: string;
}

interface AssistantAnswer {
  verdict?: string;
  summary?: string;
  display_markdown?: string;
  key_issues?: string[];
  suggested_fix?: string[];
  risk_logic?: string;
  missing_inputs?: string[];
  next_actions?: string[];
  evidence_notes?: string[];
}

interface ChatMessage {
  id: number;
  role: "user" | "assistant";
  content: string;
  answer?: AssistantAnswer;
  error?: boolean;
}

const attachmentAccept = "";
const maxAttachmentFiles = 4;
const maxAttachmentBytes = 8 * 1024 * 1024;

const props = withDefaults(
  defineProps<{
    apiModel?: string;
    apiProvider?: string;
    enabled?: boolean;
    stage?: string;
    processName?: string;
    fileName?: string | null;
    pidData?: any | null;
    currentNode?: NodeItem | null;
    selectedNodes?: NodeItem[];
    currentDeviations?: CurrentDeviation[];
    systemInputs?: string[];
    systemOutputs?: string[];
    hazopStatus?: Record<string, any> | null;
  }>(),
  {
    enabled: false,
    selectedNodes: () => [],
    currentDeviations: () => [],
    systemInputs: () => [],
    systemOutputs: () => [],
  }
);

const isOpen = ref(false);
const isLoading = ref(false);
const mode = ref<AssistantMode>("ask");
const question = ref("");
const messages = ref<ChatMessage[]>([]);
const messagesRef = ref<HTMLElement | null>(null);
const isFullscreen = ref(false);
const attachedFiles = ref<File[]>([]);
const fileInputRef = ref<HTMLInputElement | null>(null);
const isFileDragging = ref(false);
const fileError = ref("");
const assistantName = "HALO";
const assistantSubtitle = "HAZOP / LOPA assistant";

const modeOptions: { value: AssistantMode; label: string; icon: string }[] = [
  { value: "ask", label: "Ask", icon: "fi fi-br-comment-alt" },
  { value: "check", label: "Check", icon: "fi fi-br-list-check" },
  { value: "improve", label: "Improve", icon: "fi fi-br-magic-wand" },
  { value: "missing", label: "Missing", icon: "fi fi-br-search-alt" },
];

const modePrompt: Record<AssistantMode, string> = {
  ask: "Explain the current HAZOP context and answer my question.",
  check: "Check the current node and selected deviations for HAZOP/LOPA quality.",
  improve: "Improve the wording for the current HAZOP context.",
  missing: "List missing inputs that block a reliable HAZOP/LOPA assessment.",
};

const modeDescriptions: Record<AssistantMode, string> = {
  ask: "General process-safety help grounded in this screen.",
  check: "Review the selected node and deviations as worksheet evidence.",
  improve: "Rewrite wording without inventing plant facts.",
  missing: "Find the data gaps that block a reliable assessment.",
};

interface QuickPrompt {
  label: string;
  mode: AssistantMode;
  prompt: string;
}

const selectedDeviationLabel = computed(() => {
  if (!props.currentDeviations?.length) return "No deviations selected";
  return props.currentDeviations
    .slice(0, 4)
    .map((item) => `${item.parameter} / ${item.guide_word}`)
    .join(", ");
});

const statusLabel = computed(() => {
  if (!props.enabled) return `${assistantName} offline`;
  if (props.currentNode?.name) return props.currentNode.name;
  if (props.selectedNodes.length) return `${props.selectedNodes.length} nodes selected`;
  if (props.pidData) return "PID data loaded";
  return `${assistantName} online`;
});

const activeModeDescription = computed(() => modeDescriptions[mode.value]);

const contextBadges = computed(() => [
  { label: "Stage", value: props.stage || "initial" },
  { label: "Nodes", value: String(props.selectedNodes.length || 0) },
  { label: "Deviations", value: String(props.currentDeviations.length || 0) },
  {
    label: "HAZOP",
    value: props.hazopStatus?.running
      ? "Running"
      : props.hazopStatus?.result?.row_count
        ? `${props.hazopStatus.result.row_count} rows`
        : "No result",
  },
]);

const quickPrompts = computed<QuickPrompt[]>(() => [
  {
    label: "Check row",
    mode: "check",
    prompt: "Check the selected node and deviations. Tell me what is acceptable, what needs revision, and what evidence is missing.",
  },
  {
    label: "Trace consequence",
    mode: "ask",
    prompt: "Trace the likely unmitigated consequence path for this node using the current connection and adjacent lines.",
  },
  {
    label: "Improve wording",
    mode: "improve",
    prompt: "Suggest tighter HAZOP worksheet wording for the current node, deviation, cause, consequence, safeguards, and recommendation.",
  },
  {
    label: "Find gaps",
    mode: "missing",
    prompt: "List the missing inputs that block severity, likelihood, IPL credit, or final risk ranking for this context.",
  },
]);

const canChat = computed(() => props.enabled);
const canSend = computed(() => {
  return canChat.value && !isLoading.value && (question.value.trim().length > 0 || attachedFiles.value.length > 0);
});
const minPanelWidth = 320;
const panelWidth = ref(760);
const isResizing = ref(false);
let previousUserSelect = "";

const clampPanelWidth = (width: number) => {
  if (typeof window === "undefined") {
    return Math.max(width, minPanelWidth);
  }

  const viewportMax = Math.max(minPanelWidth, window.innerWidth);
  return Math.min(Math.max(width, minPanelWidth), viewportMax);
};

const assistantPanelClass = computed(() => {
  if (isFullscreen.value) {
    return "fixed inset-0 z-[60] flex h-screen w-screen flex-col bg-white shadow-2xl";
  }

  return "fixed inset-y-0 right-0 z-[60] flex h-screen flex-col border-l border-gray-200 bg-white shadow-2xl";
});

const assistantPanelStyle = computed<Record<string, string>>(() => {
  if (isFullscreen.value) return {};

  return {
    width: `${panelWidth.value}px`,
    maxWidth: "100vw",
  };
});

const openAssistant = () => {
  isOpen.value = true;
  isFullscreen.value = false;
  panelWidth.value = clampPanelWidth(panelWidth.value);
};

const closeAssistant = () => {
  stopResize();
  isOpen.value = false;
};

const toggleFullscreen = () => {
  stopResize();
  isFullscreen.value = !isFullscreen.value;

  if (!isFullscreen.value) {
    panelWidth.value = clampPanelWidth(panelWidth.value);
  }
};

const startResize = (event: PointerEvent) => {
  if (isFullscreen.value || event.button !== 0) return;

  event.preventDefault();
  isResizing.value = true;
  previousUserSelect = document.body.style.userSelect;
  document.body.style.userSelect = "none";
  window.addEventListener("pointermove", handleResizeMove);
  window.addEventListener("pointerup", stopResize);
};

function handleResizeMove(event: PointerEvent) {
  if (!isResizing.value || typeof window === "undefined") return;

  panelWidth.value = clampPanelWidth(window.innerWidth - event.clientX);
}

function stopResize() {
  if (!isResizing.value) return;

  isResizing.value = false;
  window.removeEventListener("pointermove", handleResizeMove);
  window.removeEventListener("pointerup", stopResize);
  document.body.style.userSelect = previousUserSelect;
}

const handleWindowResize = () => {
  if (!isOpen.value || isFullscreen.value) return;

  panelWidth.value = clampPanelWidth(panelWidth.value);
};

const handleKeydown = (event: KeyboardEvent) => {
  if (event.key === "Escape" && isOpen.value) {
    closeAssistant();
  }
};

onMounted(() => {
  window.addEventListener("keydown", handleKeydown);
  window.addEventListener("resize", handleWindowResize);
});

onBeforeUnmount(() => {
  stopResize();
  window.removeEventListener("keydown", handleKeydown);
  window.removeEventListener("resize", handleWindowResize);
});

const scrollToBottom = async () => {
  await nextTick();
  if (messagesRef.value) {
    messagesRef.value.scrollTop = messagesRef.value.scrollHeight;
  }
};

const answerToText = (answer: AssistantAnswer) => {
  return answer.display_markdown || answer.summary || verdictLabel(answer.verdict) || `${assistantName} response received.`;
};

const normalizeList = (value?: string[]) => {
  if (!Array.isArray(value)) return [];
  return value.filter(Boolean);
};

const formatBytes = (size: number) => {
  if (size >= 1024 * 1024) return `${(size / (1024 * 1024)).toFixed(size >= 10 * 1024 * 1024 ? 0 : 1)} MB`;
  if (size >= 1024) return `${Math.round(size / 1024)} KB`;
  return `${size} B`;
};

const validateAttachment = (file: File) => {
  if (file.size > maxAttachmentBytes) {
    return `${file.name} is larger than 8 MB.`;
  }
  return "";
};

const addAttachmentFiles = (files: FileList | File[]) => {
  fileError.value = "";
  const nextFiles = [...attachedFiles.value];

  for (const file of Array.from(files)) {
    if (nextFiles.length >= maxAttachmentFiles) {
      fileError.value = `Attach up to ${maxAttachmentFiles} files per question.`;
      break;
    }

    const validationError = validateAttachment(file);
    if (validationError) {
      fileError.value = validationError;
      continue;
    }

    const duplicate = nextFiles.some(
      (item) => item.name === file.name && item.size === file.size && item.lastModified === file.lastModified
    );
    if (!duplicate) {
      nextFiles.push(file);
    }
  }

  attachedFiles.value = nextFiles;
};

const openFilePicker = () => {
  if (!canChat.value || isLoading.value) return;
  fileInputRef.value?.click();
};

const handleFileInputChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  if (target.files?.length) {
    addAttachmentFiles(target.files);
  }
  target.value = "";
};

const removeAttachedFile = (index: number) => {
  attachedFiles.value = attachedFiles.value.filter((_, itemIndex) => itemIndex !== index);
  fileError.value = "";
};

const clearAttachments = () => {
  attachedFiles.value = [];
  fileError.value = "";
};

const handleAttachmentDrag = (event: DragEvent) => {
  if (!canChat.value || isLoading.value) return;
  event.preventDefault();
  isFileDragging.value = true;
};

const handleAttachmentDragLeave = (event: DragEvent) => {
  const currentTarget = event.currentTarget as HTMLElement | null;
  if (currentTarget && event.relatedTarget instanceof Node && currentTarget.contains(event.relatedTarget)) {
    return;
  }
  isFileDragging.value = false;
};

const handleAttachmentDrop = (event: DragEvent) => {
  event.preventDefault();
  isFileDragging.value = false;
  if (!canChat.value || isLoading.value) return;

  if (event.dataTransfer?.files?.length) {
    addAttachmentFiles(event.dataTransfer.files);
  }
};

const buildAssistantPayload = (text: string) => ({
  mode: mode.value,
  question: text,
  model: props.apiModel || "",
  provider: props.apiProvider || "",
  pid_data: props.pidData,
  context: {
    process_name: props.processName || "",
    file_name: props.fileName || "",
    stage: props.stage || "",
    current_node: props.currentNode || null,
    current_deviations: props.currentDeviations || [],
    selected_nodes: props.selectedNodes || [],
    system_inputs: props.systemInputs || [],
    system_outputs: props.systemOutputs || [],
    hazop_status: props.hazopStatus || null,
  },
  history: messages.value.slice(-8).map((item) => ({
    role: item.role,
    content: item.answer ? answerToText(item.answer) : item.content,
  })),
});

const sendMessage = async (overrideText?: string) => {
  const text = (overrideText ?? question.value).trim();
  const filesToSend = [...attachedFiles.value];
  const hasAttachments = filesToSend.length > 0;
  const defaultAttachmentQuestion = "ช่วยสรุปและตอบจากไฟล์ที่แนบนี้ โดยตอบเป็นภาษาไทยถ้าไม่ได้ระบุภาษาอื่น";
  const questionText = text || (hasAttachments ? defaultAttachmentQuestion : "");
  if (!questionText || isLoading.value || !canChat.value) return;

  question.value = "";
  const attachmentLines = filesToSend.map((file) => `- ${file.name} (${formatBytes(file.size)})`);
  const userMessage: ChatMessage = {
    id: Date.now(),
    role: "user",
    content: [text || defaultAttachmentQuestion, attachmentLines.length ? `Attached files:\n${attachmentLines.join("\n")}` : ""]
      .filter(Boolean)
      .join("\n\n"),
  };
  messages.value.push(userMessage);
  await scrollToBottom();

  isLoading.value = true;
  try {
    const payload = buildAssistantPayload(questionText);
    const requestOptions: RequestInit = hasAttachments
      ? (() => {
          const formData = new FormData();
          formData.append("payload", JSON.stringify(payload));
          filesToSend.forEach((file) => formData.append("files", file, file.name));
          return { method: "POST", headers: authHeaders(), body: formData };
        })()
      : {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
            ...authHeaders(),
          },
          body: JSON.stringify(payload),
        };

    const res = await fetch(`${API_BASE}/api/assistant/chat`, requestOptions);

    const body = await res.json();
    if (!res.ok || !body.ok) {
      throw new Error(body.error || "Assistant request failed");
    }

    const answer = body.answer as AssistantAnswer;
    messages.value.push({
      id: Date.now() + 1,
      role: "assistant",
      content: answerToText(answer),
      answer,
    });
    clearAttachments();
  } catch (err: any) {
    messages.value.push({
      id: Date.now() + 1,
      role: "assistant",
      content: err?.message || "Assistant request failed",
      error: true,
    });
  } finally {
    isLoading.value = false;
    await scrollToBottom();
  }
};

const runCurrentMode = () => {
  void sendMessage(modePrompt[mode.value]);
};

const sendQuickPrompt = (item: QuickPrompt) => {
  mode.value = item.mode;
  void sendMessage(item.prompt);
};

const modeButtonClass = (item: AssistantMode) => {
  return item === mode.value
    ? "bg-black text-white"
    : "bg-gray-100 text-gray-700 hover:bg-gray-200";
};

const verdictClass = (verdict?: string) => {
  const lower = (verdict || "").toLowerCase();
  if (lower.includes("acceptable")) return "bg-emerald-50 text-emerald-700 border-emerald-200";
  if (lower.includes("revision")) return "bg-amber-50 text-amber-800 border-amber-200";
  if (lower.includes("insufficient")) return "bg-red-50 text-red-700 border-red-200";
  return "bg-sky-50 text-sky-700 border-sky-200";
};

const verdictLabel = (verdict?: string) => {
  const value = (verdict || "").trim();
  if (!value) return "";
  return value.toLowerCase() === "advisory" ? assistantName : value;
};

const escapeHtml = (value: string) => {
  return value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
};

const renderInlineMarkdown = (value: string) => {
  return escapeHtml(value)
    .replace(/`([^`]+)`/g, "<code>$1</code>")
    .replace(/\*\*([^*]+)\*\*/g, "<strong>$1</strong>")
    .replace(/\*([^*]+)\*/g, "<em>$1</em>")
    .replace(
      /\[([^\]]+)\]\((https?:\/\/[^\s)]+)\)/g,
      '<a href="$2" target="_blank" rel="noopener noreferrer">$1</a>'
    );
};

const splitTableCells = (line: string) => {
  return line
    .trim()
    .replace(/^\|/, "")
    .replace(/\|$/, "")
    .split("|")
    .map((cell) => cell.trim());
};

const isTableSeparator = (line: string) => {
  const cells = splitTableCells(line);
  return cells.length > 1 && cells.every((cell) => /^:?-{3,}:?$/.test(cell));
};

const renderMarkdown = (markdown: string) => {
  const lines = (markdown || "").replace(/\r\n/g, "\n").split("\n");
  const html: string[] = [];
  let paragraph: string[] = [];
  let listItems: string[] = [];
  let orderedItems: string[] = [];
  let tableRows: string[] = [];
  let codeLines: string[] = [];
  let inCodeBlock = false;

  const flushParagraph = () => {
    if (!paragraph.length) return;
    html.push(`<p>${paragraph.map((line) => renderInlineMarkdown(line)).join("<br>")}</p>`);
    paragraph = [];
  };

  const flushList = () => {
    if (listItems.length) {
      html.push(`<ul>${listItems.map((item) => `<li>${renderInlineMarkdown(item)}</li>`).join("")}</ul>`);
      listItems = [];
    }
    if (orderedItems.length) {
      html.push(`<ol>${orderedItems.map((item) => `<li>${renderInlineMarkdown(item)}</li>`).join("")}</ol>`);
      orderedItems = [];
    }
  };

  const flushTable = () => {
    if (!tableRows.length) return;
    const rows = tableRows.map(splitTableCells);
    const hasHeader = rows.length >= 2 && isTableSeparator(tableRows[1]);
    const bodyRows = hasHeader ? rows.slice(2) : rows;
    const headerHtml = hasHeader
      ? `<thead><tr>${rows[0].map((cell) => `<th>${renderInlineMarkdown(cell)}</th>`).join("")}</tr></thead>`
      : "";
    const bodyHtml = `<tbody>${bodyRows
      .map((row) => `<tr>${row.map((cell) => `<td>${renderInlineMarkdown(cell)}</td>`).join("")}</tr>`)
      .join("")}</tbody>`;
    html.push(`<div class="assistant-table-wrap"><table>${headerHtml}${bodyHtml}</table></div>`);
    tableRows = [];
  };

  const flushCode = () => {
    if (!codeLines.length) return;
    html.push(`<pre><code>${escapeHtml(codeLines.join("\n"))}</code></pre>`);
    codeLines = [];
  };

  for (const rawLine of lines) {
    const line = rawLine.trimEnd();
    const trimmed = line.trim();

    if (trimmed.startsWith("```")) {
      if (inCodeBlock) {
        flushCode();
        inCodeBlock = false;
      } else {
        flushParagraph();
        flushList();
        flushTable();
        inCodeBlock = true;
      }
      continue;
    }

    if (inCodeBlock) {
      codeLines.push(rawLine);
      continue;
    }

    if (!trimmed) {
      flushParagraph();
      flushList();
      flushTable();
      continue;
    }

    const headingMatch = trimmed.match(/^(#{1,3})\s+(.+)$/);
    if (headingMatch) {
      flushParagraph();
      flushList();
      flushTable();
      const level = headingMatch[1].length + 2;
      html.push(`<h${level}>${renderInlineMarkdown(headingMatch[2])}</h${level}>`);
      continue;
    }

    if (trimmed.includes("|") && splitTableCells(trimmed).length > 1) {
      flushParagraph();
      flushList();
      tableRows.push(trimmed);
      continue;
    }

    flushTable();

    const bulletMatch = trimmed.match(/^[-*]\s+(.+)$/);
    if (bulletMatch) {
      flushParagraph();
      orderedItems = [];
      listItems.push(bulletMatch[1]);
      continue;
    }

    const orderedMatch = trimmed.match(/^\d+\.\s+(.+)$/);
    if (orderedMatch) {
      flushParagraph();
      listItems = [];
      orderedItems.push(orderedMatch[1]);
      continue;
    }

    flushList();
    paragraph.push(trimmed);
  }

  flushParagraph();
  flushList();
  flushTable();
  if (inCodeBlock) flushCode();

  return html.join("");
};

const answerMarkdown = (answer: AssistantAnswer) => {
  return answer.display_markdown || answer.summary || verdictLabel(answer.verdict) || `${assistantName} response received.`;
};

const hasStructuredDetails = (answer: AssistantAnswer) => {
  return Boolean(
    normalizeList(answer.key_issues).length ||
      normalizeList(answer.suggested_fix).length ||
      answer.risk_logic ||
      normalizeList(answer.missing_inputs).length ||
      normalizeList(answer.next_actions).length ||
      normalizeList(answer.evidence_notes).length
  );
};
</script>

<template>
  <button
    v-if="!isOpen"
    type="button"
    class="fixed right-6 bottom-8 z-[44] inline-flex h-16 items-center gap-3 rounded-full border border-gray-200 bg-white px-7 text-lg font-black text-gray-900 shadow-xl transition hover:-translate-y-0.5 hover:shadow-2xl disabled:cursor-not-allowed disabled:opacity-60"
    :disabled="!enabled"
    title="Open HALO"
    @click="openAssistant"
  >
    <span class="halo-chat-launch-icon" aria-hidden="true">
      <i class="fi fi-br-comment-alt flex items-center justify-center" />
    </span>
    <span>HALO</span>
  </button>

  <Transition name="assistant-drawer">
    <aside
      v-if="isOpen"
      :class="assistantPanelClass"
      :style="assistantPanelStyle"
      role="dialog"
      :aria-label="assistantName"
    >
      <button
        v-if="!isFullscreen"
        type="button"
        class="absolute inset-y-0 left-0 z-10 w-3 cursor-ew-resize touch-none border-0 bg-transparent p-0 transition hover:bg-gray-200/60 focus:outline-none focus-visible:ring-2 focus-visible:ring-gray-500"
        title="Drag to resize assistant"
        aria-label="Resize assistant"
        @pointerdown="startResize"
      >
        <span class="pointer-events-none absolute left-1 top-1/2 h-16 w-0.5 -translate-y-1/2 rounded-full bg-gray-300" />
      </button>

      <header class="border-b border-gray-200 px-4 py-4 sm:px-6">
        <div class="mx-auto flex w-full max-w-5xl items-start justify-between gap-4">
          <div class="min-w-0">
            <div class="flex items-center gap-5">
              <div class="min-w-0">
                <h2 class="halo-wordmark halo-title">{{ assistantName }}</h2>
                <p class="truncate text-sm font-semibold text-gray-500">
                  {{ assistantSubtitle }}
                </p>
                <p class="mt-0.5 text-xs font-medium text-gray-400">
                  {{ statusLabel }} · {{ activeModeDescription }}
                </p>
              </div>
            </div>
          </div>

          <div class="flex shrink-0 items-center gap-2" data-assistant-control>

            <button
              type="button"
              class="flex h-10 w-10 items-center justify-center rounded-lg border border-gray-200 bg-white text-gray-700 shadow-sm transition hover:bg-gray-50"
              :title="isFullscreen ? 'Exit full screen' : 'Full screen'"
              :aria-label="isFullscreen ? 'Exit full screen' : 'Open full screen'"
              @click="toggleFullscreen"
            >
              <i
                :class="isFullscreen ? 'fi fi-br-compress-alt' : 'fi fi-br-expand'"
                class="flex items-center justify-center text-base"
              />
            </button>
            <button
              type="button"
              class="inline-flex h-10 items-center justify-center gap-1 rounded-lg border border-gray-200 bg-white px-3 text-sm font-black text-gray-700 shadow-sm transition hover:bg-gray-50"
              title="Close"
              :aria-label="`Close ${assistantName}`"
              @click="closeAssistant"
            >
              <i class="fi fi-br-cross-small flex items-center justify-center text-lg" />
              <span>Close</span>
            </button>
          </div>
        </div>

        <div class="mx-auto mt-4 grid w-full max-w-5xl grid-cols-4 gap-2">
          <button
            v-for="item in modeOptions"
            :key="item.value"
            type="button"
            class="flex h-10 items-center justify-center gap-1 rounded-lg text-sm font-black transition"
            :class="modeButtonClass(item.value)"
            :title="item.label"
            @click="mode = item.value"
          >
            <i :class="item.icon" class="flex items-center justify-center text-sm" />
            <span>{{ item.label }}</span>
          </button>
        </div>
      </header>

      <section class="border-b border-gray-100 bg-gray-50 px-4 py-3 sm:px-6">
        <div class="mx-auto w-full max-w-5xl space-y-3 text-sm">
          <div class="grid gap-2 sm:grid-cols-2 sm:gap-4">
            <div class="flex items-start justify-between gap-3">
              <span class="font-black text-gray-500">Node</span>
              <span class="text-right font-semibold text-gray-800">
                {{ currentNode?.name || "Not selected" }}
              </span>
            </div>
            <div class="flex items-start justify-between gap-3">
              <span class="font-black text-gray-500">Deviation</span>
              <span class="text-right text-gray-700">
                {{ selectedDeviationLabel }}
              </span>
            </div>
          </div>
          <div class="flex flex-wrap gap-2">
            <span
              v-for="badge in contextBadges"
              :key="badge.label"
              class="inline-flex items-center gap-1 rounded-md border border-gray-200 bg-white px-2 py-1 font-semibold text-gray-600"
            >
              <span class="text-gray-400">{{ badge.label }}</span>
              <span class="text-gray-800">{{ badge.value }}</span>
            </span>
          </div>
        </div>
      </section>

      <div ref="messagesRef" class="mx-auto w-full max-w-5xl flex-1 overflow-y-auto px-4 py-5 sm:px-6">
        <div v-if="messages.length === 0" class="mt-10 text-center">
          <p class="text-base font-semibold text-gray-700">
            {{ enabled ? `${assistantName} ready` : `${assistantName} offline` }}
          </p>
          <div v-if="enabled" class="mx-auto mt-5 grid max-w-xl gap-2 sm:grid-cols-2">
            <button
              v-for="item in quickPrompts"
              :key="item.label"
              type="button"
              class="rounded-lg border border-gray-200 bg-white px-3 py-2 text-left text-sm font-black text-gray-700 shadow-sm transition hover:border-gray-300 hover:bg-gray-50 disabled:cursor-not-allowed disabled:opacity-50"
              :disabled="isLoading"
              @click="sendQuickPrompt(item)"
            >
              {{ item.label }}
            </button>
          </div>
        </div>

        <div v-for="message in messages" :key="message.id" class="mb-4 flex" :class="message.role === 'user' ? 'justify-end' : 'justify-start'">
          <div
            class="max-w-[88%] rounded-xl px-4 py-3 text-base leading-relaxed"
            :class="message.role === 'user'
              ? 'bg-black text-white'
              : message.error
                ? 'border border-red-200 bg-red-50 text-red-700'
                : 'border border-gray-200 bg-white text-gray-800 shadow-sm'"
          >
            <template v-if="message.answer">
              <div
                v-if="message.answer.verdict"
                class="mb-2 inline-flex rounded-full border px-2 py-0.5 text-xs font-black"
                :class="verdictClass(message.answer.verdict)"
              >
                {{ verdictLabel(message.answer.verdict) }}
              </div>

              <div class="assistant-markdown" v-html="renderMarkdown(answerMarkdown(message.answer))" />

              <details v-if="hasStructuredDetails(message.answer)" class="mt-3 border-t border-gray-100 pt-2">
                <summary class="cursor-pointer text-xs font-black text-gray-500">Structured notes</summary>

                <div v-if="normalizeList(message.answer.key_issues).length" class="mt-3">
                  <div class="mb-1 text-sm font-black text-gray-500">Key Issues</div>
                  <ul class="list-disc space-y-1 pl-5">
                    <li v-for="item in normalizeList(message.answer.key_issues)" :key="item" class="text-sm">
                      {{ item }}
                    </li>
                  </ul>
                </div>

                <div v-if="normalizeList(message.answer.suggested_fix).length" class="mt-3">
                  <div class="mb-1 text-sm font-black text-gray-500">Suggested Fix</div>
                  <ul class="list-disc space-y-1 pl-5">
                    <li v-for="item in normalizeList(message.answer.suggested_fix)" :key="item" class="text-sm">
                      {{ item }}
                    </li>
                  </ul>
                </div>

                <div v-if="message.answer.risk_logic" class="mt-3">
                  <div class="mb-1 text-sm font-black text-gray-500">Risk Logic</div>
                  <p class="text-sm">{{ message.answer.risk_logic }}</p>
                </div>

                <div v-if="normalizeList(message.answer.missing_inputs).length" class="mt-3">
                  <div class="mb-1 text-sm font-black text-gray-500">Missing Inputs</div>
                  <ul class="list-disc space-y-1 pl-5">
                    <li v-for="item in normalizeList(message.answer.missing_inputs)" :key="item" class="text-sm">
                      {{ item }}
                    </li>
                  </ul>
                </div>

                <div v-if="normalizeList(message.answer.next_actions).length" class="mt-3">
                  <div class="mb-1 text-sm font-black text-gray-500">Next Actions</div>
                  <ul class="list-disc space-y-1 pl-5">
                    <li v-for="item in normalizeList(message.answer.next_actions)" :key="item" class="text-sm">
                      {{ item }}
                    </li>
                  </ul>
                </div>

                <div v-if="normalizeList(message.answer.evidence_notes).length" class="mt-3">
                  <div class="mb-1 text-sm font-black text-gray-500">Evidence Notes</div>
                  <ul class="list-disc space-y-1 pl-5">
                    <li v-for="item in normalizeList(message.answer.evidence_notes)" :key="item" class="text-xs text-gray-500">
                      {{ item }}
                    </li>
                  </ul>
                </div>
              </details>
            </template>

            <template v-else>
              <div class="whitespace-pre-wrap">{{ message.content }}</div>
            </template>
          </div>
        </div>

        <div v-if="isLoading" class="flex justify-start">
          <div class="inline-flex items-center gap-2 rounded-xl border border-gray-200 bg-white px-4 py-3 text-base text-gray-600 shadow-sm">
            <span class="h-2 w-2 animate-pulse rounded-full bg-sky-500" />
            Thinking
          </div>
        </div>
      </div>

      <footer class="border-t border-gray-200 bg-white px-4 py-4 sm:px-6">
        <div class="mx-auto w-full max-w-5xl">
          <div class="mb-3 flex gap-2">
            <button
              type="button"
              class="inline-flex flex-1 items-center justify-center gap-2 rounded-lg border border-gray-300 bg-white px-3 py-2 text-sm font-black text-gray-700 transition hover:bg-gray-50 disabled:cursor-not-allowed disabled:opacity-50"
              :disabled="!canChat || isLoading"
              @click="runCurrentMode"
            >
              <i class="fi fi-br-play flex items-center justify-center text-xs" />
              <span>Run {{ modeOptions.find((item) => item.value === mode)?.label }}</span>
            </button>
          </div>

          <div
            class="mb-3 rounded-lg border border-dashed px-3 py-2 transition"
            :class="isFileDragging ? 'border-black bg-gray-50' : 'border-gray-300 bg-white'"
            @click="openFilePicker"
            @dragenter="handleAttachmentDrag"
            @dragover="handleAttachmentDrag"
            @dragleave="handleAttachmentDragLeave"
            @drop="handleAttachmentDrop"
          >
            <input
              ref="fileInputRef"
              class="hidden"
              type="file"
              multiple
              :accept="attachmentAccept"
              :disabled="!canChat || isLoading"
              @change="handleFileInputChange"
            />
            <div class="flex items-center gap-3">
              <div class="flex h-9 w-9 shrink-0 items-center justify-center rounded-lg bg-gray-100 text-gray-600">
                <i class="fi fi-br-clip flex items-center justify-center text-sm" />
              </div>
              <div class="min-w-0 flex-1">
                <div class="truncate text-sm font-black text-gray-800">Files for this question</div>
                <div class="truncate text-xs font-semibold text-gray-500">Any file type, up to 8 MB each</div>
              </div>
              <button
                type="button"
                class="shrink-0 rounded-lg border border-gray-200 bg-white px-3 py-1.5 text-xs font-black text-gray-700 transition hover:bg-gray-50 disabled:cursor-not-allowed disabled:opacity-50"
                :disabled="!canChat || isLoading"
                @click.stop="openFilePicker"
              >
                Browse
              </button>
            </div>
          </div>

          <div v-if="attachedFiles.length" class="mb-3 flex flex-wrap gap-2">
            <span
              v-for="(file, index) in attachedFiles"
              :key="`${file.name}-${file.size}-${file.lastModified}`"
              class="inline-flex max-w-full items-center gap-2 rounded-lg border border-gray-200 bg-gray-50 px-2 py-1 text-xs font-semibold text-gray-700"
            >
              <i class="fi fi-br-document flex shrink-0 items-center justify-center text-[11px] text-gray-500" />
              <span class="max-w-52 truncate">{{ file.name }}</span>
              <span class="shrink-0 text-gray-400">{{ formatBytes(file.size) }}</span>
              <button
                type="button"
                class="flex h-5 w-5 shrink-0 items-center justify-center rounded-md text-gray-500 transition hover:bg-gray-200 hover:text-gray-800"
                title="Remove file"
                :disabled="isLoading"
                @click.stop="removeAttachedFile(index)"
              >
                <i class="fi fi-br-cross-small flex items-center justify-center text-sm" />
              </button>
            </span>
            <button
              type="button"
              class="rounded-lg px-2 py-1 text-xs font-black text-gray-500 transition hover:bg-gray-100 hover:text-gray-800 disabled:cursor-not-allowed disabled:opacity-50"
              :disabled="isLoading"
              @click="clearAttachments"
            >
              Clear
            </button>
          </div>

          <p v-if="fileError" class="mb-3 text-xs font-semibold text-red-600">
            {{ fileError }}
          </p>

          <div class="flex items-end gap-2">
            <textarea
              v-model="question"
              rows="2"
              class="max-h-36 min-h-14 flex-1 resize-none rounded-lg border border-gray-300 px-3 py-2 text-base outline-none transition focus:border-gray-500"
              placeholder="Ask about this HAZOP context"
              :disabled="!canChat || isLoading"
              @keydown.enter.exact.prevent="sendMessage()"
            />
            <button
              type="button"
              class="flex h-12 w-12 items-center justify-center rounded-lg bg-black text-white transition hover:bg-gray-800 disabled:cursor-not-allowed disabled:opacity-50"
              title="Send"
              :disabled="!canSend"
              @click="sendMessage()"
            >
              <i class="fi fi-br-paper-plane flex items-center justify-center text-sm" />
            </button>
          </div>
        </div>
      </footer>
    </aside>
  </Transition>
</template>

<style scoped>
.halo-chat-launch-icon {
  display: inline-flex;
  width: 2.35rem;
  height: 2.35rem;
  flex: 0 0 2.35rem;
  align-items: center;
  justify-content: center;
  border-radius: 9999px;
  background: #111827;
  color: #fff;
  font-size: 1.05rem;
  box-shadow: 0 10px 18px rgba(15, 23, 42, 0.2);
}

.halo-emblem-frame,
.halo-empty-emblem {
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: visible;
  border: 0;
  background: transparent;
  box-shadow: none;
}

.halo-emblem-frame {
  width: 5rem;
  height: 5rem;
  flex: 0 0 5rem;
  border-radius: 9999px;
}

.halo-empty-emblem {
  width: 7rem;
  height: 7rem;
  border-radius: 9999px;
}

.halo-emblem-frame::after,
.halo-empty-emblem::after {
  display: none;
}

.halo-emblem {
  position: relative;
  z-index: 1;
  width: 100%;
  height: 100%;
  border-radius: 9999px;
  object-fit: cover;
  filter: drop-shadow(0 14px 24px rgba(154, 92, 10, 0.24));
}

.halo-emblem-frame .halo-emblem {
  width: 8.5rem;
  height: 8.5rem;
  max-width: none;
  flex: 0 0 auto;
}

.halo-wordmark {
  font-family: "Trajan Pro", "Cinzel", "Copperplate Gothic Light", "Constantia", "Times New Roman", serif;
  font-variant: small-caps;
  font-weight: 700;
  letter-spacing: 0;
  line-height: 1;
  text-transform: uppercase;
}

.halo-title {
  position: relative;
  display: inline-flex;
  align-items: center;
  color: #0f172a;
  font-size: 1.42rem;
  text-shadow: 0 1px 0 #fff, 0 10px 24px rgba(15, 23, 42, 0.12);
}

.halo-title::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0.08rem;
  bottom: -0.26rem;
  height: 1px;
  background: linear-gradient(90deg, rgba(15, 23, 42, 0.85), rgba(148, 163, 184, 0.24));
}

.halo-chip {
  font-size: 1.18rem;
}

.assistant-drawer-enter-active,
.assistant-drawer-leave-active {
  transition: opacity 0.18s ease, transform 0.18s ease;
}

.assistant-drawer-enter-from,
.assistant-drawer-leave-to {
  opacity: 0;
  transform: translateX(100%);
}

.assistant-markdown {
  color: #1f2937;
  line-height: 1.65;
}

.assistant-markdown :deep(p) {
  margin: 0.35rem 0 0;
}

.assistant-markdown :deep(p:first-child) {
  margin-top: 0;
}

.assistant-markdown :deep(h3),
.assistant-markdown :deep(h4),
.assistant-markdown :deep(h5) {
  margin: 0.9rem 0 0.35rem;
  color: #111827;
  font-weight: 900;
  line-height: 1.25;
}

.assistant-markdown :deep(h3) {
  font-size: 1.02rem;
}

.assistant-markdown :deep(h4),
.assistant-markdown :deep(h5) {
  font-size: 0.95rem;
}

.assistant-markdown :deep(ul),
.assistant-markdown :deep(ol) {
  margin: 0.45rem 0 0;
  padding-left: 1.25rem;
}

.assistant-markdown :deep(ul) {
  list-style: disc;
}

.assistant-markdown :deep(ol) {
  list-style: decimal;
}

.assistant-markdown :deep(li) {
  margin: 0.2rem 0;
  padding-left: 0.1rem;
}

.assistant-markdown :deep(strong) {
  color: #111827;
  font-weight: 900;
}

.assistant-markdown :deep(code) {
  border-radius: 0.35rem;
  background: #f3f4f6;
  padding: 0.05rem 0.28rem;
  color: #111827;
  font-size: 0.9em;
  font-weight: 700;
}

.assistant-markdown :deep(pre) {
  margin: 0.65rem 0 0;
  overflow-x: auto;
  border-radius: 0.55rem;
  background: #111827;
  padding: 0.75rem;
  color: #f9fafb;
}

.assistant-markdown :deep(pre code) {
  background: transparent;
  padding: 0;
  color: inherit;
  font-weight: 500;
}

.assistant-markdown :deep(a) {
  color: #0369a1;
  font-weight: 800;
  text-decoration: underline;
  text-underline-offset: 2px;
}

.assistant-markdown :deep(.assistant-table-wrap) {
  margin-top: 0.65rem;
  overflow-x: auto;
  border-radius: 0.55rem;
  border: 1px solid #e5e7eb;
}

.assistant-markdown :deep(table) {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.88rem;
}

.assistant-markdown :deep(th),
.assistant-markdown :deep(td) {
  border-bottom: 1px solid #e5e7eb;
  padding: 0.48rem 0.6rem;
  text-align: left;
  vertical-align: top;
}

.assistant-markdown :deep(th) {
  background: #f9fafb;
  color: #374151;
  font-weight: 900;
}

.assistant-markdown :deep(tr:last-child td) {
  border-bottom: 0;
}
</style>

