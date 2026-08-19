<script setup lang="ts">
import { ref, watch, onMounted, computed } from "vue";

const API_BASE = "http://localhost:5000";

const props = defineProps<{
  disabled?: boolean;
  jsonFileName?: string | null;
  prefillInstruction?: string;
  openTrigger?: number;
}>();

const emit = defineEmits<{
  (e: "call-hazop"): void;
  (e: "exit"): void;
  (e: "modify-done", payload: { data: any; fileName: string }): void;
}>();

/* ---- LLM config (same as ProcessInput) ---- */
interface LLMGroup { id: string; label: string; models: string[] }
const llmGroups = ref<LLMGroup[]>([]);
const llmProvider = ref("own_api");
const llmModel = ref("");
const currentModels = computed<string[]>(() => llmGroups.value.find(g => g.id === llmProvider.value)?.models ?? []);

onMounted(async () => {
  try {
    const res = await fetch(`${API_BASE}/api/llm-config`);
    const data = await res.json();
    llmGroups.value = data.groups ?? [];
    llmProvider.value = llmGroups.value[0]?.id ?? "";
    llmModel.value = llmGroups.value[0]?.models[0] ?? "";
  } catch { /* backend may not be running yet */ }
});

const onProviderChange = (id: string) => {
  llmProvider.value = id;
  llmModel.value = llmGroups.value.find(g => g.id === id)?.models[0] ?? "";
};

/* ---- Modify modal state ---- */
const modifyOpen = ref(false);
const instruction = ref("");
const modifyFile = ref<File | null>(null);
const modifyFileRef = ref<HTMLInputElement | null>(null);
const modifyError = ref("");
const modifyLoading = ref(false);

const openModify = (prefill = "") => {
  instruction.value = prefill;
  modifyError.value = "";
  modifyFile.value = null;
  modifyOpen.value = true;
};

// Called from index.vue via openTrigger prop
watch(() => props.openTrigger, (ts) => {
  if (ts && ts > 0) openModify(props.prefillInstruction ?? "");
});

const closeModify = () => { modifyOpen.value = false; };

const handleModifyFileChange = (e: Event) => {
  const f = (e.target as HTMLInputElement).files?.[0] ?? null;
  modifyFile.value = f;
};

const submitModify = async () => {
  if (!instruction.value.trim()) { modifyError.value = "Instruction is required."; return; }
  if (!props.jsonFileName) { modifyError.value = "No file loaded."; return; }

  const baseName = props.jsonFileName.endsWith(".json")
    ? props.jsonFileName.slice(0, -5)
    : props.jsonFileName;

  modifyLoading.value = true;
  modifyError.value = "";

  try {
    const form = new FormData();
    form.append("file_name", baseName);
    form.append("instruction", instruction.value.trim());
    form.append("llm_provider", llmProvider.value);
    if (llmModel.value) form.append("llm_model", llmModel.value);
    if (modifyFile.value) form.append("file", modifyFile.value);

    const res = await fetch(`${API_BASE}/api/modify`, { method: "POST", body: form });
    const body = await res.json();

    if (!res.ok || !body.ok) {
      modifyError.value = body.error || "Modify failed.";
      return;
    }

    emit("modify-done", { data: body.data, fileName: body.file_name });
    closeModify();
  } catch (err) {
    modifyError.value = "Network error.";
  } finally {
    modifyLoading.value = false;
  }
};
</script>

