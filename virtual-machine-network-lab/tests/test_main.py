import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parents[1] / "src"))

from main import run_connectivity_tests


TOPOLOGY = json.loads(
    (Path(__file__).parents[1] / "data" / "topology.json").read_text()
)


def test_complete_virtual_path_is_verified():
    result = run_connectivity_tests(TOPOLOGY)
    assert result["gateway"] is True
    assert result["server_path"] is True
    assert result["status"] == "VERIFIED"


def test_gateway_mismatch_stops_local_path():
    broken = {**TOPOLOGY, "client": {**TOPOLOGY["client"], "gateway": "10.0.0.254"}}
    result = run_connectivity_tests(broken)
    assert result["gateway"] is False
    assert result["server_path"] is False
    assert result["status"] == "LOCAL_FAILURE"
