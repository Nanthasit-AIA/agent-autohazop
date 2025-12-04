<script setup lang="ts">
const props = defineProps<{
  disabled?: boolean;
}>();

const emit = defineEmits<{
  (e: "call-hazop"): void;
  (e: "exit"): void;
}>();
</script>

<template>
  <div class="flex gap-3 justify-center mb-8">
    <button
      @click="emit('call-hazop')"
      :disabled="disabled"
      class="px-6 py-2 rounded-lg transition"
      :class="
        disabled
          ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
          : 'bg-black text-white hover:bg-gray-800'
      "
    >
      Call to HAZOP analysis
    </button>

    <button
      @click="emit('exit')"
      class="px-6 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition"
    >
      exit
    </button>
  </div>
</template>
