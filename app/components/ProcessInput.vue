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
        }
      | { mode: "search"; name: string }
  ): void;
}>();

const fileInputRef = ref<HTMLInputElement | null>(null);
const selectedFile = ref<File | null>(null);
const selectedFileName = ref<string | null>(null);

const handleFileButtonClick = () => {
  if (busy.value) return; 
  fileInputRef.value?.click();
};

const handleNameInput = (event: Event) => {
  const target = event.target as HTMLInputElement | HTMLTextAreaElement;
  emit("update:name", target.value);
};

const handleDescriptionInput = (event: Event) => {
  const target = event.target as HTMLTextAreaElement;
  emit("update:description", target.value);
};

const handleFileChange = (event: Event) => {
  const target = event.target as HTMLInputElement;
  const file = target.files?.[0] ?? null;
  selectedFile.value = file;
  selectedFileName.value = file ? file.name : null;
  emit("update:file", file);
};

const handleStartExtract = () => {
  if (busy.value) return;
  locked.value = true;
  emit("start-extract", {
    mode: "full",
    name: name.value,
    description: description.value,
    file: selectedFile.value,
    fileName: selectedFileName.value,
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
        <!-- file name on top-left -->
        <div
          v-if="selectedFileName"
          class="absolute top-2 left-10 text-sm text-gray-600"
        >
          File: {{ selectedFileName }}
        </div>

        <div class="flex items-start gap-3 mb-4 mt-3">
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

          <input
            type="text"
            placeholder="type name"
            :value="name"
            @input="handleNameInput"
            :disabled="locked"
            class="bg-black text-white px-4 py-2 rounded-lg w-80"
            :class="locked ? 'opacity-60 cursor-not-allowed' : ''"
          />
        </div>

        <div class="flex items-start gap-3">
          <textarea
            placeholder="type about process description"
            :value="description"
            @input="handleDescriptionInput"
            :disabled="locked"
            class="bg-gray-200 px-4 py-2 rounded-lg flex-1 h-12 resize-none overflow-hidden leading-tight"
            :class="locked ? 'opacity-60 cursor-not-allowed' : ''"
            rows="1"
          ></textarea>

          <!-- hidden file input -->
          <input
            ref="fileInputRef"
            type="file"
            class="hidden"
            accept="application/pdf,image/*"
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
            class="bg-gray-200 px-4 py-3 rounded-lg h-12 w-full max-w-full resize-none overflow-hidden text-gray-800 leading-tight "
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
