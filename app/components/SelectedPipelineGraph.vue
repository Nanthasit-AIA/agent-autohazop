<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from 'vue'

export interface Connection {
  line_id: string
  from_id: string
  to_id: string
  context?: string
}

interface NodePosition {
  id: string
  x: number
  y: number
}

const props = defineProps<{
  show: boolean
  connections: Connection[]
}>()

const emit = defineEmits<{
  close: []
}>()

const hoveredNode = ref<string | null>(null)

const svgWidth = 1400
const svgHeight = 900

const handleEscape = (e: KeyboardEvent) => {
  if (e.key === 'Escape' && props.show) {
    emit('close')
  }
}

onMounted(() => {
  document.addEventListener('keydown', handleEscape)
})

onUnmounted(() => {
  document.removeEventListener('keydown', handleEscape)
})

// Extract unique nodes and find connected groups
const graphData = computed(() => {
  const uniqueNodes = new Set<string>()
  props.connections.forEach((conn) => {
    uniqueNodes.add(conn.from_id)
    uniqueNodes.add(conn.to_id)
  })

  // Build adjacency for grouping
  const adjacency: { [key: string]: Set<string> } = {}
  uniqueNodes.forEach(node => {
    adjacency[node] = new Set()
  })
  
  props.connections.forEach(conn => {
    const fromAdj = adjacency[conn.from_id]
    const toAdj = adjacency[conn.to_id]
    if (fromAdj && toAdj) {
      fromAdj.add(conn.to_id)
      toAdj.add(conn.from_id)
    }
  })

  // Find connected components using BFS
  const visited = new Set<string>()
  const groups: string[][] = []
  
  uniqueNodes.forEach(node => {
    if (!visited.has(node)) {
      const group: string[] = []
      const queue = [node]
      while (queue.length > 0) {
        const current = queue.shift()
        if (current && !visited.has(current)) {
          visited.add(current)
          group.push(current)
          const neighbors = adjacency[current]
          if (neighbors) {
            neighbors.forEach(neighbor => {
              if (!visited.has(neighbor)) {
                queue.push(neighbor)
              }
            })
          }
        }
      }
      groups.push(group)
    }
  })

  // Position nodes by group with increased spacing
  const positions: { [key: string]: NodePosition } = {}
  let currentY = 100
  
  groups.forEach((group, groupIndex) => {
    // Calculate levels within group based on dependencies
    const levels: { [key: string]: number } = {}
    const inDegree: { [key: string]: number } = {}
    
    group.forEach(node => {
      inDegree[node] = 0
    })
    
    props.connections.forEach(conn => {
      if (group.includes(conn.to_id) && group.includes(conn.from_id)) {
        inDegree[conn.to_id] = (inDegree[conn.to_id] || 0) + 1
      }
    })
    
    // BFS to assign levels
    const queue = group.filter(n => inDegree[n] === 0)
    queue.forEach(n => levels[n] = 0)
    
    while (queue.length > 0) {
      const current = queue.shift()
      if (!current) continue
      
      props.connections.forEach(conn => {
        if (conn.from_id === current && group.includes(conn.to_id)) {
          const currentLevel = levels[current] ?? 0
          const toLevel = levels[conn.to_id] ?? 0
          
          if (levels[conn.to_id] === undefined || toLevel <= currentLevel) {
            levels[conn.to_id] = currentLevel + 1
          }
          inDegree[conn.to_id] = (inDegree[conn.to_id] || 1) - 1
          if (inDegree[conn.to_id] === 0) {
            queue.push(conn.to_id)
          }
        }
      })
    }
    
    // Assign remaining nodes
    group.forEach(node => {
      if (levels[node] === undefined) {
        levels[node] = 0
      }
    })
    
    // Group by level
    const levelGroups: { [key: number]: string[] } = {}
    group.forEach(node => {
      const level = levels[node] ?? 0
      if (!levelGroups[level]) levelGroups[level] = []
      levelGroups[level].push(node)
    })
    
    const levelKeys = Object.keys(levelGroups).map(Number).sort((a, b) => a - b)
    const groupStartY = currentY
    
    levelKeys.forEach((level, levelIndex) => {
      const nodesAtLevel = levelGroups[level]
      if (!nodesAtLevel) return
      
      const levelWidth = nodesAtLevel.length * 280 // Increased spacing
      const startX = (svgWidth - levelWidth) / 2 + 140
      
      nodesAtLevel.forEach((node, nodeIndex) => {
        positions[node] = {
          id: node,
          x: startX + nodeIndex * 280, // Increased spacing
          y: groupStartY + levelIndex * 180, // Increased spacing
        }
      })
    })
    
    currentY = groupStartY + levelKeys.length * 180 + 80
    
    // Add separator line for groups
    if (groupIndex < groups.length - 1) {
      currentY += 50
    }
  })

  return { nodePositions: positions, connectedGroups: groups }
})

