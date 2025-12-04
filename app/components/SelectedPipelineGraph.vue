<script setup lang="ts">
import { ref, computed, onMounted, onUnmounted } from "vue";

export interface Connection {
  line_id: string;
  from_id: string;
  to_id: string;
  context?: string;
}

interface NodePosition {
  id: string;
  x: number;
  y: number;
}

const props = defineProps<{
  show: boolean;
  connections: Connection[];
}>();

const emit = defineEmits<{
  close: [];
}>();

const hoveredNode = ref<string | null>(null);
const zoom = ref(1);
const panX = ref(0);
const panY = ref(0);
const isPanning = ref(false);
const lastMousePos = ref({ x: 0, y: 0 });
const svgContainer = ref<HTMLDivElement | null>(null);

const svgWidth = 1400;
const svgHeight = 900;

const tooltipStyle = computed(() => {
  if (!hoveredNode.value) return {};

  const pos = nodePositions.value[hoveredNode.value];
  if (!pos) return {};

  // Fixed distance from node center (in pixels)
  const offsetX = 150; // Distance to the right of the node
  const offsetY = 30; // Slight vertical adjustment to align with node center

  // Apply zoom and pan transformations
  const transformedX = pos.x * zoom.value + panX.value;
  const transformedY = pos.y * zoom.value + panY.value;

  return {
    left: '0',
    top: '0',
    transform: `translate(${transformedX + offsetX}px, ${transformedY + offsetY}px)`,
  };
});

const handleWheel = (e: WheelEvent) => {
  e.preventDefault();
  
  if (!svgContainer.value) return;
  
  const rect = svgContainer.value.getBoundingClientRect();
  const mouseX = e.clientX - rect.left;
  const mouseY = e.clientY - rect.top;
  
  // Calculate mouse position in SVG coordinates before zoom
  const beforeZoomX = (mouseX - panX.value) / zoom.value;
  const beforeZoomY = (mouseY - panY.value) / zoom.value;
  
  // Apply zoom
  const delta = e.deltaY > 0 ? 0.9 : 1.1;
  const newZoom = Math.max(0.1, Math.min(5, zoom.value * delta));
  
  // Calculate mouse position in SVG coordinates after zoom
  const afterZoomX = (mouseX - panX.value) / newZoom;
  const afterZoomY = (mouseY - panY.value) / newZoom;
  
  // Adjust pan to keep mouse position constant
  panX.value += (afterZoomX - beforeZoomX) * newZoom;
  panY.value += (afterZoomY - beforeZoomY) * newZoom;
  
  zoom.value = newZoom;
};

const handleMouseDown = (e: MouseEvent) => {
  // Start panning on left click or middle click, but not if clicking on a node
  if ((e.button === 0 || e.button === 1) && (e.target as HTMLElement).tagName === 'svg') {
    e.preventDefault();
    isPanning.value = true;
    lastMousePos.value = { x: e.clientX, y: e.clientY };
  }
};

const handleMouseMove = (e: MouseEvent) => {
  if (isPanning.value) {
    e.preventDefault();
    const dx = e.clientX - lastMousePos.value.x;
    const dy = e.clientY - lastMousePos.value.y;
    panX.value += dx;
    panY.value += dy;
    lastMousePos.value = { x: e.clientX, y: e.clientY };
  }
};

const handleMouseUp = (e: MouseEvent) => {
  isPanning.value = false;
};

const handleContainerMouseDown = (e: MouseEvent) => {
  // Allow panning from anywhere in the container
  if (e.button === 0 || e.button === 1) {
    e.preventDefault();
    isPanning.value = true;
    lastMousePos.value = { x: e.clientX, y: e.clientY };
  }
};

