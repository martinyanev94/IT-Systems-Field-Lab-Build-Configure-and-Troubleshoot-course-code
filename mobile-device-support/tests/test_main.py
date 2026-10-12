import unittest

from src.main import diagnose_charging


class ChargingDiagnosisTests(unittest.TestCase):
    def test_low_charge_and_unknown_rating_checks_rating_first(self):
        result = diagnose_charging(
            charge_percent=5,
            charger_rating_known=False,
            overheating=False,
        )
        self.assertEqual(result["first_action"], "check the charger power rating")
        self.assertIn("unverified charger", result["evidence"])

    def test_overheating_takes_priority(self):
        result = diagnose_charging(
            charge_percent=5,
            charger_rating_known=False,
            overheating=True,
        )
        self.assertEqual(
            result["first_action"], "stop normal charging and escalate safely"
        )

    def test_known_rating_moves_to_charging_path(self):
        result = diagnose_charging(
            charge_percent=5,
            charger_rating_known=True,
            overheating=False,
        )
        self.assertEqual(result["first_action"], "inspect the charging path")

    def test_charge_percent_must_be_valid(self):
        with self.assertRaises(ValueError):
            diagnose_charging(
                charge_percent=101,
                charger_rating_known=False,
                overheating=False,
            )


if __name__ == "__main__":
    unittest.main()
