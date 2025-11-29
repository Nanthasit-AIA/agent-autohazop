<template>
  <div class="bg-white border-2 border-gray-300 rounded-2xl p-6 mb-6">
    <h3 class="font-semibold text-gray-800 mb-4">Choose perform deviation</h3>
    <div class="mb-4">
      <div class="text-sm text-gray-600 mb-3">node 1 :<br />From ST-101 to HT-101<br />context</div>
      <div class="space-y-2">
        <label v-for="type in deviationTypes" :key="type" class="flex items-center gap-3 cursor-pointer">
          <input
            type="checkbox"
            :checked="modelValue[type] || false"
            @change="toggleDeviation(type, $event.target.checked)"
          />
          <span class="flex-1 text-gray-700">{{ type }}</span>
          <span class="text-sm text-gray-500">{{ deviationOptions[type] }}</span>
        </label>
      </div>
    </div>
    <div class="flex gap-3 mb-4">
      <button @click="selectAll" class="px-4 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition text-sm">
        select all
      </button>
      <button @click="deleteAll" class="px-4 py-2 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 transition text-sm">
        delete all
      </button>
    </div>
    <div class="flex items-center justify-between">
      <div class="flex items-center gap-2">
        <button class="p-2 hover:bg-gray-100 rounded">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="15 18 9 12 15 6"></polyline>
          </svg>
        </button>
        <span class="text-sm text-gray-600">← 1 2 3 4 5 . . . →</span>
        <button class="p-2 hover:bg-gray-100 rounded">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <polyline points="9 18 15 12 9 6"></polyline>
          </svg>
        </button>
      </div>
      <div class="flex gap-3">
        <button class="px-6 py-2 bg-black text-white rounded-lg hover:bg-gray-800 transition">
          Preview
        </button>
        <button class="w-10 h-10 bg-white border border-gray-300 rounded-lg flex items-center justify-center hover:bg-gray-50 transition">
          <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
const props = defineProps(['modelValue'])
const emit = defineEmits(['update:modelValue'])

const deviationTypes = ['Flow', 'Pressure', 'Temperature', 'Level', 'Concentration', 'Composition']

const deviationOptions = {
  'Flow': 'More - Less - NO - Reverse',
  'Pressure': 'More - Less',
  'Temperature': 'More - Less',
  'Level': 'More - Less - NO',
  'Concentration': 'More - Less',
  'Composition': 'Other than'
}

const toggleDeviation = (type, checked) => {
  emit('update:modelValue', { ...props.modelValue, [type]: checked })
}

const selectAll = () => {
  const all = {}
  deviationTypes.forEach(type => { all[type] = true })
  emit('update:modelValue', all)
}

const deleteAll = () => {
  emit('update:modelValue', {})
}
</script>