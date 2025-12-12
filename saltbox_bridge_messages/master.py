from __future__ import annotations

from saltbox_bridge_messages.base import CoreMessageBase
from saltbox_bridge_messages.utils import SaltTgtType


class CoreUpdatePillarCacheRequest(CoreMessageBase):
    tgt: str
    tgt_type: SaltTgtType


class CoreEncryptPillarRequest(CoreMessageBase):
    text: str


class CoreEncryptPillarResponse(CoreMessageBase):
    encrypted_text: str
