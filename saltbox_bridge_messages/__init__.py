from enum import Enum
from typing import Annotated
from pydantic import AfterValidator, BaseModel, ConfigDict, Field
from typing_extensions import Self  # typing.Self starting from Python 3.11

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
    new = 'new'
    accepted = 'accepted'
    rejected = 'rejected'


class MasterSshPubkeysMixin:
    gitfs_pubkey: SshPubKeyModel = Field(description='OpenSSH formatted public key to authorize GitFS')
    sshfs_pubkey: SshPubKeyModel = Field(description='OpenSSH formatted public key to authorize SSHFS')


class AuthRequestMessage(BaseModel, MasterSshPubkeysMixin):
    master: str
    crypt_pubkey: str = Field(description='Public key for message encryption and verification')


class AuthResponseMessage(BaseModel):
    crypt_pubkey: str = Field(description='Salt.Box Core public key for message encryption and verification')


class MasterStatusMessage(BaseModel):
    master: str
    status: MasterStatus
    is_pubkey_set: bool


class _BusMasterMessage(BaseModel):
    master: str

    model_config = ConfigDict(extra='allow')


class BusMasterMessage(_BusMasterMessage):
    model_config = ConfigDict(extra='ignore')


class EmptyMessage(BusMasterMessage):
    ...
