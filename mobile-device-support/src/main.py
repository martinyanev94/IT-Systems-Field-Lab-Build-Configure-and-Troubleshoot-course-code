"""Decision helper for mobile charging and battery symptoms."""

from __future__ import annotations

import argparse
import json


def diagnose_charging(
    *, charge_percent: int, charger_rating_known: bool, overheating: bool
) -> dict[str, str]:
    """Return a ranked first action and the evidence behind it."""
    if not 0 <= charge_percent <= 100:
        raise ValueError("charge_percent must be between 0 and 100")

    if overheating:
        return {
            "first_action": "stop normal charging and escalate safely",
            "evidence": "overheating is present",
            "next_check": "inspect battery, charger, cable, and active load",
        }

    if charge_percent <= 5 and not charger_rating_known:
        return {
            "first_action": "check the charger power rating",
            "evidence": "very low charge with an unverified charger",
            "next_check": "continue diagnosis only after rating is confirmed",
        }

    return {
        "first_action": "inspect the charging path",
        "evidence": "the first charger check did not explain the symptom",
        "next_check": "separate cable, battery, and device causes",
    }


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Rank the first action for a mobile charging symptom."
    )
    parser.add_argument("--charge-percent", type=int, required=True)
    parser.add_argument("--charger-rating-known", action="store_true")
    parser.add_argument("--overheating", action="store_true")
    args = parser.parse_args()

    result = diagnose_charging(
        charge_percent=args.charge_percent,
        charger_rating_known=args.charger_rating_known,
        overheating=args.overheating,
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
