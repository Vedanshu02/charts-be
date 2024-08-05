from pydantic import BaseModel, ConfigDict
from typing import Optional


class PlotsSchema(BaseModel):
    id: int
    fc_name: str
    fc_ns: str
    fc_ts:int    
    
    model_config=ConfigDict(from_attributes=True)

class PlotsCreateRequestSchema(BaseModel):

    fc_name: str
    fc_ns: str
    fc_ts:int    
    
    model_config=ConfigDict(from_attributes=True)
