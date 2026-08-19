<!-- app/components/PipelineGraph.vue -->
<script setup lang="ts">
import { computed, ref } from "vue";

interface RawConnection {
  line_id: string;
  from_id: string;
  to_id: string;
  [key: string]: unknown;
}

interface Connection {
  line_id: string;
  from_id: string;
  to_id: string;
}

interface NodePosition {
  id: string;
  x: number;
  y: number;
  layer: number;
}

const props = defineProps<{
  data: any;
}>();

const emit = defineEmits<{
  (e: "open-modify", instruction: string): void;
}>();

const svgWidth = 1400;
const svgHeight = 900;

/* ----------------- Display mode toggle ----------------- */

type DisplayMode = "line" | "grouped";
const displayMode = ref<DisplayMode>("line");

/* ----------------- Normalize connections ----------------- */

const normalizeConns = (raw: any[]): Connection[] =>
  raw
    .filter(
      (c: any) =>
        c &&
        typeof c.from_id === "string" &&
        typeof c.to_id === "string" &&
        typeof c.line_id === "string" &&
        c.from_id !== c.to_id
    )
    .map((c: any) => ({
      line_id: String(c.line_id),
      from_id: String(c.from_id),
      to_id: String(c.to_id),
    }));

const connections = computed<Connection[]>(() => {
  const d = props.data;
  if (!d) return [];

  if (displayMode.value === "line") {
    const lineConns = Array.isArray(d.line_level_connections) ? d.line_level_connections : [];
    if (lineConns.length > 0) return normalizeConns(lineConns);
    // fall back to grouped if line-level is empty
    return normalizeConns(Array.isArray(d.connections) ? d.connections : []);
  } else {
    const grouped = Array.isArray(d.connections) ? d.connections : [];
    if (grouped.length > 0) return normalizeConns(grouped);
    return normalizeConns(Array.isArray(d.line_level_connections) ? d.line_level_connections : []);
  }
});

const hasLineLevel = computed(() => {
  const d = props.data;
  return d && Array.isArray(d.line_level_connections) && d.line_level_connections.length > 0;
});

const hasGrouped = computed(() => {
  const d = props.data;
  return d && Array.isArray(d.connections) && d.connections.length > 0;
});

/* ----------------- Node set ----------------- */

const nodeIds = computed<string[]>(() => {
  const s = new Set<string>();
  connections.value.forEach((c) => { s.add(c.from_id); s.add(c.to_id); });
  return Array.from(s);
});

/* ----------------- Layer calculation ----------------- */

const layerMap = computed<Record<string, number>>(() => {
  const nodes = nodeIds.value;
  const inDegree = new Map<string, number>();
  const adjacency = new Map<string, string[]>();

  nodes.forEach((n) => { inDegree.set(n, 0); adjacency.set(n, []); });

  connections.value.forEach((c) => {
    const from = c.from_id;
    const to = c.to_id;
    if (!adjacency.has(from)) adjacency.set(from, []);
    adjacency.get(from)!.push(to);
    inDegree.set(to, (inDegree.get(to) ?? 0) + 1);
  });

  const sources = nodes.filter((n) => (inDegree.get(n) ?? 0) === 0);
  const layer = new Map<string, number>();
  const queue: string[] = [];

  if (sources.length === 0) {
    nodes.forEach((n) => layer.set(n, 0));
  } else {
    sources.forEach((s) => { layer.set(s, 0); queue.push(s); });
    while (queue.length) {
      const current = queue.shift()!;
      const currentLayer = layer.get(current) ?? 0;
      adjacency.get(current)!.forEach((n) => {
        if (!layer.has(n)) { layer.set(n, currentLayer + 1); queue.push(n); }
        else if (currentLayer + 1 > layer.get(n)!) { layer.set(n, currentLayer + 1); }
      });
    }
    let maxLayer = 0;
    layer.forEach((v) => { if (v > maxLayer) maxLayer = v; });
    nodes.forEach((n) => { if (!layer.has(n)) layer.set(n, maxLayer + 1); });
  }

  const out: Record<string, number> = {};
  layer.forEach((v, k) => { out[k] = v; });
  return out;
});

