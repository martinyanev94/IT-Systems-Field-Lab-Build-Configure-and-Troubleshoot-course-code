"""Deterministic display and projector troubleshooting rules."""

from __future__ import annotations

from typing import Mapping


CHECKS = ("power", "input", "cable", "output", "resolution")


def next_display_check(observation: Mapping[str, bool]) -> str:
    """Return the first unresolved display-path check.

    The function evaluates recorded observations only. It does not inspect
    physical hardware or prove that a corrective action succeeded.
    """
    for check in CHECKS:
        if not observation.get(check, False):
            return {
                "power": "CHECK_POWER",
                "input": "SELECT_INPUT",
                "cable": "REPLACE_OR_RESEAT_CABLE",
                "output": "ENABLE_DUPLICATE_OR_EXTEND",
                "resolution": "SET_COMPATIBLE_RESOLUTION",
            }[check]
    return "VERIFY_IMAGE"


def classify_symptom(symptom: str) -> str:
    """Map a reported display symptom to its first diagnostic branch."""
    normalized = symptom.strip().lower()
    if normalized == "no signal":
        return "CHECK_SIGNAL_PATH"
    if normalized == "fuzzy image":
        return "ADJUST_PROJECTOR_LENS"
    if normalized == "dim image":
        return "CHECK_PROJECTOR_BULB"
    if normalized in {"flicker", "discoloration"}:
        return "CHECK_CABLE_CONNECTION"
    if normalized == "intermittent reboot":
        return "CHECK_VENTS_AND_FAN"
    if normalized in {"cut off image", "distorted image"}:
        return "CHECK_OUTPUT_RESOLUTION"
    return "RECORD_MORE_DISPLAY_EVIDENCE"


if __name__ == "__main__":
    example = {
        "power": True,
        "input": True,
        "cable": True,
        "output": False,
        "resolution": False,
    }
    print(next_display_check(example))
    print(classify_symptom("no signal"))
