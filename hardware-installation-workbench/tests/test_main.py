import unittest

from src.main import build_report, verify_build


class VerifyBuildTests(unittest.TestCase):
    def test_all_required_checks_pass(self):
        checks = {
            "power": True,
            "memory": True,
            "storage": True,
            "display": True,
            "cooling": True,
        }
        self.assertEqual(verify_build(checks), {"status": "READY", "failures": []})

    def test_storage_failure_blocks_handoff(self):
        checks = {
            "power": True,
            "memory": True,
            "storage": False,
            "display": True,
            "cooling": True,
        }
        self.assertEqual(
            verify_build(checks),
            {"status": "BLOCKED", "failures": ["storage"]},
        )

    def test_missing_evidence_is_blocked(self):
        checks = {"power": True, "memory": True}
        result = verify_build(checks)
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["failures"], ["storage", "display", "cooling"])

    def test_report_names_failed_checks(self):
        report = build_report({"power": True, "memory": False})
        self.assertIn("Status: BLOCKED", report)
        self.assertIn("memory", report)


if __name__ == "__main__":
    unittest.main()
