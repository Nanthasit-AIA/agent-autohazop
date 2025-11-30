<script setup lang="ts">
export interface NodeItem {
  id: string | number
  name: string
  range?: string
  context?: string
}


const props = defineProps<{
  modelValue: (string | number)[];
  nodes: NodeItem[];
}>();

const emit = defineEmits<{
  "update:modelValue": [(string | number)[]];
  next: [];
}>();

const toggleNode = (nodeId: string | number) => {
  const exists = props.modelValue.includes(nodeId);
  const newValue = exists
    ? props.modelValue.filter((id) => id !== nodeId)
    : [...props.modelValue, nodeId];

  emit("update:modelValue", newValue);
};

const handleNextClick = () => {
  emit("next");
};

// ✅ Select all nodes
const handleSelectAll = () => {
  const allIds = props.nodes.map((node) => node.id);
  emit("update:modelValue", allIds);
};

// ✅ Clear all selections
const handleClearAll = () => {
  emit("update:modelValue", []);
};
</script>


<template>
  <div class="bg-white border-2 border-gray-300 rounded-2xl p-6 mb-6">
    <!-- Header + Select/Clear buttons -->
    <div class="flex items-center justify-between mb-4">
      <h3 class="font-semibold text-gray-800">
        Choose perform node : {{ modelValue.length }}/{{ nodes.length }}
      </h3>

      <div class="flex gap-2">
        <button
          type="button"
          class="px-3 py-1 text-sm font-semibold rounded-lg border border-gray-300 text-white bg-black hover:bg-gray-900 transition"
          @click="handleSelectAll"
        >
          Select all
        </button>
        <button
          type="button"
          class="px-3 py-1 text-sm font-semibold rounded-lg border border-gray-300 bg-white hover:bg-gray-50 transition"
          @click="handleClearAll"
        >
          Delete all
        </button>
      </div>
    </div>

    <!-- Node list -->
    <div
      class="grid grid-cols-2 gap-4 mb-4"
      :class="nodes.length > 4 ? 'max-h-64 overflow-y-auto pr-2' : ''"
    >
      <label
        v-for="node in nodes"
        :key="node.id"
        class="flex items-start gap-3 cursor-pointer"
      >
        <input
          type="checkbox"
          :checked="modelValue.includes(node.id)"
          @change="toggleNode(node.id)"
          class="mt-1"
        />
        <div class="flex-1">
          <div class="font-medium text-gray-700">
            {{ node.name }}
          </div>
          <div v-if="node.range" class="text-sm text-gray-500">
            {{ node.range }}
          </div>
          <div v-if="node.context" class="text-sm text-gray-500">
            {{ node.context }}
          </div>
        </div>
      </label>
    </div>

    <!-- Footer buttons -->
    <div class="flex items-center justify-end">
      <div class="flex gap-3">
        <button
          class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition"
          type="button"
        >
          Preview
        </button>
        <button
          class="w-10 h-10 bg-white border border-gray-300 rounded-lg flex items-center justify-center hover:bg-gray-50 transition"
          type="button"
          @click="handleNextClick"
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
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>
