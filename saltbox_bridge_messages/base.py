from pydantic import BaseModel

class CoreMessageBase(BaseModel):
    master: str

class BridgeMessageBase(BaseModel):
    master: str

class CoreEmptyMessage(CoreMessageBase):
    ...
