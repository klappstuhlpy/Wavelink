from __future__ import annotations

from typing import TYPE_CHECKING, TypedDict, Any

from .state import VoiceState

from typing_extensions import NotRequired


class Filters(TypedDict):
    ...


class _BaseRequest(TypedDict, total=False):
    voice: NotRequired[VoiceState]
    position: NotRequired[int | float]
    endTime: NotRequired[int]
    volume: NotRequired[int]
    paused: NotRequired[bool]
    filters: NotRequired[dict[str, Any]]
    voice: NotRequired[VoiceState]


class EncodedTrackRequest(_BaseRequest):
    encodedTrack: str | None


class IdentifierRequest(_BaseRequest):
    identifier: str


Request = _BaseRequest | EncodedTrackRequest | IdentifierRequest
