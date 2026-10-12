import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from main import rank_first_action, verify_incident


def test_all_required_checks_pass_verifies_incident():
    record = {
        "incident_id": "MW-104",
        "verification_checks": {
            "associated": True,
            "authenticated": True,
            "usable_address": True,
            "gateway_reachable": True,
            "required_service_reachable": True,
        },
        "escalation_conditions": [],
    }

    result = verify_incident(record)

    assert result["status"] == "VERIFIED"
    assert result["failed_checks"] == []


def test_failed_service_check_keeps_incident_open():
    record = {
        "incident_id": "MW-104",
        "verification_checks": {
            "associated": True,
            "authenticated": True,
            "usable_address": True,
            "gateway_reachable": True,
            "required_service_reachable": False,
        },
        "escalation_conditions": [],
    }

    result = verify_incident(record)

    assert result["status"] == "OPEN"
    assert result["failed_checks"] == ["required_service_reachable"]


def test_escalation_takes_priority_over_passing_checks():
    record = {
        "incident_id": "MW-105",
        "verification_checks": {"required_service_reachable": True},
        "escalation_conditions": ["overheating continues after safe load removal"],
    }

    result = verify_incident(record)

    assert result["status"] == "ESCALATE"


def test_wireless_action_follows_recorded_boundary():
    action = rank_first_action(
        "wireless_access_failure",
        {"associated": True, "authenticated": False},
    )

    assert action == "verify authentication settings without exposing the passphrase"
