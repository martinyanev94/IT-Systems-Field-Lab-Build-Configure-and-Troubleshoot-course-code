import pytest

from src.error_log import Result, next_action, summarize


def test_correct_high_confidence_is_maintained() -> None:
    result = Result("Q1", "M.2", True, "high", "matched the form-factor statement")
    assert next_action(result) == "maintain"


def test_correct_low_confidence_requires_verification() -> None:
    result = Result("Q3", "flash memory", True, "low", "eliminated two choices")
    assert next_action(result) == "verify with a new question"


def test_wrong_high_confidence_flags_misconception() -> None:
    result = Result("Q2", "RAID", False, "high", "assumed highest fault tolerance")
    assert next_action(result) == "check for a misconception"


def test_summary_contains_the_next_action() -> None:
    result = Result("Q4", "motherboard", False, "low", "rushed the wording")
    assert summarize([result])[0]["next_action"] == "targeted review"


def test_invalid_confidence_is_rejected() -> None:
    with pytest.raises(ValueError):
        Result("Q1", "M.2", True, "certain", "")