const nodePositions = computed(() => graphData.value.nodePositions)
const connectedGroups = computed(() => graphData.value.connectedGroups)

const formatNodeName = (name: string) => {
  return name.replace(/_/g, " ")
}

// Get connections for a node
const getNodeConnections = (nodeId: string) => {
  return props.connections.filter(
    (conn) => conn.from_id === nodeId || conn.to_id === nodeId
  )
}

// Group connections by from-to pair to handle parallel lines
const connectionGroups = computed(() => {
  const groups: { [key: string]: Connection[] } = {}
  props.connections.forEach((conn) => {
    const key = [conn.from_id, conn.to_id].sort().join("--")
    if (!groups[key]) groups[key] = []
    groups[key].push(conn)
  })
  return groups
})

// Get highlighted state for a connection
const isConnectionHighlighted = (conn: Connection) => {
  return hoveredNode.value === conn.from_id || hoveredNode.value === conn.to_id
}

// Get path data for a connection
const getConnectionPath = (conn: Connection, index: number, total: number) => {
  const from = nodePositions.value[conn.from_id]
  const to = nodePositions.value[conn.to_id]
  if (!from || !to) return null
  return getPath(from, to, index, total)
}

// Check if node is connected to hovered node
const isNodeConnectedToHovered = (nodeId: string) => {
  if (!hoveredNode.value) return false
  const nodeConnections = getNodeConnections(nodeId)
  return nodeConnections.some(
    (c) => c.from_id === hoveredNode.value || c.to_id === hoveredNode.value
  )
}
const getPath = (from: NodePosition, to: NodePosition, index: number, total: number) => {
  const dx = to.x - from.x
  const dy = to.y - from.y
  
  // Offset for parallel lines
  const offsetAmount = total > 1 ? (index - (total - 1) / 2) * 18 : 0
  
  // Perpendicular offset
  const length = Math.sqrt(dx * dx + dy * dy)
  const perpX = length > 0 ? (-dy / length) * offsetAmount : 0
  const perpY = length > 0 ? (dx / length) * offsetAmount : 0

  const startX = from.x + perpX
  const startY = from.y + perpY
  const endX = to.x + perpX
  const endY = to.y + perpY

  const midX = (startX + endX) / 2
  const midY = (startY + endY) / 2

  // Create smooth curves
  if (Math.abs(dy) < 60) {
    // Horizontal-ish connections - arc over/under
    const curveOffset = Math.sign(perpY) * 50 || 50
    return {
      path: `M ${startX} ${startY} Q ${midX} ${midY - curveOffset} ${endX} ${endY}`,
      labelX: midX,
      labelY: midY - curveOffset / 2 - 10,
    }
  } else {
    // Vertical connections - smooth S-curve
    return {
      path: `M ${startX} ${startY} C ${startX} ${midY} ${endX} ${midY} ${endX} ${endY}`,
      labelX: midX + perpX,
      labelY: midY,
    }
  }
}
</script>