/* ----------------- Node positions ----------------- */

const nodePositions = computed<Record<string, NodePosition>>(() => {
  const byLayer: Record<number, string[]> = {};
  nodeIds.value.forEach((id) => {
    const l = layerMap.value[id] ?? 0;
    if (!byLayer[l]) byLayer[l] = [];
    byLayer[l].push(id);
  });

  const layerIndices = Object.keys(byLayer).map(Number);
  const maxLayer = layerIndices.length ? Math.max(...layerIndices) : 0;
  const verticalPadding = 80;
  const usableHeight = svgHeight - verticalPadding * 2;
  const layerCount = maxLayer + 1 || 1;
  const layerSpacing = layerCount > 1 ? usableHeight / (layerCount - 1) : 0;
  const map: Record<string, NodePosition> = {};

  Object.entries(byLayer).forEach(([layerIndexStr, ids]) => {
    const layerIndex = Number(layerIndexStr);
    const count = ids.length;
    const horizontalPadding = 120;
    const usableWidth = svgWidth - horizontalPadding * 2;
    const spacing = count > 1 ? usableWidth / (count - 1) : 0;
    const y = verticalPadding + layerIndex * layerSpacing;
    ids.forEach((id, idx) => {
      const x = count === 1 ? svgWidth / 2 : horizontalPadding + spacing * idx;
      map[id] = { id, x, y, layer: layerIndex };
    });
  });

  return map;
});

/* ----------------- Interaction ----------------- */

const hoveredNode = ref<string | null>(null);

const getNodeConnections = (nodeId: string): Connection[] =>
  connections.value.filter((c) => c.from_id === nodeId || c.to_id === nodeId);

const isNodeConnectedToHovered = (nodeId: string): boolean => {
  if (!hoveredNode.value) return false;
  const h = hoveredNode.value;
  return connections.value.some(
    (c) => (c.from_id === nodeId && c.to_id === h) || (c.to_id === nodeId && c.from_id === h)
  );
};

const formatNodeName = (name: string): string =>
  String(name).replace(/_/g, " ").replace(/(\d+)L/g, "$1L");

/* ----------------- Paths & helpers ----------------- */

interface PathInfo { path: string; labelX: number; labelY: number }

const getPath = (from: NodePosition, to: NodePosition, index: number, total: number): PathInfo => {
  const dx = to.x - from.x;
  const dy = to.y - from.y;
  const offsetAmount = total > 1 ? (index - (total - 1) / 2) * 15 : 0;
  const length = Math.sqrt(dx * dx + dy * dy);
  const perpX = length > 0 ? (-dy / length) * offsetAmount : 0;
  const perpY = length > 0 ? (dx / length) * offsetAmount : 0;
  const startX = from.x + perpX; const startY = from.y + perpY;
  const endX = to.x + perpX; const endY = to.y + perpY;
  const midX = (startX + endX) / 2; const midY = (startY + endY) / 2;
  if (Math.abs(dy) < 50) {
    const curveOffset = Math.sign(perpY) * 40 || 40;
    return { path: `M ${startX} ${startY} Q ${midX} ${midY - curveOffset} ${endX} ${endY}`, labelX: midX, labelY: midY - curveOffset / 2 - 10 };
  }
  return { path: `M ${startX} ${startY} C ${startX} ${midY} ${endX} ${midY} ${endX} ${endY}`, labelX: midX + perpX, labelY: midY };
};

const getLineShadowProps = (conn: Connection, index: number, total: number) => {
  const from = nodePositions.value[conn.from_id]!;
  const to = nodePositions.value[conn.to_id]!;
  const info = getPath(from, to, index, total);
  const isHighlighted = hoveredNode.value === conn.from_id || hoveredNode.value === conn.to_id;
  return { d: info.path, fill: "none", stroke: "hsl(var(--background))", "stroke-width": isHighlighted ? 6 : 4, "stroke-opacity": 0.5 };
};

