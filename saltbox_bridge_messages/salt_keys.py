from __future__ import annotations

from pydantic import Field

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase


class SaltKeysRequest(CoreMessageBase):
    minions: list[str] = Field(default=[])


class SaltKeysResponse(BridgeMessageBase):
    minions: list[str] = Field(default=[])
