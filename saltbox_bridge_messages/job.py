from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase
from saltbox_bridge_messages.utils import SaltTgtType


class JobReturnSchema(BaseModel):
    ret: Any
    retcode: int
    jid: str

    model_config = ConfigDict(extra='allow')


class CoreNewJobAsyncRequest(CoreMessageBase):
    hash_name: str


class CoreNewJobRequest(CoreMessageBase):
    tgt: str
    tgt_type: SaltTgtType
    fun: str
    arg: list
    kwarg: dict
    jid: str | None = None


class BridgeNewJobResponse(BridgeMessageBase):
    jid: str
    tgt: str
    tgt_type: SaltTgtType
    fun: str
    arg: list
    kwarg: dict
    returns: dict[str, JobReturnSchema]


class BridgeInventoryDataSavedMessage(BridgeMessageBase):
    jid: str
    minions: list[str]
    path: list[str | int] = Field(
        description='Path to data in job return, str for field, int for list index',
        examples=['return', 'module name', 'chages', 'ret'],
    )
