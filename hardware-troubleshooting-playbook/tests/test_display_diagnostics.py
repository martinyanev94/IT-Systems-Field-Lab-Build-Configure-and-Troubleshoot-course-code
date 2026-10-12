from src.display_diagnostics import classify_symptom, next_display_check


def test_first_failed_check_is_returned_in_order():
    observation = {
        "power": True,
        "input": True,
        "cable": True,
        "output": False,
        "resolution": False,
    }
    assert next_display_check(observation) == "ENABLE_DUPLICATE_OR_EXTEND"


def test_resolution_is_checked_after_output():
    observation = {
        "power": True,
        "input": True,
        "cable": True,
        "output": True,
        "resolution": False,
    }
    assert next_display_check(observation) == "SET_COMPATIBLE_RESOLUTION"


def test_all_checks_lead_to_verification():
    observation = {name: True for name in ("power", "input", "cable", "output", "resolution")}
    assert next_display_check(observation) == "VERIFY_IMAGE"


def test_symptoms_map_to_distinct_branches():
    assert classify_symptom("no signal") == "CHECK_SIGNAL_PATH"
    assert classify_symptom("fuzzy image") == "ADJUST_PROJECTOR_LENS"
    assert classify_symptom("dim image") == "CHECK_PROJECTOR_BULB"
    assert classify_symptom("intermittent reboot") == "CHECK_VENTS_AND_FAN"


def test_unknown_symptom_preserves_the_evidence_boundary():
    assert classify_symptom("strange behavior") == "RECORD_MORE_DISPLAY_EVIDENCE"
