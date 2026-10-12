from __future__ import annotations


def recommend_print_action(symptom: str) -> str:
    """Return the narrowest documented next action for a print symptom."""
    symptom = symptom.lower()
    if "does not stick" in symptom or "does not bond" in symptom:
        return "inspect_or_replace_fuser"
    if "one side" in symptom or "duplex" in symptom:
        return "verify_duplex_setup"
    if "repeated marks" in symptom:
        return "inspect_drum_and_feed_rollers"
    if "will not feed" in symptom:
        return "check_paper_weight_or_thickness"
    if "jam" in symptom:
        return "inspect_paper_path_for_obstructions"
    return "collect_more_output_evidence"


def deployment_status(checks: dict[str, bool]) -> str:
    """A deployment is ready only when every required check passes."""
    return "READY" if checks and all(checks.values()) else "BLOCKED"


if __name__ == "__main__":
    observations = [
        "text does not stick to the paper",
        "duplex job prints one side",
        "repeated marks on paper",
    ]
    for observation in observations:
        print(observation, "->", recommend_print_action(observation))
    print(deployment_status({"controlled_print": True, "repeat_check": True}))
