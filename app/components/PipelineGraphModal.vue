<template>
  <Transition name="fade">
    <div
      v-if="show"
      class="fixed inset-0 z-50 flex items-center justify-center"
    >
      <!-- Backdrop -->
      <div
        class="absolute inset-0 bg-black/70"
        @click="handleClose"
      />

      <!-- Modal container -->
      <div
        :class="[
          'relative bg-background border border-border shadow-2xl flex flex-col overflow-hidden transition-all',
          isFullScreen
            ? 'w-screen h-screen max-w-none rounded-none'
            : 'w-[90vw] max-w-6xl h-[80vh] rounded-2xl'
        ]"
      >
        <!-- Header -->
        <div
          class="flex items-center justify-between px-4 py-3 border-b border-border bg-background/80 backdrop-blur-sm"
        >
          <div class="flex items-center gap-3">
            <span class="inline-flex h-6 w-6 items-center justify-center rounded-full bg-primary/10">
              <span class="h-2 w-2 rounded-full bg-primary" />
            </span>
            <div class="flex flex-col">
              <h2 class="text-sm font-semibold text-foreground">
                Pipeline Graph Preview
              </h2>
              <p class="text-xs text-muted-foreground">
                {{ connections.length }} connections ·
                {{ connectedGroups.length }} group<span v-if="connectedGroups.length !== 1">s</span>
              </p>
            </div>
          </div>

          <div class="flex items-center gap-2">
            <button
              type="button"
              class="px-3 py-1.5 text-xs rounded-lg border border-border/70 text-muted-foreground hover:bg-muted transition"
              @click="toggleFullScreen"
            >
              {{ isFullScreen ? 'Exit full screen' : 'Full screen' }}
            </button>

            <button
              type="button"
              class="px-3 py-1.5 text-xs rounded-lg bg-muted hover:bg-muted/80 text-foreground transition"
              @click="handleClose"
            >
              Close
            </button>
          </div>
        </div>

        <!-- Graph area -->
        <div class="flex-1 relative overflow-auto bg-background">
          <svg
            :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
            class="w-full h-full"
            :style="{ minHeight: '500px', minWidth: '800px' }"
          >
            <defs>
              <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
                <feGaussianBlur stdDeviation="3" result="coloredBlur" />
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
                <polygon
                  points="0 0, 8 3, 0 6"
                  fill="hsl(var(--primary))"
                  opacity="0.6"
                />
              </marker>

              <marker
                id="arrow-highlight"
                markerWidth="8"
                markerHeight="6"
                refX="7"
                refY="3"
                orient="auto"
              >
                <polygon
                  points="0 0, 8 3, 0 6"
                  fill="hsl(var(--accent))"
                />
              </marker>
            </defs>

            <!-- Group separators -->
            <g v-if="connectedGroups.length > 1">
              <template
                v-for="(group, index) in connectedGroups.slice(0, -1)"
                :key="`sep-${index}`"
              >
                <line
                  :x1="100"
                  :y1="getGroupSeparatorY(group) + 70"
                  :x2="svgWidth - 100"
                  :y2="getGroupSeparatorY(group) + 70"
                  stroke="hsl(var(--border))"
                  stroke-width="1"
                  stroke-dasharray="8 4"
                />
                <text
                  :x="svgWidth / 2"
                  :y="getGroupSeparatorY(group) + 90"
                  text-anchor="middle"
                  class="text-[10px] fill-muted-foreground"
                >
                  Separate Connection Group
                </text>
              </template>
            </g>

            <!-- Connection lines -->
            <g
              v-for="{ conn, from, to } in connectionsWithPos"
              :key="conn.line_id"
              class="cursor-pointer"
              @mouseenter="hoveredLine = conn.line_id"
              @mouseleave="hoveredLine = null"
            >
              <path
                :d="getPath(from, to)"
                fill="none"
                stroke="transparent"
                stroke-width="20"
              />
              <!-- Shadow -->
              <path
                :d="getPath(from, to)"
                fill="none"
                stroke="hsl(var(--background))"
                :stroke-width="isHovered(conn.line_id) ? 5 : 3"
                stroke-opacity="0.5"
              />
              <!-- Main line -->
              <path
                :d="getPath(from, to)"
                fill="none"
                :stroke="isHovered(conn.line_id)
                  ? 'hsl(var(--accent))'
                  : 'hsl(var(--primary))'"
                :stroke-width="isHovered(conn.line_id) ? 2.5 : 1.5"
                :stroke-opacity="isHovered(conn.line_id) ? 1 : 0.6"
                :marker-end="isHovered(conn.line_id)
                  ? 'url(#arrow-highlight)'
                  : 'url(#arrow)'"
                class="transition-all duration-200"
                :filter="isHovered(conn.line_id) ? 'url(#glow)' : undefined"
              />

              <!-- Line label -->
              <g
                :transform="`translate(${(from.x + to.x) / 2}, ${(from.y + to.y) / 2})`"
              >
                <rect
                  x="-18"
                  y="-10"
                  width="36"
                  height="20"
                  rx="4"
                  fill="hsl(var(--card))"
                  :stroke="isHovered(conn.line_id)
                    ? 'hsl(var(--accent))'
                    : 'hsl(var(--border))'"
                  stroke-width="1"
                />
                <text
                  text-anchor="middle"
                  dominant-baseline="middle"
                  class="text-[10px] font-mono font-medium"
                  :class="isHovered(conn.line_id)
                    ? 'fill-accent'
                    : 'fill-muted-foreground'"
                >
                  {{ conn.line_id }}
                </text>
              </g>
            </g>

            <!-- Nodes -->
            <g
              v-for="pos in Object.values(nodePositions)"
              :key="pos.id"
              :transform="`translate(${pos.x}, ${pos.y})`"
            >
              <circle
                r="24"
                fill="hsl(var(--card))"
                stroke="hsl(var(--border))"
                stroke-width="2"
              />
              <circle r="5" fill="hsl(var(--primary))" />
              <text
                y="40"
                text-anchor="middle"
                class="text-[10px] font-medium fill-foreground pointer-events-none"
              >
                {{
                  formatLabel(pos.id).length > 16
                    ? formatLabel(pos.id).slice(0, 16) + '...'
                    : formatLabel(pos.id)
                }}
              </text>
            </g>
          </svg>

          <!-- Hover tooltip -->
          <div
            v-if="hoveredConnection"
            class="absolute top-4 right-4 bg-card border border-accent rounded-xl p-4 shadow-2xl max-w-sm animate-fade-in z-10"
          >
            <div class="space-y-2">
              <div class="flex items-center gap-2">
                <div class="w-2 h-2 rounded-full bg-accent" />
                <span class="font-mono font-bold text-accent text-sm">
                  {{ hoveredConnection.line_id }}
                </span>
              </div>

              <div class="flex items-center gap-2 text-sm">
                <span class="text-primary font-medium">
                  {{ formatLabel(hoveredConnection.from_id) }}
                </span>
                <span class="text-muted-foreground">→</span>
                <span class="text-primary font-medium">
                  {{ formatLabel(hoveredConnection.to_id) }}
                </span>
              </div>

              <p
                v-if="hoveredConnection.context"
                class="text-xs text-muted-foreground border-t border-border pt-2 mt-2"
              >
                {{ hoveredConnection.context }}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </Transition>
