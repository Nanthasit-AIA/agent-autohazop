<script setup lang="ts">
import { ref, toRefs } from "vue";

const locked = ref(false);
const props = withDefaults(
  defineProps<{
    name: string;
    description: string;
    mode: "full" | "search";
    busy?: boolean;
  }>(),
  {
    busy: false,
  }
);

const { name, description, mode, busy } = toRefs(props);

const emit = defineEmits<{
  (e: "update:name", value: string): void;
  (e: "update:description", value: string): void;
  (e: "update:file", file: File | null): void;
  (
    e: "start-extract",
    payload:
      | {
          mode: "full";
          name: string;
          description: string;
          file: File | null;
          fileName: string | null;
          files: File[];
        }
      | { mode: "search"; name: string }
  ): void;
}>();

const fileInputRef = ref<HTMLInputElement | null>(null);

/* ------------------------------
   MULTI FILE SUPPORT
------------------------------ */
const selectedFiles = ref<File[]>([]);

const handleFileButtonClick = () => {
  if (busy.value) return;
  fileInputRef.value?.click();
};

const handleNameInput = (event: Event) => {
  emit("update:name", (event.target as HTMLInputElement).value);
};

const handleDescriptionInput = (event: Event) => {
  emit("update:description", (event.target as HTMLTextAreaElement).value);
};

/* -------------------------
    ON FILE CHANGE
--------------------------*/
const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const files = target.files;

  if (!files) return;

  for (const f of files) {
    selectedFiles.value.push(f);
  }

  // always emit the *first* file like old system
  emit("update:file", selectedFiles.value[0] ?? null);

  target.value = "";
};

/* -------------------------
    REMOVE FILE CHIP
--------------------------*/
const removeFile = (i: number) => {
  selectedFiles.value.splice(i, 1);

  // update extract main file
  emit("update:file", selectedFiles.value[0] ?? null);
};

/* -------------------------
    EXTRACT
--------------------------*/
const handleStartExtract = () => {
  if (busy.value) return;
  locked.value = true;

  const firstFile = selectedFiles.value[0] || null;

  emit("start-extract", {
    mode: "full",
    name: name.value,
    description: description.value,
    file: firstFile,
    fileName: firstFile ? firstFile.name : null,
    files: [...selectedFiles.value],
  });
};

const handleSearchMode = () => {
  if (busy.value) return;
  locked.value = true;

  emit("start-extract", {
    mode: "search",
    name: name.value,
  });
};

/* -------------------------
    CHIP COLOR + LABEL
--------------------------*/
const fileType = (file: File): string => {
  const ext = file.name.split(".").pop()?.toLowerCase() ?? "";

  if (ext === "pdf") return "PDF";
  if (["jpg", "jpeg"].includes(ext)) return "JPG";
  if (ext === "png") return "PNG";

  return ext ? ext.toUpperCase() : "FILE";
};

const fileColor = (file: File): string => {
  const ext = file.name.split(".").pop()?.toLowerCase() ?? ""; //

  if (ext === "pdf") return "bg-red-600";
  if (["jpg", "jpeg", "png"].includes(ext)) return "bg-blue-600";

  return "bg-gray-600";
};
</script>

