from __future__ import annotations

from typing import TYPE_CHECKING
from typing import Union

if TYPE_CHECKING:
    from app.objects.beatmap import Beatmap, BeatmapSet


bcrypt: dict[bytes, bytes] = {}  # {bcrypt: md5, ...}
beatmap: dict[Union[str, int], Beatmap] = {}  # {md5: map, id: map, ...}
beatmapset: dict[int, BeatmapSet] = {}  # {bsid: map_set}
discord_code: dict[str, str] = {}  # {code: discord_id} & {discord_id: code}
map_name: dict[int, str] = {}  # {map_id: name}
unsubmitted: set[str] = set()  # {md5, ...}
needs_update: set[str] = set()  # {md5, ...}