const zoomIn = () => {
  const centerX = svgWidth / 2;
  const centerY = svgHeight / 2;
  
  const beforeZoomX = (centerX - panX.value) / zoom.value;
  const beforeZoomY = (centerY - panY.value) / zoom.value;
  
  const newZoom = Math.min(5, zoom.value * 1.2);
  
  const afterZoomX = (centerX - panX.value) / newZoom;
  const afterZoomY = (centerY - panY.value) / newZoom;
  
  panX.value += (afterZoomX - beforeZoomX) * newZoom;
  panY.value += (afterZoomY - beforeZoomY) * newZoom;
  
  zoom.value = newZoom;
};

const zoomOut = () => {
  const centerX = svgWidth / 2;
  const centerY = svgHeight / 2;
  
  const beforeZoomX = (centerX - panX.value) / zoom.value;
  const beforeZoomY = (centerY - panY.value) / zoom.value;
  
  const newZoom = Math.max(0.1, zoom.value / 1.2);
  
  const afterZoomX = (centerX - panX.value) / newZoom;
  const afterZoomY = (centerY - panY.value) / newZoom;
  
  panX.value += (afterZoomX - beforeZoomX) * newZoom;
  panY.value += (afterZoomY - beforeZoomY) * newZoom;
  
  zoom.value = newZoom;
};

const resetZoom = () => {
  zoom.value = 1;
  panX.value = 0;
  panY.value = 0;
};

const svgTransform = computed(() => {
  return `translate(${panX.value}, ${panY.value}) scale(${zoom.value})`;
});

const handleEscape = (e: KeyboardEvent) => {
  if (e.key === "Escape" && props.show) {
    emit("close");
  }
};

onMounted(() => {
  document.addEventListener("keydown", handleEscape);
  document.addEventListener("mousemove", handleMouseMove);
  document.addEventListener("mouseup", handleMouseUp);
});

onUnmounted(() => {
  document.removeEventListener("keydown", handleEscape);
  document.removeEventListener("mousemove", handleMouseMove);
  document.removeEventListener("mouseup", handleMouseUp);
});

// Extract unique nodes and find connected groups
const graphData = computed(() => {
  const uniqueNodes = new Set<string>();
  props.connections.forEach((conn) => {
    uniqueNodes.add(conn.from_id);
    uniqueNodes.add(conn.to_id);
  });

  // Build adjacency for grouping
  const adjacency: { [key: string]: Set<string> } = {};
  uniqueNodes.forEach((node) => {
    adjacency[node] = new Set();
  });

  props.connections.forEach((conn) => {
    const fromAdj = adjacency[conn.from_id];
    const toAdj = adjacency[conn.to_id];
    if (fromAdj && toAdj) {
      fromAdj.add(conn.to_id);
      toAdj.add(conn.from_id);
    }
  });

  // Find connected components using BFS
  const visited = new Set<string>();
  const groups: string[][] = [];

  uniqueNodes.forEach((node) => {
    if (!visited.has(node)) {
      const group: string[] = [];
      const queue = [node];
      while (queue.length > 0) {
        const current = queue.shift();
        if (current && !visited.has(current)) {
          visited.add(current);
          group.push(current);
          const neighbors = adjacency[current];
          if (neighbors) {
            neighbors.forEach((neighbor) => {
              if (!visited.has(neighbor)) {
                queue.push(neighbor);
              }
            });
          }
        }
      }
      groups.push(group);
    }
  });

  // Position nodes by group with increased spacing
  const positions: { [key: string]: NodePosition } = {};
  let currentY = 100;

  groups.forEach((group, groupIndex) => {
    // Calculate levels within group based on dependencies
    const levels: { [key: string]: number } = {};
    const inDegree: { [key: string]: number } = {};

    group.forEach((node) => {
      inDegree[node] = 0;
    });

    props.connections.forEach((conn) => {
      if (group.includes(conn.to_id) && group.includes(conn.from_id)) {
        inDegree[conn.to_id] = (inDegree[conn.to_id] || 0) + 1;
      }
    });

    // BFS to assign levels
    const queue = group.filter((n) => inDegree[n] === 0);
    queue.forEach((n) => (levels[n] = 0));

    while (queue.length > 0) {
      const current = queue.shift();
      if (!current) continue;

      props.connections.forEach((conn) => {
        if (conn.from_id === current && group.includes(conn.to_id)) {
          const currentLevel = levels[current] ?? 0;
          const toLevel = levels[conn.to_id] ?? 0;

          if (levels[conn.to_id] === undefined || toLevel <= currentLevel) {
            levels[conn.to_id] = currentLevel + 1;
          }
          inDegree[conn.to_id] = (inDegree[conn.to_id] || 1) - 1;
          if (inDegree[conn.to_id] === 0) {
            queue.push(conn.to_id);
          }
        }
      });
    }

    // Assign remaining nodes
    group.forEach((node) => {
      if (levels[node] === undefined) {
        levels[node] = 0;
      }
    });

    // Group by level
    const levelGroups: { [key: number]: string[] } = {};
    group.forEach((node) => {
      const level = levels[node] ?? 0;
      if (!levelGroups[level]) levelGroups[level] = [];
      levelGroups[level].push(node);
    });

    const levelKeys = Object.keys(levelGroups)
      .map(Number)
      .sort((a, b) => a - b);
    const groupStartY = currentY;

    levelKeys.forEach((level, levelIndex) => {
      const nodesAtLevel = levelGroups[level];
      if (!nodesAtLevel) return;

      const levelWidth = nodesAtLevel.length * 280; // Increased spacing
      const startX = (svgWidth - levelWidth) / 2 + 140;

      nodesAtLevel.forEach((node, nodeIndex) => {
        positions[node] = {
          id: node,
          x: startX + nodeIndex * 280, // Increased spacing
          y: groupStartY + levelIndex * 180, // Increased spacing
        };
      });
    });

    currentY = groupStartY + levelKeys.length * 180 + 80;

    // Add separator line for groups
    if (groupIndex < groups.length - 1) {
      currentY += 50;
    }
  });

  return { nodePositions: positions, connectedGroups: groups };
});

