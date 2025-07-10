from datetime import datetime, timezone
from typing import Annotated, Any, Literal

from pydantic import AfterValidator, PlainSerializer

SaltTgtType = Literal[
    'glob', 'pcre', 'list', 'grain', 'grain_pcre', 'pillar', 'pillar_pcre', 'nodegroup', 'range', 'compound', 'ipcidr'
]


def utc_now() -> datetime:
    return datetime.now(tz=timezone.utc)


def make_aware(value: Any) -> Any:
    if isinstance(value, datetime) and value.tzinfo is None:
        value = value.replace(tzinfo=timezone.utc)
    return value


def format_iso8601_z(dt: datetime) -> str:
    """
    Format datetime to ISO 8601 with Z-suffix (UTC).
    Example: 2025-04-08T11:39:06.140000Z
    """
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


Iso8601ZDatetime = Annotated[
    datetime,
    AfterValidator(make_aware),
    PlainSerializer(format_iso8601_z, when_used='json'),
    'Aware datetime serializing with Z-suffix. Unaware datetime decides UTC.'
]
