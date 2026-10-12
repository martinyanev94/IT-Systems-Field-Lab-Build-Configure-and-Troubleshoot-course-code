"""Rule-based hardware troubleshooting helper."""

from typing import Mapping


def diagnose_cooling_or_expansion(observation: Mapping[str, bool]) -> str:
    """Return the next controlled action from recorded observations."""
    if observation["shutdown_under_load"] and not observation["thermal_path_verified"]:
        return "Inspect heat sink contact, dust, and airflow; then repeat the load test."
    if observation["display_fault"] and not observation["card_path_verified"]:
        return "Power down, reseat the expansion card, check auxiliary power, and retest display output."
    return "Record the original symptom and choose the next evidence-based check."


def verification_status(
    original_shutdown: bool,
    repeated_shutdown: bool,
    thermal_path_verified: bool,
) -> str:
    """Require both path evidence and a retest against the original symptom."""
    if thermal_path_verified and original_shutdown and not repeated_shutdown:
        return "VERIFIED"
    return "INCOMPLETE"


if __name__ == "__main__":
    incident = {
        "shutdown_under_load": True,
        "thermal_path_verified": False,
        "display_fault": False,
        "card_path_verified": False,
    }
    print(diagnose_cooling_or_expansion(incident))
    print(verification_status(True, False, True))