const getLineMainProps = (conn: Connection, index: number, total: number) => {
  const from = nodePositions.value[conn.from_id]!;
  const to = nodePositions.value[conn.to_id]!;
  const info = getPath(from, to, index, total);
  const isHighlighted = hoveredNode.value === conn.from_id || hoveredNode.value === conn.to_id;
  const review = reviewMap.value[conn.line_id];
  const strokeColor = review === "bad" ? "#ef4444" : review === "ok" ? "#22c55e" : isHighlighted ? "hsl(var(--accent))" : "hsl(var(--primary))";
  return {
    d: info.path,
    fill: "none",
    stroke: strokeColor,
    "stroke-width": isHighlighted ? 2.5 : 1.5,
    "stroke-opacity": isHighlighted ? 1 : 0.7,
    "stroke-dasharray": "8 4",
    "marker-end": isHighlighted ? "url(#arrowhead-highlight)" : (review === "bad" ? "url(#arrowhead-bad)" : review === "ok" ? "url(#arrowhead-ok)" : "url(#arrowhead)"),
    class: "flow-edge transition-all duration-300",
    filter: isHighlighted ? "url(#glow)" : undefined,
  };
};

const getHitProps = (conn: Connection, index: number, total: number) => {
  const from = nodePositions.value[conn.from_id]!;
  const to = nodePositions.value[conn.to_id]!;
  const info = getPath(from, to, index, total);
  return { d: info.path, fill: "none", stroke: "transparent", "stroke-width": 16, class: "cursor-pointer" };
};

const getLabelTransform = (conn: Connection, index: number, total: number) => {
  const from = nodePositions.value[conn.from_id]!;
  const to = nodePositions.value[conn.to_id]!;
  const info = getPath(from, to, index, total);
  return `translate(${info.labelX}, ${info.labelY})`;
};

const getNodeTransform = (nodeId: string) => {
  const pos = nodePositions.value[nodeId]!;
  return `translate(${pos.x}, ${pos.y})`;
};

/* ----------------- Group connections ----------------- */

const connectionGroups = computed<Record<string, Connection[]>>(() => {
  const groups: Record<string, Connection[]> = {};
  connections.value.forEach((conn) => {
    const key = [conn.from_id, conn.to_id].sort().join("--");
    if (!groups[key]) groups[key] = [];
    groups[key].push(conn);
  });
  return groups;
});

/* ----------------- Review marks ----------------- */

type ReviewState = "ok" | "bad" | null;
const reviewMap = ref<Record<string, ReviewState>>({});
const noteMap = ref<Record<string, string>>({});
const editingNoteFor = ref<string | null>(null);

const cycleReview = (lineId: string) => {
  const current = reviewMap.value[lineId] ?? null;
  if (current === null) reviewMap.value[lineId] = "ok";
  else if (current === "ok") reviewMap.value[lineId] = "bad";
  else { reviewMap.value[lineId] = null; delete noteMap.value[lineId]; }
};

const badItems = computed(() =>
  Object.entries(reviewMap.value)
    .filter(([, v]) => v === "bad")
    .map(([id]) => id)
);

const sendIssuesToModify = () => {
  if (!badItems.value.length) return;
  const lines = badItems.value.map((id) => {
    const note = noteMap.value[id];
    return `- ${id}${note ? `: ${note}` : ""}`;
  });
  const instruction = `Fix these connections identified as incorrect during visual review:\n${lines.join("\n")}`;
  emit("open-modify", instruction);
};
</script>