</template>

<script setup lang="ts">
import { computed, ref, withDefaults } from 'vue'

export interface Connection {
  from_id: string
  to_id: string
  line_id: string
  context?: string | null
}

interface NodePosition {
  id: string
  x: number
  y: number
}

interface Props {
  show?: boolean
  connections: Connection[]
}

const props = withDefaults(defineProps<Props>(), {
  show: false,
  connections: () => []
})

const emit = defineEmits<{
  (e: 'close'): void
}>()

const svgWidth = 1200
const svgHeight = 800

const hoveredLine = ref<string | null>(null)
const isFullScreen = ref(false)

// ---------- Layout calculation ----------
const layout = computed<{
  nodePositions: Record<string, NodePosition>
  connectedGroups: string[][]
}>(() => {
  const connections = props.connections
  const uniqueNodes = new Set<string>()

  // collect all nodes
  for (const conn of connections) {
    uniqueNodes.add(conn.from_id)
    uniqueNodes.add(conn.to_id)
  }

  // adjacency map
  const adjacency = new Map<string, Set<string>>()
  for (const node of uniqueNodes) {
    adjacency.set(node, new Set())
  }

  for (const conn of connections) {
    const fromSet = adjacency.get(conn.from_id)
    const toSet = adjacency.get(conn.to_id)
    if (fromSet) fromSet.add(conn.to_id)
    if (toSet) toSet.add(conn.from_id)
  }

  // BFS connected components
  const visited = new Set<string>()
  const groups: string[][] = []

  for (const node of uniqueNodes) {
    if (visited.has(node)) continue

    const group: string[] = []
    const queue: string[] = [node]

    while (queue.length > 0) {
      const current = queue.shift()!
      if (visited.has(current)) continue
      visited.add(current)
      group.push(current)

      const neighbors = adjacency.get(current)
      if (!neighbors) continue
      for (const n of neighbors) {
        if (!visited.has(n)) queue.push(n)
      }
    }

    groups.push(group)
  }

  const positions: Record<string, NodePosition> = {}
  let currentY = 80

  // layout each group
  groups.forEach((group, groupIndex) => {
    const levels: Record<string, number> = {}
    const inDegree: Record<string, number> = {}
    const groupSet = new Set(group)

    // init in-degree
    for (const node of group) {
      inDegree[node] = 0
    }

    // compute in-degree only for edges inside this group
    for (const conn of connections) {
      if (groupSet.has(conn.from_id) && groupSet.has(conn.to_id)) {
        inDegree[conn.to_id] = (inDegree[conn.to_id] ?? 0) + 1
      }
    }

    // queue for topological layering
    const q: string[] = []
    for (const node of group) {
      if ((inDegree[node] ?? 0) === 0) {
        levels[node] = 0
        q.push(node)
      }
    }

    while (q.length > 0) {
      const current = q.shift()!
      const currentLevel = levels[current] ?? 0

      for (const conn of connections) {
        if (conn.from_id === current && groupSet.has(conn.to_id)) {
          const nextLevel = currentLevel + 1

          if ((levels[conn.to_id] ?? -1) < nextLevel) {
            levels[conn.to_id] = nextLevel
          }

          inDegree[conn.to_id] = (inDegree[conn.to_id] ?? 0) - 1
          if ((inDegree[conn.to_id] ?? 0) === 0) {
            q.push(conn.to_id)
          }
        }
      }
    }

    // any nodes that never got a level become 0
    for (const node of group) {
      if (levels[node] == null) {
        levels[node] = 0
      }
    }

    // group nodes by level using Map to avoid undefined access
    const levelGroups = new Map<number, string[]>()
    for (const node of group) {
      const level = levels[node] ?? 0
      const list = levelGroups.get(level) ?? []
      list.push(node)
      levelGroups.set(level, list)
    }

    const levelKeys = Array.from(levelGroups.keys()).sort((a, b) => a - b)
    const groupStartY = currentY

    levelKeys.forEach((level, levelIndex) => {
      const nodesAtLevel = levelGroups.get(level) ?? []
      const levelWidth = nodesAtLevel.length * 220
      const startX = (svgWidth - levelWidth) / 2 + 110

      nodesAtLevel.forEach((node, nodeIndex) => {
        positions[node] = {
          id: node,
          x: startX + nodeIndex * 220,
          y: groupStartY + levelIndex * 140
        }
      })
    })

    currentY = groupStartY + levelKeys.length * 140 + 60
    if (groupIndex < groups.length - 1) {
      currentY += 40
    }
  })

  return {
    nodePositions: positions,
    connectedGroups: groups
  }
})