const nodePositions = computed(() => graphData.value.nodePositions);
const connectedGroups = computed(() => graphData.value.connectedGroups);

const formatNodeName = (name: string) => {
  return name.replace(/_/g, " ");
};

// Phase color mapping
const phaseColors: { [key: string]: { fill: string; stroke: string; glow: string } } = {
  'Phase-1': { fill: '#fef3c7', stroke: '#f59e0b', glow: '#fbbf24' },
  'Phase-2': { fill: '#dbeafe', stroke: '#3b82f6', glow: '#60a5fa' },
  'Phase-3': { fill: '#dcfce7', stroke: '#10b981', glow: '#34d399' },
  'Phase-4': { fill: '#fce7f3', stroke: '#ec4899', glow: '#f472b6' },
  'Phase-5': { fill: '#f3e8ff', stroke: '#a855f7', glow: '#c084fc' },
  'Phase-6': { fill: '#ffedd5', stroke: '#f97316', glow: '#fb923c' },
};

// Extract phase from node's connections context
const getNodePhase = (nodeId: string): string | null => {
  const connections = props.connections.filter(
    (conn) => conn.from_id === nodeId || conn.to_id === nodeId
  );
  
  for (const conn of connections) {
    if (conn.context) {
      const phaseMatch = conn.context.match(/\(Phase-(\d+)\)/i);
      if (phaseMatch) {
        return `Phase-${phaseMatch[1]}`;
      }
    }
  }
  
  return null;
};

// Get color for a node based on its phase
const getNodeColor = (nodeId: string, isHovered: boolean, isConnected: boolean) => {
  const phase = getNodePhase(nodeId);
  
  if (phase && phaseColors[phase]) {
    const colors = phaseColors[phase];
    return {
      fill: colors.fill,
      stroke: isHovered ? colors.glow : colors.stroke,
      innerDot: colors.stroke,
      glow: colors.glow,
    };
  }
  
  // Default colors
  return {
    fill: 'white',
    stroke: isHovered ? '#8b5cf6' : isConnected ? '#3b82f6' : '#e5e7eb',
    innerDot: isHovered ? '#8b5cf6' : '#3b82f6',
    glow: '#8b5cf6',
  };
};

