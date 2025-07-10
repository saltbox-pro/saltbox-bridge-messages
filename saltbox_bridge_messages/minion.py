from typing import Annotated, Any

from pydantic import BaseModel, Field, PositiveInt

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase
from saltbox_bridge_messages.utils import SaltTgtType


class BridgeMinionPresenceMessage(BridgeMessageBase):
    minions: list[str]
    stamp: float


class BridgeMinionGrainsMessage(BridgeMessageBase):
    grains: dict[str, Any]


class GatheredMinionSchema(BaseModel):
    minion_id: str = Field(title='Minion ID')
    master: str = Field(title='Master')


class CoreGatherMinionsRequest(CoreMessageBase):
    tgt: str
    tgt_type: SaltTgtType


class BridgeGatherMinionsResponse(BridgeMessageBase):
    count: Annotated[int, PositiveInt] = Field(title='Minion count', default=0)
    minions: list[GatheredMinionSchema] = Field(title='Minion list (max 100)', default=[])
