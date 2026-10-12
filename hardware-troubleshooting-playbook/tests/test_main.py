from src.main import diagnose_cooling_or_expansion, verification_status


def test_thermal_symptom_prioritizes_cooling_path():
    incident = {
        "shutdown_under_load": True,
        "thermal_path_verified": False,
        "display_fault": False,
        "card_path_verified": False,
    }
    assert diagnose_cooling_or_expansion(incident).startswith("Inspect heat sink")


def test_display_symptom_prioritizes_unverified_card_path():
    incident = {
        "shutdown_under_load": False,
        "thermal_path_verified": True,
        "display_fault": True,
        "card_path_verified": False,
    }
    assert "reseat the expansion card" in diagnose_cooling_or_expansion(incident)


def test_verification_requires_original_symptom_retest():
    assert verification_status(True, False, True) == "VERIFIED"
    assert verification_status(True, True, True) == "INCOMPLETE"
    assert verification_status(True, False, False) == "INCOMPLETE"
