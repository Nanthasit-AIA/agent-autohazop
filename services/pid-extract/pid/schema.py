from typing import List, Optional
from pydantic import BaseModel, Field

class Equipment(BaseModel):
    id: str
    name: str
    type: str
    context: Optional[str] = None

class Valve(BaseModel):
    id: str
    type: str
    location: Optional[str] = None
    context: Optional[str] = None

class Instrument(BaseModel):
    id: str
    function: str
    location: Optional[str] = None
    context: Optional[str] = None

class UtilityLine(BaseModel):
    utility_type: str
    valves: List[str]
    flow_direction: str
    context: Optional[str] = None

class NodeDefinition(BaseModel):
    node_id: str
    node_name: str
    description: str

class Connection(BaseModel):
    line_id: str
    node: Optional[str] = None
    node_boundary: Optional[str] = None
    from_id: str
    to_id: str
    included_equipment: List[str] = Field(default_factory=list)
    included_lines: List[str] = Field(default_factory=list)
    valves: List[str] = Field(default_factory=list)
    instruments: List[str] = Field(default_factory=list)
    flow_direction: Optional[str] = None
    context: Optional[str] = None

class LineLevelConnection(BaseModel):
    line_id: str
    from_id: str
    to_id: str
    valves: List[str] = Field(default_factory=list)
    instruments: List[str] = Field(default_factory=list)
    flow_direction: Optional[str] = None
    context: Optional[str] = None

class NominalSize(BaseModel):
    value: float
    unit: str

class LineIdParse(BaseModel):
    area_or_unit: Optional[str] = None
    service_code: Optional[str] = None
    line_sequence_number: Optional[str] = None
    piping_class: Optional[str] = None
    insulation_or_design_code: Optional[str] = None
    nominal_size: Optional[NominalSize] = None

class LineLevelDetails(BaseModel):
    line_id: str
    raw_line_label: Optional[str] = None
    line_id_parse: Optional[LineIdParse] = None

class PIDResponse(BaseModel):
    process_description: str
    intention: str
    system_inputs: List[str]
    system_outputs: List[str]
    node_define: List[NodeDefinition] = Field(default_factory=list)
    equipment: List[Equipment]
    valves: List[Valve]
    instruments: List[Instrument]
    utility_lines: List[UtilityLine]
    connections: List[Connection]
    line_level_connections: List[LineLevelConnection] = Field(default_factory=list)
    line_level_details: List[LineLevelDetails] = Field(default_factory=list)

    @staticmethod
    def schema_name() -> str:
        return "PIDResponse"
