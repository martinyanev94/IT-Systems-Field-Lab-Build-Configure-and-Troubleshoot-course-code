from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class Result:
    question: str
    topic: str
    correct: bool
    confidence: str
    reason: str

    def __post_init__(self) -> None:
        if self.confidence not in {"high", "medium", "low"}:
            raise ValueError("confidence must be high, medium, or low")
        if not self.question or not self.topic:
            raise ValueError("question and topic are required")


def next_action(result: Result) -> str:
    if result.correct and result.confidence == "high":
        return "maintain"
    if result.correct:
        return "verify with a new question"
    if result.confidence == "high":
        return "check for a misconception"
    return "targeted review"


def summarize(results: Iterable[Result]) -> list[dict[str, str | bool]]:
    return [
        {
            "question": result.question,
            "topic": result.topic,
            "correct": result.correct,
            "confidence": result.confidence,
            "reason": result.reason,
            "next_action": next_action(result),
        }
        for result in results
    ]


if __name__ == "__main__":
    sample = [
        Result("Q1", "M.2", True, "medium", "eliminated interface-only claims"),
        Result("Q2", "RAID", False, "high", "treated redundancy as highest fault tolerance"),
    ]
    for row in summarize(sample):
        print(row)