const nodePositions = computed(() => layout.value.nodePositions)
const connectedGroups = computed(() => layout.value.connectedGroups)

// only keep connections whose endpoints have positions
const connectionsWithPos = computed(() => {
  const positions = nodePositions.value
  return props.connections
    .map((conn) => {
      const from = positions[conn.from_id]
      const to = positions[conn.to_id]
      if (!from || !to) return null
      return { conn, from, to }
    })
    .filter(
      (
        v
      ): v is { conn: Connection; from: NodePosition; to: NodePosition } =>
        v !== null
    )
})

// ---------- helpers ----------
const formatLabel = (name: string) => name.replace(/_/g, ' ')

const getPath = (from: NodePosition, to: NodePosition) => {
  const midY = (from.y + to.y) / 2
  return `M ${from.x} ${from.y} C ${from.x} ${midY} ${to.x} ${midY} ${to.x} ${to.y}`
}

const getGroupSeparatorY = (group: string[]) => {
  const positions = nodePositions.value
  if (group.length === 0) return 0
  return Math.max(...group.map((id) => positions[id]?.y ?? 0))
}

const isHovered = (lineId: string) => hoveredLine.value === lineId

const hoveredConnection = computed(() => {
  return props.connections.find((c) => c.line_id === hoveredLine.value) ?? null
})

const handleClose = () => {
  isFullScreen.value = false
  emit('close')
}

const toggleFullScreen = () => {
  isFullScreen.value = !isFullScreen.value
}
</script>


<style scoped>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.2s ease;
}
.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>