<template>
  <!-- Full-screen Modal -->
  <Teleport to="body">
    <Transition
      enter-active-class="transition-opacity duration-200"
      leave-active-class="transition-opacity duration-200"
      enter-from-class="opacity-0"
      leave-to-class="opacity-0"
    >
      <div
        v-if="show"
        class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 backdrop-blur-sm"
        @click.self="emit('close')"
      >
        <Transition
          enter-active-class="transition-all duration-200"
          leave-active-class="transition-all duration-200"
          enter-from-class="opacity-0 scale-95"
          leave-to-class="opacity-0 scale-95"
        >
          <div
            v-if="show"
            class="w-full h-full m-4 bg-white rounded-2xl shadow-2xl flex flex-col overflow-hidden"
          >
            <!-- Header -->
            <div class="flex items-center justify-between px-6 py-4 border-b border-gray-200 bg-white shrink-0">
              <h2 class="text-2xl font-black text-gray-900">
                🗠🔍 Pipeline Graph Preview
                <span class="text-sm font-bold text-gray-500 ml-2">
                  ({{ connections.length }} connections)
                </span>
              </h2>
              <button
                @click="emit('close')"
                class="p-2 text-gray-500 bg-gray-300 hover:text-gray-700 hover:bg-gray-100 rounded-full transition-colors"
                title="Close (ESC)"
                >
                
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="currentColor"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <line x1="18" y1="6" x2="6" y2="18"></line>
                  <line x1="6" y1="6" x2="18" y2="18"></line>
                </svg>
              </button>
            </div>
            <!-- Graph -->
            <div class="flex-1 relative overflow-auto bg-gray-50">
              <svg
                :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                class="w-full h-full"
                style="min-height: 600px; min-width: 900px"
              >
                <defs>
                  <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
                    <feGaussianBlur stdDeviation="4" result="coloredBlur" />
                    <feMerge>
                      <feMergeNode in="coloredBlur" />
                      <feMergeNode in="SourceGraphic" />
                    </feMerge>
                  </filter>
                  <marker
                    id="arrow"
                    markerWidth="8"
                    markerHeight="6"
                    refX="7"
                    refY="3"
                    orient="auto"
                  >
                    <polygon points="0 0, 8 3, 0 6" fill="#3b82f6" opacity="0.6" />
                  </marker>
                  <marker
                    id="arrow-highlight"
                    markerWidth="8"
                    markerHeight="6"
                    refX="7"
                    refY="3"
                    orient="auto"
                  >
                    <polygon points="0 0, 8 3, 0 6" fill="#8b5cf6" />
                  </marker>
                </defs>

                <!-- Group separators -->
                <g v-if="connectedGroups.length > 1">
                  <g v-for="(group, index) in connectedGroups.slice(0, -1)" :key="`sep-${index}`">
                    <template v-if="group.every(n => nodePositions[n])">
                      <line
                        x1="100"
                        :y1="Math.max(...group.map(n => nodePositions[n]?.y || 0)) + 90"
                        :x2="svgWidth - 100"
                        :y2="Math.max(...group.map(n => nodePositions[n]?.y || 0)) + 90"
                        stroke="#e5e7eb"
                        stroke-width="1"
                        stroke-dasharray="8 4"
                      />
                      <text
                        :x="svgWidth / 2"
                        :y="Math.max(...group.map(n => nodePositions[n]?.y || 0)) + 110"
                        text-anchor="middle"
                        class="text-[10px] fill-gray-500"
                      >
                        Separate Connection Group
                      </text>
                    </template>
                  </g>
                </g>

                <!-- Connection lines -->
                <template v-for="(group, groupKey) in connectionGroups" :key="groupKey">
                  <template v-for="(conn, index) in group" :key="conn.line_id">
                    <g v-if="getConnectionPath(conn, index, group.length)">
                      <!-- Line shadow for depth -->
                      <path
                        :d="getConnectionPath(conn, index, group.length)!.path"
                        fill="none"
                        :stroke="isConnectionHighlighted(conn) ? '#8b5cf6' : '#3b82f6'"
                        :stroke-width="isConnectionHighlighted(conn) ? 4.5 : 1.5"
                        :stroke-opacity="isConnectionHighlighted(conn) ? 1.5 : 0.5"
                      />
                      <!-- Main line -->
                      <path
                        :d="getConnectionPath(conn, index, group.length)!.path"
                        fill="none"
                        :stroke="isConnectionHighlighted(conn) ? '#8b5cf6' : '#3b82f6'"
                        :stroke-width="isConnectionHighlighted(conn) ? 2.5 : 1.5"
                        :stroke-opacity="isConnectionHighlighted(conn) ? 1 : 0.5"
                        :marker-end="isConnectionHighlighted(conn) ? 'url(#arrow-highlight)' : 'url(#arrow)'"
                        class="transition-all duration-300"
                        :filter="isConnectionHighlighted(conn) ? 'url(#glow)' : undefined"
                      />
                      <!-- Line label -->
                      <g :transform="`translate(${getConnectionPath(conn, index, group.length)!.labelX}, ${getConnectionPath(conn, index, group.length)!.labelY})`">
                        <rect
                          x="-18"
                          y="-10"
                          width="36"
                          height="20"
                          rx="4"
                          fill="white"
                          fill-opacity="0.9"
                          :stroke="isConnectionHighlighted(conn) ? '#8b5cf6' : '#e5e7eb'"
                          stroke-width="1"
                        />
                        <text
                          text-anchor="middle"
                          dominant-baseline="middle"
                          :class="[
                            'text-[10px] font-mono font-medium transition-all duration-300',
                            isConnectionHighlighted(conn) ? 'fill-purple-600' : 'fill-gray-600'
                          ]"
                        >
                          {{ conn.line_id }}
                        </text>
                      </g>
                    </g>
                  </template>
                </template>

                <!-- Nodes -->
                <g
                  v-for="pos in Object.values(nodePositions)"
                  :key="pos.id"
                  :transform="`translate(${pos.x}, ${pos.y})`"
                  @mouseenter="hoveredNode = pos.id"
                  @mouseleave="hoveredNode = null"
                  class="cursor-pointer"
                >
                  <!-- Node glow -->
                  <circle
                    v-if="hoveredNode === pos.id || isNodeConnectedToHovered(pos.id)"
                    :r="hoveredNode === pos.id ? 40 : 32"
                    fill="#8b5cf6"
                    opacity="0.2"
                    class="animate-pulse"
                  />

                  <!-- Main node -->
                  <circle
                    :r="hoveredNode === pos.id ? 28 : 24"
                    fill="white"
                    :stroke="hoveredNode === pos.id ? '#8b5cf6' : isNodeConnectedToHovered(pos.id) ? '#3b82f6' : '#e5e7eb'"
                    :stroke-width="hoveredNode === pos.id ? 3 : 2"
                    class="transition-all duration-300"
                    :filter="hoveredNode === pos.id ? 'url(#glow)' : undefined"
                  />

                  <!-- Inner dot -->
                  <circle
                    :r="hoveredNode === pos.id ? 6 : 5"
                    :fill="hoveredNode === pos.id ? '#8b5cf6' : '#3b82f6'"
                    class="transition-all duration-300"
                  />

                  <!-- Label -->
                  <text
                    :y="hoveredNode === pos.id ? 46 : 40"
                    text-anchor="middle"
                    :class="[
                      'text-[10px] font-medium transition-all duration-300 pointer-events-none',
                      hoveredNode === pos.id ? 'fill-purple-600' : isNodeConnectedToHovered(pos.id) ? 'fill-gray-900' : 'fill-gray-600'
                    ]"
                  >
                    {{ formatNodeName(pos.id).length > 18
                      ? formatNodeName(pos.id).substring(0, 18) + "..."
                      : formatNodeName(pos.id) }}
                  </text>
                </g>
              </svg>

              <!-- Hover tooltip -->
              <div
                v-if="hoveredNode"
                class="absolute top-6 right-6 bg-white border border-gray-200 rounded-xl p-4 shadow-2xl max-w-xs animate-fade-in z-10"
              >
                <div class="space-y-3">
                  <div class="flex items-center gap-2">
                    <div class="w-3 h-3 rounded-full bg-purple-600 animate-pulse" />
                    <h3 class="font-semibold text-gray-900 text-sm">
                      {{ formatNodeName(hoveredNode) }}
                    </h3>
                  </div>

                  <div class="space-y-2">
                    <p class="text-[10px] text-gray-600 uppercase tracking-wider">
                      Connections
                    </p>
                    <div class="space-y-1 max-h-40 overflow-y-auto">
                      <div
                        v-for="conn in getNodeConnections(hoveredNode)"
                        :key="conn.line_id"
                        class="flex items-center gap-1.5 text-xs bg-gray-50 rounded-lg px-2 py-1.5"
                      >
                        <span class="font-mono text-[10px] text-blue-600 font-bold min-w-7">
                          {{ conn.line_id }}
                        </span>
                        <span class="text-gray-700 text-[10px] truncate">
                          {{ formatNodeName(conn.from_id) }}
                        </span>
                        <svg
                          class="w-3 h-3 text-purple-600 shrink-0"
                          fill="none"
                          viewBox="0 0 24 24"
                          stroke="currentColor"
                        >
                          <path
                            stroke-linecap="round"
                            stroke-linejoin="round"
                            stroke-width="2"
                            d="M17 8l4 4m0 0l-4 4m4-4H3"
                          />
                        </svg>
                        <span class="text-gray-700 text-[10px] truncate">
                          {{ formatNodeName(conn.to_id) }}
                        </span>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </Transition>
      </div>
    </Transition>
  </Teleport>
</template>

<style scoped>
@keyframes fade-in {
  from {
    opacity: 0;
    transform: translateY(-10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fade-in 0.7s ease-out;
}
</style>