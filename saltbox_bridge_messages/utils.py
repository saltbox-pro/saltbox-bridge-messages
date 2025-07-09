from datetime import datetime, timezone
from typing import Annotated, Literal

from pydantic import PlainSerializer

SaltTgtType = Literal[
    'glob', 'pcre', 'list', 'grain', 'grain_pcre', 'pillar', 'pillar_pcre', 'nodegroup', 'range', 'compound', 'ipcidr'
]


def utc_now() -> datetime:
    return datetime.now(tz=timezone.utc)


def format_iso8601_z(dt: datetime) -> str:
    """
    Format datetime to ISO 8601 with Z-suffix (UTC).
    Example: 2025-04-08T11:39:06.140000Z
    """
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


Iso8601ZDatetime = Annotated[datetime, PlainSerializer(format_iso8601_z, when_used='json')]