// Get connections for a node
const getNodeConnections = (nodeId: string) => {
  return props.connections.filter(
    (conn) => conn.from_id === nodeId || conn.to_id === nodeId
  );
};

// Group connections by from-to pair to handle parallel lines
const connectionGroups = computed(() => {
  const groups: { [key: string]: Connection[] } = {};
  props.connections.forEach((conn) => {
    const key = [conn.from_id, conn.to_id].sort().join("--");
    if (!groups[key]) groups[key] = [];
    groups[key].push(conn);
  });
  return groups;
});

// Get highlighted state for a connection
const isConnectionHighlighted = (conn: Connection) => {
  return hoveredNode.value === conn.from_id || hoveredNode.value === conn.to_id;
};

// Get phase from connection context
const getConnectionPhase = (conn: Connection): string | null => {
  if (conn.context) {
    const phaseMatch = conn.context.match(/\(Phase-(\d+)\)/i);
    if (phaseMatch) {
      return `Phase-${phaseMatch[1]}`;
    }
  }
  return null;
};

// Get color for a connection based on its phase
const getConnectionColor = (conn: Connection, isHighlighted: boolean) => {
  const phase = getConnectionPhase(conn);
  
  if (phase && phaseColors[phase]) {
    const colors = phaseColors[phase];
    return {
      stroke: isHighlighted ? colors.glow : colors.stroke,
      labelStroke: colors.stroke,
      labelFill: colors.stroke,
    };
  }
  
  // Default colors
  return {
    stroke: isHighlighted ? '#8b5cf6' : '#3b82f6',
    labelStroke: isHighlighted ? '#8b5cf6' : '#e5e7eb',
    labelFill: isHighlighted ? '#8b5cf6' : '#3b82f6',
  };
};

// Get path data for a connection
const getConnectionPath = (conn: Connection, index: number, total: number) => {
  const from = nodePositions.value[conn.from_id];
  const to = nodePositions.value[conn.to_id];
  if (!from || !to) return null;
  return getPath(from, to, index, total);
};

