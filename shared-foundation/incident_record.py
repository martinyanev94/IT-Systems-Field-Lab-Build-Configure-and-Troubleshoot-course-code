REQUIRED_FIELDS = (
    "symptom",
    "suspected_cause",
    "confirming_test",
    "verification",
    "verification_result",
)

incident = {
    "device": "salesperson smartphone",
    "symptom": "No calls or internet in the new territory",
    "suspected_cause": "Outdated PRL",
    "confirming_test": "Check PRL status or update availability",
    "verification": "Place a call and load a webpage",
    "verification_result": "Call connected; webpage loaded",
}


def assess_record(record):
    """Return whether an incident record has the required evidence."""
    missing = []
    for field in REQUIRED_FIELDS:
        value = record.get(field)
        if not value:
            missing.append(field)
    if missing:
        return f"incomplete: {', '.join(missing)}"
    return "ready for confirmation"


if __name__ == "__main__":
    print(assess_record(incident))
