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

class Connection(BaseModel):
    line_id: str
    from_id: str
    to_id: str
    valves: List[str] = Field(default_factory=list)
    instruments: List[str] = Field(default_factory=list)
    context: Optional[str] = None

class PIDResponse(BaseModel):
    process_description: str
    system_inputs: List[str]
    system_outputs: List[str]

    equipment: List[Equipment]
    valves: List[Valve]
    instruments: List[Instrument]
    utility_lines: List[UtilityLine]
    connections: List[Connection]

    @staticmethod
    def schema_name() -> str: 
        return "PIDResponse"