// Check if node is connected to hovered node
const isNodeConnectedToHovered = (nodeId: string) => {
  if (!hoveredNode.value) return false;
  const nodeConnections = getNodeConnections(nodeId);
  return nodeConnections.some(
    (c) => c.from_id === hoveredNode.value || c.to_id === hoveredNode.value
  );
};
const getPath = (
  from: NodePosition,
  to: NodePosition,
  index: number,
  total: number
) => {
  const dx = to.x - from.x;
  const dy = to.y - from.y;

  // Offset for parallel lines
  const offsetAmount = total > 1 ? (index - (total - 1) / 2) * 18 : 0;

  // Perpendicular offset
  const length = Math.sqrt(dx * dx + dy * dy);
  const perpX = length > 0 ? (-dy / length) * offsetAmount : 0;
  const perpY = length > 0 ? (dx / length) * offsetAmount : 0;

  const startX = from.x + perpX;
  const startY = from.y + perpY;
  const endX = to.x + perpX;
  const endY = to.y + perpY;

  const midX = (startX + endX) / 2;
  const midY = (startY + endY) / 2;

  // Create smooth curves
  if (Math.abs(dy) < 60) {
    // Horizontal-ish connections - arc over/under
    const curveOffset = Math.sign(perpY) * 50 || 50;
    return {
      path: `M ${startX} ${startY} Q ${midX} ${midY - curveOffset} ${endX} ${endY}`,
      labelX: midX,
      labelY: midY - curveOffset / 2 - 10,
    };
  } else {
    // Vertical connections - smooth S-curve
    return {
      path: `M ${startX} ${startY} C ${startX} ${midY} ${endX} ${midY} ${endX} ${endY}`,
      labelX: midX + perpX,
      labelY: midY,
    };
  }
};
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
            <div
              class="flex items-center justify-between px-6 py-4 border-b border-gray-200 bg-white shrink-0"
            >
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
            <div 
              ref="svgContainer"
              class="flex-1 relative overflow-hidden bg-gray-50 select-none"
              @wheel="handleWheel"
              @mousedown="handleContainerMouseDown"
              :class="{ 'cursor-grab': !isPanning, 'cursor-grabbing': isPanning }"
            >
              <!-- Zoom Controls -->
              <div class="absolute top-4 right-4 z-20 flex flex-col gap-2 bg-white rounded-lg shadow-lg p-2 border border-gray-200">
                <button
                  @click="zoomIn"
                  class="p-2 hover:bg-gray-100 rounded transition-colors"
                  title="Zoom In"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="11" y1="8" x2="11" y2="14"></line>
                    <line x1="8" y1="11" x2="14" y2="11"></line>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                </button>
                <button
                  @click="zoomOut"
                  class="p-2 hover:bg-gray-100 rounded transition-colors"
                  title="Zoom Out"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <circle cx="11" cy="11" r="8"></circle>
                    <line x1="8" y1="11" x2="14" y2="11"></line>
                    <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                  </svg>
                </button>
                <button
                  @click="resetZoom"
                  class="p-2 hover:bg-gray-100 rounded transition-colors"
                  title="Reset Zoom"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <path d="M3 12a9 9 0 0 1 9-9 9.75 9.75 0 0 1 6.74 2.74L21 8"></path>
                    <path d="M21 3v5h-5"></path>
                    <path d="M21 12a9 9 0 0 1-9 9 9.75 9.75 0 0 1-6.74-2.74L3 16"></path>
                    <path d="M3 21v-5h5"></path>
                  </svg>
                </button>
                <div class="text-xs text-center text-gray-600 font-mono pt-1 border-t border-gray-200">
                  {{ Math.round(zoom * 100) }}%
                </div>
              </div>

              <!-- Phase Legend -->
              <!-- <div class="absolute top-4 left-4 z-20 bg-white rounded-lg shadow-lg p-3 border border-gray-200">
                <h3 class="text-xs font-bold text-gray-700 mb-2">Phases</h3>
                <div class="space-y-1">
                  <div v-for="(color, phase) in phaseColors" :key="phase" class="flex items-center gap-2">
                    <div class="w-4 h-4 rounded-full border-2" :style="{ backgroundColor: color.fill, borderColor: color.stroke }"></div>
                    <span class="text-[10px] text-gray-600">{{ phase }}</span>
                  </div>
                </div>
              </div> -->

              <svg
                :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
                class="w-full h-full pointer-events-none"
                style="min-height: 600px; min-width: 900px"
              >
                <g :transform="svgTransform" class="pointer-events-auto">
                <defs>
                  <filter
                    id="glow"
                    x="-50%"
                    y="-50%"
                    width="200%"
                    height="200%"
                  >
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
                    <polygon
                      points="0 0, 8 3, 0 6"
                      fill="#3b82f6"
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
                    <polygon points="0 0, 8 3, 0 6" fill="#8b5cf6" />
                  </marker>
                  <!-- Phase-specific arrows -->
                  <marker
                    v-for="(color, phase) in phaseColors"
                    :key="`arrow-${phase}`"
                    :id="`arrow-${phase}`"
                    markerWidth="8"
                    markerHeight="6"
                    refX="7"
                    refY="3"
                    orient="auto"
                  >
                    <polygon points="0 0, 8 3, 0 6" :fill="color.stroke" opacity="0.8" />
                  </marker>
                  <marker
                    v-for="(color, phase) in phaseColors"
                    :key="`arrow-${phase}-highlight`"
                    :id="`arrow-${phase}-highlight`"
                    markerWidth="8"
                    markerHeight="6"
                    refX="7"
                    refY="3"
                    orient="auto"
                  >
                    <polygon points="0 0, 8 3, 0 6" :fill="color.glow" />
                  </marker>
                </defs>

                <!-- Group separators -->
                <g v-if="connectedGroups.length > 1">
                  <g
                    v-for="(group, index) in connectedGroups.slice(0, -1)"
                    :key="`sep-${index}`"
                  >
                    <template v-if="group.every((n) => nodePositions[n])">
                      <line
                        x1="100"
                        :y1="
                          Math.max(
                            ...group.map((n) => nodePositions[n]?.y || 0)
                          ) + 90
                        "
                        :x2="svgWidth - 100"
                        :y2="
                          Math.max(
                            ...group.map((n) => nodePositions[n]?.y || 0)
                          ) + 90
                        "
                        stroke="#e5e7eb"
                        stroke-width="1"
                        stroke-dasharray="8 4"
                      />
                      <text
                        :x="svgWidth / 2"
                        :y="
                          Math.max(
                            ...group.map((n) => nodePositions[n]?.y || 0)
                          ) + 110
                        "
                        text-anchor="middle"
                        class="text-[10px] fill-gray-500"
                      >
                        Separate Connection Group
                      </text>
                    </template>
                  </g>
                </g>

                <!-- Connection lines -->
                <template
                  v-for="(group, groupKey) in connectionGroups"
                  :key="groupKey"
                >
                  <template v-for="(conn, index) in group" :key="conn.line_id">
                    <g v-if="getConnectionPath(conn, index, group.length)">
                      <!-- Line shadow for depth -->
                      <path
                        :d="getConnectionPath(conn, index, group.length)!.path"
                        fill="none"
                        :stroke="getConnectionColor(conn, isConnectionHighlighted(conn)).stroke"
                        :stroke-width="
                          isConnectionHighlighted(conn) ? 4.5 : 1.5
                        "
                        :stroke-opacity="
                          isConnectionHighlighted(conn) ? 1.5 : 0.5
                        "
                      />
                      <!-- Main line -->
                      <path
                        :d="getConnectionPath(conn, index, group.length)!.path"
                        fill="none"
                        :stroke="getConnectionColor(conn, isConnectionHighlighted(conn)).stroke"
                        :stroke-width="
                          isConnectionHighlighted(conn) ? 2.5 : 1.5
                        "
                        :stroke-opacity="
                          isConnectionHighlighted(conn) ? 1 : 0.6
                        "
                        :marker-end="
                          getConnectionPhase(conn)
                            ? isConnectionHighlighted(conn)
                              ? `url(#arrow-${getConnectionPhase(conn)}-highlight)`
                              : `url(#arrow-${getConnectionPhase(conn)})`
                            : isConnectionHighlighted(conn)
                              ? 'url(#arrow-highlight)'
                              : 'url(#arrow)'
                        "
                        class="transition-all duration-300"
                        :filter="
                          isConnectionHighlighted(conn)
                            ? 'url(#glow)'
                            : undefined
                        "
                      />
                      <!-- Line label -->
                      <g
                        :transform="`translate(${getConnectionPath(conn, index, group.length)!.labelX}, ${getConnectionPath(conn, index, group.length)!.labelY})`"
                      >
                        <rect
                          x="-18"
                          y="-10"
                          width="36"
                          height="20"
                          rx="4"
                          :fill="(() => {
                            const phase = getConnectionPhase(conn);
                            return phase && phaseColors[phase] ? phaseColors[phase].fill : 'white';
                          })()"
                          fill-opacity="0.9"
                          :stroke="getConnectionColor(conn, isConnectionHighlighted(conn)).labelStroke"
                          stroke-width="1"
                        />
                        <text
                          text-anchor="middle"
                          dominant-baseline="middle"
                          :class="[
                            'text-[10px] font-mono font-medium transition-all duration-300',
                          ]"
                          :fill="getConnectionColor(conn, isConnectionHighlighted(conn)).labelFill"
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
                    v-if="
                      hoveredNode === pos.id || isNodeConnectedToHovered(pos.id)
                    "
                    :r="hoveredNode === pos.id ? 40 : 32"
                    :fill="getNodeColor(pos.id, hoveredNode === pos.id, isNodeConnectedToHovered(pos.id)).glow"
                    opacity="0.2"
                    class="animate-pulse"
                  />

                  <!-- Main node -->
                  <circle
                    :r="hoveredNode === pos.id ? 28 : 24"
                    :fill="getNodeColor(pos.id, hoveredNode === pos.id, isNodeConnectedToHovered(pos.id)).fill"
                    :stroke="getNodeColor(pos.id, hoveredNode === pos.id, isNodeConnectedToHovered(pos.id)).stroke"
                    :stroke-width="hoveredNode === pos.id ? 3 : 2"
                    class="transition-all duration-300"
                    :filter="hoveredNode === pos.id ? 'url(#glow)' : undefined"
                  />

                  <!-- Inner dot -->
                  <circle
                    :r="hoveredNode === pos.id ? 6 : 5"
                    :fill="getNodeColor(pos.id, hoveredNode === pos.id, isNodeConnectedToHovered(pos.id)).innerDot"
                    class="transition-all duration-300"
                  />

                  <!-- Phase badge (if node has phase) -->
                  <g v-if="getNodePhase(pos.id)">
                    <rect
                      x="12"
                      y="-28"
                      width="32"
                      height="14"
                      rx="7"
                      :fill="getNodeColor(pos.id, false, false).stroke"
                      opacity="0.9"
                    />
                    <text
                      x="28"
                      y="-20"
                      text-anchor="middle"
                      dominant-baseline="middle"
                      class="text-[8px] font-bold fill-white"
                    >
                      {{ getNodePhase(pos.id)?.replace('Phase-', 'P') }}
                    </text>
                  </g>

                  <!-- Label -->
                  <text
                    :y="hoveredNode === pos.id ? 46 : 40"
                    text-anchor="middle"
                    :class="[
                      'text-[10px] font-medium transition-all duration-300 pointer-events-none',
                      hoveredNode === pos.id
                        ? 'fill-purple-600'
                        : isNodeConnectedToHovered(pos.id)
                          ? 'fill-gray-900'
                          : 'fill-gray-600',
                    ]"
                  >
                    {{
                      formatNodeName(pos.id).length > 18
                        ? formatNodeName(pos.id).substring(0, 18) + "..."
                        : formatNodeName(pos.id)
                    }}
                  </text>
                </g>
              </g>
              </svg>

              <!-- Hover tooltip -->
              <div
                v-if="hoveredNode && nodePositions[hoveredNode]"
                class="absolute bg-white border border-gray-200 rounded-xl p-4 shadow-2xl max-w-xs animate-fade-in z-10 opacity-90"
                :style="tooltipStyle"
              >
                <div class="space-y-3">
                  <div class="flex items-center gap-2">
                    <div
                      class="w-3 h-3 rounded-full animate-pulse"
                      :style="{ backgroundColor: getNodeColor(hoveredNode, true, false).innerDot }"
                    />
                    <h3 class="font-semibold text-gray-900 text-sm">
                      {{ formatNodeName(hoveredNode) }}
                    </h3>
                    <span 
                      v-if="getNodePhase(hoveredNode)"
                      class="text-[9px] font-bold px-2 py-0.5 rounded-full"
                      :style="{ 
                        backgroundColor: getNodeColor(hoveredNode, false, false).fill,
                        color: getNodeColor(hoveredNode, false, false).stroke,
                        border: `1px solid ${getNodeColor(hoveredNode, false, false).stroke}`
                      }"
                    >
                      {{ getNodePhase(hoveredNode) }}
                    </span>
                  </div>

                  <div class="space-y-2">
                    <p
                      class="text-[10px] text-gray-600 uppercase tracking-wider"
                    >
                      Connections
                    </p>
                    <div class="space-y-1 overflow-y-auto">
                      <div
                        v-for="conn in getNodeConnections(hoveredNode)"
                        :key="conn.line_id"
                        class="flex items-center gap-1.5 text-xs bg-gray-50 rounded-lg px-2 py-1.5"
                      >
                        <span
                          class="font-mono text-[10px] text-blue-600 font-bold min-w-7"
                        >
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