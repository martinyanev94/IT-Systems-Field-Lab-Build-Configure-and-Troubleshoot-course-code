from __future__ import annotations

from typing import Any


def rank_first_action(symptom: str, evidence: dict[str, Any]) -> str:
    """Return a safe first action for a small mobile or wireless incident."""
    if symptom == "overheating":
        return "stop hotspot or heavy load, move the device to a safe state, and inspect battery evidence"
    if symptom == "charging_failure":
        if not evidence.get("charger_rating_verified", False):
            return "verify charger power rating and inspect the cable and charging path"
        return "compare with a known-good compatible charger and cable"
    if symptom == "bluetooth_pairing_failure":
        if not evidence.get("bluetooth_enabled", False):
            return "enable Bluetooth on both devices"
        return "put the accessory into discoverable mode and scan for it"
    if symptom == "wireless_access_failure":
        if not evidence.get("associated", False):
            return "verify SSID selection and wireless association"
        if not evidence.get("authenticated", False):
            return "verify authentication settings without exposing the passphrase"
        return "test the device address, gateway, and required service in order"
    return "record the symptom and choose a confirming test"


def verify_incident(record: dict[str, Any]) -> dict[str, Any]:
    """Classify a repaired incident from recorded evidence.

    This function evaluates supplied observations. It does not inspect live hardware,
    perform network tests, or prove that a repair happened.
    """
    checks = record.get("verification_checks", {})
    escalation = record.get("escalation_conditions", [])
    failed_checks = [name for name, passed in checks.items() if not passed]

    if escalation:
        status = "ESCALATE"
    elif failed_checks:
        status = "OPEN"
    else:
        status = "VERIFIED"

    return {
        "incident_id": record.get("incident_id", ""),
        "status": status,
        "failed_checks": failed_checks,
        "escalation_conditions": list(escalation),
    }


def example_incident() -> dict[str, Any]:
    return {
        "incident_id": "MW-104",
        "symptom": "wireless_access_failure",
        "verification_checks": {
            "associated": True,
            "authenticated": True,
            "usable_address": True,
            "gateway_reachable": True,
            "required_service_reachable": True,
        },
        "escalation_conditions": [],
    }


if __name__ == "__main__":
    result = verify_incident(example_incident())
    print(result)
