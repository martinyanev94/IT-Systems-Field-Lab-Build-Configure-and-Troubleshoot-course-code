import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from main import ClientObservation, build_report, evaluate_client


EXPECTED_GATEWAY = "192.168.10.1"


def test_gateway_and_upstream_both_pass():
    assert evaluate_client("192.168.10.24", EXPECTED_GATEWAY, True, True, EXPECTED_GATEWAY) == "VERIFIED"


def test_gateway_pass_upstream_fail_is_upstream_failure():
    assert evaluate_client("192.168.10.24", EXPECTED_GATEWAY, True, False, EXPECTED_GATEWAY) == "UPSTREAM_FAILURE"


def test_apipa_and_missing_gateway_are_local_failure():
    assert evaluate_client("169.254.10.1", "", False, False, EXPECTED_GATEWAY) == "LOCAL_FAILURE"


def test_invalid_address_is_local_failure():
    assert evaluate_client("not-an-ip", EXPECTED_GATEWAY, True, True, EXPECTED_GATEWAY) == "LOCAL_FAILURE"


def test_mismatched_gateway_is_local_failure():
    assert evaluate_client("192.168.10.24", "192.168.10.254", True, True, EXPECTED_GATEWAY) == "LOCAL_FAILURE"


def test_report_preserves_medium_and_observations():
    report = build_report(
        [ClientObservation("Lee", "wireless", "192.168.10.24", EXPECTED_GATEWAY, True, False)],
        expected_gateway=EXPECTED_GATEWAY,
    )
    assert report == [
        {
            "client": "Lee",
            "medium": "wireless",
            "ip_address": "192.168.10.24",
            "gateway": EXPECTED_GATEWAY,
            "gateway_ping": True,
            "upstream_ping": False,
            "status": "UPSTREAM_FAILURE",
        }
    ]
