from __future__ import annotations

from typing import Any
from pydantic import BaseModel, ConfigDict

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase
from saltbox_bridge_messages.utils import SaltTgtType


#class JobReturn(BaseModel):
class JobReturnSchema(BaseModel):
    ret: Any
    retcode: int
    jid: str

    model_config = ConfigDict(extra='allow')


#class NewJobIneMessage(BridgeMessageBase):
class CoreNewJobAsyncRequest(CoreMessageBase):
    hash_name: str


#class NewJobSyncIneMessage(BridgeMessageBase):
class CoreNewJobRequest(CoreMessageBase):
    tgt: str
    tgt_type: SaltTgtType
    fun: str
    arg: list
    kwarg: dict
    jid: str | None = None


#class JobSyncOutMessage(BridgeMessageBase):
class BridgeNewJobResponce(BridgeMessageBase):
    jid: str
    tgt: str
    tgt_type: SaltTgtType
    fun: str
    arg: list
    kwarg: dict
    returns: dict[str, JobReturnSchema]
