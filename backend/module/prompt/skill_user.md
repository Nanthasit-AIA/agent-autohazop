Node definitions (if provided, use these EXACTLY as the authoritative structure for connections[]; if blank, auto-define nodes from the P&ID):
{node_define}

Intention seed (expand into a full operational intention paragraph; do not contradict this):
{intention}

Process description seed (expand into a full process description paragraph; do not contradict this):
{process_description}

Identify all equipment, valves, and instruments; list system inputs and outputs; detail utility lines; build grouped HAZOP node connections and equipment-to-equipment line-level connections as specified above.

For every `context` field, preserve all visible engineering metadata from the P&ID and process description, including valve size, pipe size, line number, piping class/spec, valve rating, normal/fail position, operating pressure, operating temperature, design pressure, design temperature, flow rate, capacity, setpoints, alarms, trips, and interlock actions. Do not invent unavailable values.

Return only the JSON matching the schema.
