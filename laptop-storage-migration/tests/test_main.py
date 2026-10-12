import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from main import MigrationVerification, build_report


def test_complete_verification_is_verified():
    verification = MigrationVerification("Replacement SSD", True, True)
    report = build_report(verification)
    assert report["status"] == "verified"
    assert all(report["checks"].values())


def test_wrong_boot_source_requires_investigation():
    verification = MigrationVerification("Replacement SSD", False, True)
    report = build_report(verification)
    assert report["status"] == "investigate"
    assert report["checks"] == {"drive": True, "boot": False, "data": True}


def test_missing_restored_file_requires_investigation():
    verification = MigrationVerification("Replacement SSD", True, False)
    report = build_report(verification)
    assert report["status"] == "investigate"
    assert report["checks"] == {"drive": True, "boot": True, "data": False}
