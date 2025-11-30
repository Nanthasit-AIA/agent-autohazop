<script setup lang="ts">
import { toRefs, ref, computed } from 'vue'

const props = defineProps<{
  name: string
  description: string
  mode?: 'full' | 'search'
}>()

const { name, description } = toRefs(props)
const mode = computed(() => props.mode ?? 'full')

const emit = defineEmits<{
  'update:name': [value: string]
  'update:description': [value: string]
  'update:file': [file: File | null]
  'start-extract': []
}>()

const selectedFileName = ref<string | null>(null)


const handleDescriptionInput = (e: Event) => {
  const el = e.target as HTMLTextAreaElement
  emit('update:description', el.value)

  el.style.height = 'auto'
  el.style.height = `${el.scrollHeight}px`
}

const fileInputRef = ref<HTMLInputElement | null>(null)

const handleFileButtonClick = () => {
  fileInputRef.value?.click()
}

const handleFileChange = (e: Event) => {
  const el = e.target as HTMLInputElement
  const file = el.files?.[0] ?? null

  selectedFileName.value = file ? file.name : null
  emit('update:file', file)
}

const handleNameInput = (e: Event) => {
  emit('update:name', (e.target as HTMLInputElement | HTMLTextAreaElement).value)
}

const handleStartExtract = () => {
  emit('start-extract')
}
</script>

<template>
  <!-- 🔄 Transition between full/search layouts -->
  <Transition name="mode-fade" mode="out-in">
    <!-- key forces Vue to treat them as different elements -->
    <div :key="mode" class="max-w-6xl mx-auto">
      <!-- ✅ MODE: full (Call to action) -->
      <div v-if="mode === 'full'" class="bg-gray-200 rounded-2xl p-6 mb-6 relative">
        <!-- file name on top-left -->
        <div v-if="selectedFileName" class="absolute top-2 left-10 text-sm text-gray-600">
          File: {{ selectedFileName }}
        </div>

        <div class="flex items-start gap-3 mb-4 mt-3">
          <button @click="handleFileButtonClick"
            class="w-8 h-8 bg-black text-white rounded-full flex items-center justify-center hover:bg-gray-800 transition">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="12" y1="5" x2="12" y2="19" />
              <line x1="5" y1="12" x2="19" y2="12" />
            </svg>
          </button>

          <input type="text" placeholder="type name" :value="name" @input="handleNameInput"
            class="bg-black text-white px-4 py-2 rounded-lg w-80" />
        </div>

        <div class="flex items-start gap-3">
          <textarea placeholder="type about process description" :value="description" @input="handleDescriptionInput"
            class="bg-gray-200 px-4 py-2 rounded-lg flex-1 h-12 resize-none overflow-hidden leading-tight"
            rows="1"></textarea>

          <!-- hidden file input -->
          <input ref="fileInputRef" type="file" class="hidden" accept="application/pdf,image/*"
            @change="handleFileChange" />

          <button @click="handleStartExtract"
            class="w-10 h-10 bg-white rounded-lg flex items-center justify-center hover:bg-gray-100 transition self-end">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <line x1="5" y1="12" x2="19" y2="12" />
              <polyline points="12 5 19 12 12 19" />
            </svg>
          </button>
        </div>
      </div>

      <!-- ✅ MODE: search (Search button) -->
      <div v-else class="bg-gray-200 rounded-2xl p-6 mb-6 relative">
        <div class="flex items-start gap-3 justify-center">
          <textarea type="text" placeholder="type name" :value="name" @input="handleNameInput"
            class="bg-gray-200 px-4 py-2 rounded-lg flex-1 h-12 resize-none overflow-hidden leading-tight items-center justify-center"
            rows="1"></textarea>

          <button @click="handleStartExtract"
            class="w-10 h-10 bg-white rounded-lg flex items-center justify-center hover:bg-gray-100 transition self-end">
            <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none"
              stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
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
