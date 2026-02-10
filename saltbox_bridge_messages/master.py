from __future__ import annotations

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase
from saltbox_bridge_messages.utils import SaltTgtType


class CoreUpdatePillarCacheRequest(CoreMessageBase):
    tgt: str
    tgt_type: SaltTgtType


class CoreEncryptPillarRequest(CoreMessageBase):
    text: str


class CoreEncryptPillarResponse(CoreMessageBase):
    encrypted_text: str


class BridgePillarDataRequest(BridgeMessageBase):
    minion_id: str
    pillarenv: str


class CorePillarDataResponse(CoreMessageBase):
    data: dict
