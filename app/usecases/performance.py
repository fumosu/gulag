from __future__ import annotations

import math
from typing import Optional
from typing import TypedDict

try:  # TODO: ask asottile about this
    from oppai_ng.oppai import OppaiWrapper
except ModuleNotFoundError:
    pass  # utils will handle this for us

from common.utils.calculator import calculate_performances_std, calculate_performances_taiko, calculate_performances_catch, calculate_performances_mania

class DifficultyRating(TypedDict):
    performance: float
    star_rating: float


class StdTaikoCatchScore(TypedDict):
    mods: Optional[int]
    acc: Optional[float]
    combo: Optional[int]
    nmiss: Optional[int]


class ManiaScore(TypedDict):
    mods: Optional[int]
    score: Optional[int]


class ScoreDifficultyParams(TypedDict, total=False):
    # std, taiko, catch
    acc: float
    combo: int
    nmiss: int

    # mania
    score: int


def calculate_performances(
    osu_file_path: str,
    mode: int,
    mods: Optional[int],
    scores: list[ScoreDifficultyParams],
) -> list[DifficultyRating]:
    if mode in (0, 1, 2, 4, 5, 6, 8):
        std_taiko_catch_scores: list[StdTaikoCatchScore] = [
            {
                "mods": mods,
                "acc": score.get("acc"),
                "combo": score.get("combo"),
                "nmiss": score.get("nmiss"),
            }
            for score in scores
        ]

        if mode in (0, 4, 8):
            results = calculate_performances_std(
                osu_file_path=osu_file_path,
                scores=std_taiko_catch_scores,
                mode=mode,
            )
        elif mode in (1, 5):
            results = calculate_performances_taiko(
                osu_file_path=osu_file_path,
                scores=std_taiko_catch_scores,
            )
        elif mode in (2, 6):
            results = calculate_performances_catch(
                osu_file_path=osu_file_path,
                scores=std_taiko_catch_scores,
            )
    elif mode == 3:
        mania_scores: list[ManiaScore] = [
            {
                "mods": mods,
                "score": score.get("score"),
            }
            for score in scores
        ]

        results = calculate_performances_mania(
            osu_file_path=osu_file_path,
            scores=mania_scores,
        )
    else:
        raise NotImplementedError

    return results
