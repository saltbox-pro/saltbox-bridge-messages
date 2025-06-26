from datetime import timedelta
from enum import Enum
from typing import Annotated

from pydantic import AfterValidator, BaseModel, Field
from typing_extensions import Self  # typing.Self starting from Python 3.11

from saltbox_bridge_messages.base import BridgeMessageBase, CoreMessageBase


def validate_ssh_pubkey_token(value: str) -> str:
    if not value.isascii() or ' ' in value:
        msg = 'Expected ASCII string with no space symbols'
        raise ValueError(msg)
    return value


def validate_is_ascii(value: str) -> str:
    if not value.isascii():
        msg = 'Expected ASCII string'
        raise ValueError(msg)
    return value


SshPubKeyToken = Annotated[str, AfterValidator(validate_ssh_pubkey_token)]
AsciiStr = Annotated[str, AfterValidator(validate_is_ascii)]


class SshPubKeyModel(BaseModel):
    type_name: SshPubKeyToken
    public_key: SshPubKeyToken
    comment: AsciiStr = ''

    def __str__(self) -> str:
        result = f'{self.type_name} {self.public_key}'
        if self.comment:
            result = f'{result} {self.comment}'
        return result

    @classmethod
    def from_str(cls, value: str) -> Self:
        tokens = value.split(' ', maxsplit=2)
        if 2 > len(tokens) > 3:
            msg = 'Unexpected OpenSSH public key string'
            raise ValueError(msg)
        try:
            comment = tokens[2]
        except IndexError:
            comment = ''
        return cls(type_name=tokens[0], public_key=tokens[1], comment=comment)


# FIXME (a.karmanov): Normalize enum
class MasterStatus(str, Enum):
    NEW = 'new'
    ACCEPTED = 'accepted'
    REJECTED = 'rejected'
    KEYS_STALE = 'keys_stale'  # Master needs keys rotation


class BridgeAuthRequest(BridgeMessageBase):
    crypt_pubkey: str = Field(description='Public key for message encryption and verification')
    salt_conf_pubkey: SshPubKeyModel = Field(description='OpenSSH formatted public key to authorize GitFS')
    sshfs_pubkey: SshPubKeyModel = Field(description='OpenSSH formatted public key to authorize SSHFS')


class CoreAuthResponse(CoreMessageBase):
    crypt_pubkey: str = Field(description='Salt.Box Core public key for message encryption and verification')
    status: MasterStatus


class CoreTestBurstRequest(CoreMessageBase):
    count: int
    size: int = 0


class BridgeTestBurstLoadMessage(BridgeMessageBase):
    load: str | None = None


class BridgeTestBurstResponse(BridgeMessageBase):
    time: timedelta