<template>
  <div>
    <div class="flex gap-3 justify-center mb-8">
      <button
        @click="emit('call-hazop')"
        :disabled="disabled"
        class="px-6 py-2 rounded-lg transition"
        :class="disabled ? 'bg-gray-300 text-gray-500 cursor-not-allowed' : 'bg-black text-white hover:bg-gray-800'"
      >
        Call to HAZOP analysis
      </button>

      <button
        @click="openModify()"
        :disabled="!jsonFileName"
        class="px-6 py-2 rounded-lg border transition"
        :class="!jsonFileName ? 'border-gray-200 text-gray-400 cursor-not-allowed' : 'border-gray-400 text-gray-700 hover:bg-gray-50'"
      >
        Modify / Fix JSON
      </button>

      <button
        @click="emit('exit')"
        class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition"
      >
        exit
      </button>
    </div>

    <!-- Modify modal -->
    <Transition name="fade">
      <div
        v-if="modifyOpen"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/40"
        @click.self="closeModify"
      >
        <div class="bg-white rounded-2xl shadow-2xl w-full max-w-xl p-6">
          <div class="flex items-center justify-between mb-4">
            <h3 class="text-base font-bold text-gray-800">Modify / Fix JSON</h3>
            <button
              @click="closeModify"
              class="w-8 h-8 rounded-full bg-gray-100 flex items-center justify-center hover:bg-gray-200 transition"
            >
              <span class="text-sm font-bold text-gray-600">×</span>
            </button>
          </div>

          <!-- Instruction -->
          <label class="text-xs text-gray-500 mb-1 block">Modification instruction *</label>
          <textarea
            v-model="instruction"
            rows="4"
            placeholder="Describe what to fix or change, e.g. 'FV-002 should be a level control valve, not flow control'"
            class="w-full border border-gray-300 rounded-lg px-3 py-2 text-sm mb-3 resize-none focus:outline-none focus:ring-1 focus:ring-gray-400"
          ></textarea>

          <!-- Optional file -->
          <label class="text-xs text-gray-500 mb-1 block">Optional file (extra P&ID sheet, spec, marked-up image)</label>
          <div class="flex items-center gap-2 mb-4">
            <input ref="modifyFileRef" type="file" class="hidden" accept="application/pdf,image/*" @change="handleModifyFileChange" />
            <button
              @click="modifyFileRef?.click()"
              class="px-3 py-1.5 text-xs border border-gray-300 rounded-lg hover:bg-gray-50 transition"
            >
              {{ modifyFile ? modifyFile.name : "Choose file…" }}
            </button>
            <button v-if="modifyFile" @click="modifyFile = null" class="text-xs text-gray-400 hover:text-gray-600">✕</button>
          </div>

          <!-- Model selector -->
          <div v-if="llmGroups.length" class="flex items-center gap-2 mb-4 flex-wrap">
            <button
              v-for="group in llmGroups"
              :key="group.id"
              @click="onProviderChange(group.id)"
              class="px-3 py-1 rounded-full text-xs font-medium transition"
              :class="llmProvider === group.id ? 'bg-black text-white' : 'bg-gray-100 text-gray-600 hover:bg-gray-200'"
            >
              {{ group.label }}
            </button>
            <select
              v-if="currentModels.length"
              v-model="llmModel"
              class="ml-1 bg-white border border-gray-300 text-gray-700 text-xs rounded-lg px-2 py-1"
            >
              <option v-for="m in currentModels" :key="m" :value="m">{{ m }}</option>
            </select>
          </div>

          <!-- Error -->
          <p v-if="modifyError" class="text-xs text-red-600 mb-3">{{ modifyError }}</p>

          <!-- Submit -->
          <div class="flex justify-end gap-2">
            <button @click="closeModify" class="px-4 py-2 text-sm border border-gray-300 rounded-lg hover:bg-gray-50 transition">
              Cancel
            </button>
            <button
              @click="submitModify"
              :disabled="modifyLoading"
              class="px-4 py-2 text-sm rounded-lg text-white transition"
              :class="modifyLoading ? 'bg-gray-400 cursor-not-allowed' : 'bg-black hover:bg-gray-800'"
            >
              {{ modifyLoading ? "Applying…" : "Apply" }}
            </button>
          </div>
        </div>
      </div>
    </Transition>
  </div>
</template>

<style scoped>
.fade-enter-active, .fade-leave-active { transition: opacity 0.2s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }
</style>
