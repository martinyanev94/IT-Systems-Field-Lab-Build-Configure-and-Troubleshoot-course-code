from incident_record import assess_record, incident


def test_complete_incident_is_ready_for_confirmation():
    assert assess_record(incident) == "ready for confirmation"


def test_missing_symptom_is_reported():
    incomplete = dict(incident)
    incomplete["symptom"] = ""
    assert assess_record(incomplete) == "incomplete: symptom"


def test_missing_verification_result_is_reported():
    incomplete = dict(incident)
    incomplete["verification_result"] = ""
    assert assess_record(incomplete) == "incomplete: verification_result"
