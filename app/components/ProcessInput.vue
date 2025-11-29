<template>
  <div class="bg-gray-200 rounded-2xl p-6 mb-6 relative">
    <div class="flex items-start gap-3 mb-4">
      <button class="w-8 h-8 bg-black text-white rounded-full flex items-center justify-center hover:bg-gray-800 transition">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="12" y1="5" x2="12" y2="19"></line>
          <line x1="5" y1="12" x2="19" y2="12"></line>
        </svg>
      </button>
      <input
        type="text"
        placeholder="type name"
        :value="name"
        @input="$emit('update:name', $event.target.value)"
        class="bg-black text-white px-4 py-2 rounded-lg flex-1"
      />
    </div>
    <div class="flex items-center gap-3">
      <input
        type="text"
        placeholder="type about process description"
        :value="description"
        @input="$emit('update:description', $event.target.value)"
        class="bg-white px-4 py-2 rounded-lg flex-1"
      />
      <button class="w-10 h-10 bg-white rounded-lg flex items-center justify-center hover:bg-gray-100 transition">
        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <line x1="5" y1="12" x2="19" y2="12"></line>
          <polyline points="12 5 19 12 12 19"></polyline>
        </svg>
      </button>
    </div>
    <div class="absolute -bottom-8 left-1/3 bg-gray-200 px-4 py-2 rounded-lg text-sm text-gray-600">
      name<br />process description
    </div>
  </div>
</template>

<script setup>
defineProps(['name', 'description'])
defineEmits(['update:name', 'update:description'])
</script>