<template>
  <div class="relative w-full h-full bg-slate-50 overflow-auto flex flex-col">
    <!-- Toolbar -->
    <div class="flex items-center gap-2 px-3 py-2 border-b border-gray-200 bg-white flex-shrink-0 flex-wrap">
      <!-- Toggle -->
      <div class="flex rounded-lg overflow-hidden border border-gray-300 text-xs">
        <button
          @click="displayMode = 'line'"
          class="px-3 py-1.5 transition"
          :class="displayMode === 'line' ? 'bg-black text-white' : 'bg-white text-gray-600 hover:bg-gray-50'"
        >Line-level</button>
        <button
          @click="displayMode = 'grouped'"
          class="px-3 py-1.5 transition"
          :class="displayMode === 'grouped' ? 'bg-black text-white' : 'bg-white text-gray-600 hover:bg-gray-50'"
        >Grouped nodes</button>
      </div>

      <span class="text-xs text-gray-400 ml-1">Click an edge to mark ✓ / ✗</span>

      <div class="flex-1"></div>

      <button
        v-if="badItems.length > 0"
        @click="sendIssuesToModify"
        class="px-3 py-1.5 text-xs rounded-lg bg-red-600 text-white hover:bg-red-700 transition"
      >
        Send {{ badItems.length }} issue{{ badItems.length > 1 ? 's' : '' }} to Modify
      </button>
    </div>

    <!-- SVG graph -->
    <div class="flex-1 overflow-auto">
      <svg
        :viewBox="`0 0 ${svgWidth} ${svgHeight}`"
        class="w-full h-full"
        style="min-height: 500px; min-width: 800px"
      >
        <defs>
          <filter id="glow" x="-50%" y="-50%" width="200%" height="200%">
            <feGaussianBlur stdDeviation="4" result="coloredBlur" />
            <feMerge><feMergeNode in="coloredBlur" /><feMergeNode in="SourceGraphic" /></feMerge>
          </filter>
          <marker id="arrowhead" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="hsl(var(--primary))" opacity="0.6" />
          </marker>
          <marker id="arrowhead-highlight" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="hsl(var(--accent))" />
          </marker>
          <marker id="arrowhead-ok" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#22c55e" />
          </marker>
          <marker id="arrowhead-bad" markerWidth="8" markerHeight="6" refX="7" refY="3" orient="auto">
            <polygon points="0 0, 8 3, 0 6" fill="#ef4444" />
          </marker>
        </defs>

        <!-- Connection lines -->
        <g v-for="(group, groupKey) in connectionGroups" :key="groupKey">
          <template v-for="(conn, index) in group" :key="conn.line_id">
            <g>
              <path v-bind="getLineShadowProps(conn, index, group.length)" />
              <path v-bind="getLineMainProps(conn, index, group.length)" />
              <!-- hit zone for click -->
              <path v-bind="getHitProps(conn, index, group.length)" @click="cycleReview(conn.line_id)" />
              <!-- label + review icon -->
              <g :transform="getLabelTransform(conn, index, group.length)">
                <rect x="-20" y="-9" width="40" height="18" rx="4" fill="hsl(var(--card))" fill-opacity="0.9" stroke="hsl(var(--border))" stroke-width="1" />
                <text text-anchor="middle" dominant-baseline="middle" class="text-[8px] font-mono font-medium fill-muted-foreground" :y="reviewMap[conn.line_id] ? -1 : 0">
                  {{ conn.line_id.length > 10 ? conn.line_id.slice(-8) : conn.line_id }}
                </text>
                <text v-if="reviewMap[conn.line_id]" text-anchor="middle" dominant-baseline="middle" :y="6"
                  :style="{ fill: reviewMap[conn.line_id] === 'ok' ? '#22c55e' : '#ef4444', fontSize: '9px', fontWeight: 'bold' }">
                  {{ reviewMap[conn.line_id] === "ok" ? "✓" : "✗" }}
                </text>
              </g>
            </g>
          </template>
        </g>

        <!-- Nodes -->
        <g
          v-for="nodeId in nodeIds"
          :key="nodeId"
          :transform="getNodeTransform(nodeId)"
          class="cursor-pointer"
          @mouseenter="hoveredNode = nodeId"
          @mouseleave="hoveredNode = null"
        >
          <circle v-if="hoveredNode === nodeId || isNodeConnectedToHovered(nodeId)" :r="hoveredNode === nodeId ? 38 : 30" fill="hsl(var(--accent))" opacity="0.2" class="animate-pulse" />
          <circle
            :r="hoveredNode === nodeId ? 26 : 20"
            fill="hsl(var(--card))"
            :stroke="hoveredNode === nodeId ? 'hsl(var(--accent))' : isNodeConnectedToHovered(nodeId) ? 'hsl(var(--primary))' : 'hsl(var(--border))'"
            :stroke-width="hoveredNode === nodeId ? 3 : 2"
            class="transition-all duration-300"
            :filter="hoveredNode === nodeId ? 'url(#glow)' : undefined"
          />
          <circle :r="hoveredNode === nodeId ? 5 : 4" :fill="hoveredNode === nodeId ? 'hsl(var(--accent))' : 'hsl(var(--primary))'" class="transition-all duration-300" />
          <text
            :y="hoveredNode === nodeId ? 42 : 36"
            text-anchor="middle"
            class="text-[10px] font-medium pointer-events-none"
            :class="hoveredNode === nodeId ? 'fill-accent' : isNodeConnectedToHovered(nodeId) ? 'fill-foreground' : 'fill-muted-foreground'"
          >
            {{ formatNodeName(nodeId).length > 18 ? formatNodeName(nodeId).substring(0, 18) + "..." : formatNodeName(nodeId) }}
          </text>
        </g>
      </svg>
    </div>

    <!-- Hover tooltip -->
    <div v-if="hoveredNode" class="absolute top-12 right-4 bg-white border border-gray-200 rounded-xl p-4 shadow-2xl max-w-xs z-10">
      <div class="space-y-3">
        <div class="flex items-center gap-2">
          <div class="w-3 h-3 rounded-full bg-accent animate-pulse" />
          <h3 class="font-semibold text-foreground text-sm">{{ formatNodeName(hoveredNode) }}</h3>
        </div>
        <div class="space-y-2">
          <p class="text-[10px] text-muted-foreground uppercase tracking-wider">Connections</p>
          <div class="space-y-1 max-h-40 overflow-y-auto">
            <div v-for="conn in getNodeConnections(hoveredNode)" :key="conn.line_id" class="flex items-center gap-1.5 text-xs bg-muted/50 rounded-lg px-2 py-1.5">
              <span class="font-mono text-[10px] text-primary font-bold min-w-[28px]">{{ conn.line_id }}</span>
              <span class="text-foreground/70 text-[10px] truncate">{{ formatNodeName(conn.from_id) }}</span>
              <svg class="w-3 h-3 text-accent flex-shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3" />
              </svg>
              <span class="text-foreground/70 text-[10px] truncate">{{ formatNodeName(conn.to_id) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Note input for bad items -->
    <div v-if="badItems.length > 0" class="flex-shrink-0 border-t border-gray-100 px-3 py-2 bg-white">
      <p class="text-xs text-gray-500 mb-1">Add notes for flagged connections (optional):</p>
      <div v-for="id in badItems" :key="id" class="flex items-center gap-2 mb-1">
        <span class="text-xs text-red-500 font-mono w-32 truncate">✗ {{ id }}</span>
        <input
          :value="noteMap[id] ?? ''"
          @input="noteMap[id] = ($event.target as HTMLInputElement).value"
          type="text"
          placeholder="note (optional)"
          class="flex-1 text-xs border border-gray-200 rounded px-2 py-0.5 focus:outline-none"
        />
      </div>
    </div>
  </div>
</template>

<style scoped>
@keyframes flow {
  from { stroke-dashoffset: 24; }
  to   { stroke-dashoffset: 0; }
}
.flow-edge {
  animation: flow 1.2s linear infinite;
}
</style>
