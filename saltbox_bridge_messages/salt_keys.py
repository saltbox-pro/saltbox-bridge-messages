from __future__ import annotations

from enum import Enum

from pydantic import Field

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase


class SaltKeyStatusType(str, Enum):
    accepted = 'accepted'
    unaccepted = 'unaccepted'
    rejected = 'rejected'
    denied = 'denied'


class SaltKeysRequest(CoreMessageBase):
    minions: list[str] = Field(default=[])


class SaltKeysResponse(BridgeMessageBase):
    minions: list[str] = Field(default=[])


class SaltListKeysRequest(CoreMessageBase):
    status: SaltKeyStatusType | None = Field(default=None)


class SaltListKeysResponse(BridgeMessageBase):
    salt_keys: dict[SaltKeyStatusType, list[str]] = Field(default={})