<template>
  <!-- Transition between full/search layouts -->
  <Transition name="mode-fade" mode="out-in">
    <div :key="mode" class="max-w-6xl mx-auto">
      <!-- MODE: full (Start-new-process button) -->
      <div
        v-if="mode === 'full'"
        class="bg-gray-200 rounded-2xl p-6 mb-6 relative"
      >
        <div class="flex items-center gap-3 mb-4 mt-3 jusitfy-center">
          <!-- File Add Button -->
          <button
            @click="handleFileButtonClick"
            :disabled="locked"
            class="w-8 h-8 rounded-full flex items-center justify-center transition"
            :class="
              locked
                ? 'bg-gray-400 cursor-not-allowed opacity-60'
                : 'bg-black text-white hover:bg-gray-800'
            "
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
              <line x1="12" y1="5" x2="12" y2="19" />
              <line x1="5" y1="12" x2="19" y2="12" />
            </svg>
          </button>

          <!-- Name -->
          <input
            type="text"
            placeholder="type name"
            :value="name"
            @input="handleNameInput"
            :disabled="locked"
            class="bg-black text-white px-4 py-2 rounded-lg w-60 max-w-full md:max-w-xl transition disabled:opacity-60 disabled:cursor-not-allowed"
            :style="{
              width:
                name && name.length > 0
                  ? `max(${240}px, ${name.length * 12 + 60}px)`
                  : undefined,
            }"
          />
        </div>

        <!-- 🌟 NEW: FILE CHIPS -->
        <div class="flex flex-wrap gap-3 mb-4 ml-2">
          <div
            v-for="(file, i) in selectedFiles"
            :key="i"
            class="flex items-center gap-3 px-4 py-3 rounded-xl text-white shadow relative min-w-[200px]"
            :class="fileColor(file)"
          >
            <div class="text-2xl">📄</div>

            <div class="flex flex-col">
              <span class="font-medium truncate max-w-[120px]">
                {{ file.name }}</span
              >
              <span class="text-xs opacity-80">{{ fileType(file) }}</span>
            </div>

            <button
              @click="removeFile(i)"
              class="absolute top-2 right-2 text-white hover:text-gray-200"
            >
              ✕
            </button>
          </div>
        </div>

        <div class="flex items-start gap-3">
          <textarea
            placeholder="type about process description"
            :value="description"
            :disabled="locked"
            rows="1"
            class="bg-gray-200 px-4 py-2 rounded-lg flex-1 min-h-[3rem] h-auto resize-none overflow-hidden leading-tight disabled:opacity-60 disabled:cursor-not-allowed"
            @input="
              (e) => {
                handleDescriptionInput(e);

                const el = e.target as HTMLTextAreaElement;
                el.style.height = 'auto';
                el.style.height = el.scrollHeight + 'px';
              }
            "
          ></textarea>

          <!-- Hidden input -->
          <input
            ref="fileInputRef"
            type="file"
            class="hidden"
            accept="application/pdf,image/*"
            multiple
            @change="handleFileChange"
          />

          <button
            @click="handleStartExtract"
            :disabled="locked"
            class="w-10 h-10 rounded-lg flex items-center justify-center self-end transition"
            :class="
              locked
                ? 'bg-gray-300 cursor-not-allowed opacity-60'
                : 'bg-white hover:bg-gray-100'
            "
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
              <line x1="5" y1="12" x2="19" y2="12" />
              <polyline points="12 5 19 12 12 19" />
            </svg>
          </button>
        </div>
      </div>

      <!-- MODE: search (Search button) -->
      <div v-else class="bg-gray-200 rounded-2xl p-6 mb-6 relative">
        <div class="flex items-center justify-center gap-3">
          <!-- Input -->
          <textarea
            :disabled="locked"
            placeholder="type search name"
            :value="name"
            @input="handleNameInput"
            rows="1"
            class="bg-gray-200 px-4 py-3 rounded-lg h-12 w-full max-w-full resize-none overflow-hidden text-gray-800 leading-tight"
            :class="locked ? 'opacity-60 cursor-not-allowed' : ''"
          ></textarea>

          <!-- Button -->
          <button
            @click="handleSearchMode"
            :disabled="locked"
            class="w-12 h-12 rounded-lg flex items-center justify-center transition"
            :class="
              locked
                ? 'bg-gray-300 cursor-not-allowed opacity-60'
                : 'bg-white hover:bg-gray-100'
            "
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
              <line x1="5" y1="12" x2="19" y2="12" />
              <polyline points="12 5 19 12 12 19" />
            </svg>
          </button>
        </div>
      </div>
    </div>
  </Transition>
</template>

<style scoped>
.mode-fade-enter-active,
.mode-fade-leave-active {
  transition: all 0.25s ease;
}

.mode-fade-enter-from,
.mode-fade-leave-to {
  opacity: 0;
  transform: translateY(8px) scale(0.98);
}
</style>
