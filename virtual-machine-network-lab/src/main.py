from __future__ import annotations

import json
from pathlib import Path


def load_topology(path: str | Path) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def run_connectivity_tests(topology: dict) -> dict:
    client = topology["client"]
    router = topology["router"]
    server = topology["server"]

    gateway_match = client["gateway"] == router["gateway"]
    gateway_reachable = (
        gateway_match
        and client["interface"]
        and router["lan_interface"]
    )
    server_reachable = (
        bool(gateway_reachable)
        and server["interface"] == "eth0"
    )
    status = "VERIFIED" if server_reachable else "LOCAL_FAILURE"

    return {
        "client": client["name"],
        "router": router["name"],
        "server": server["name"],
        "gateway": bool(gateway_reachable),
        "server_path": bool(server_reachable),
        "status": status,
        "observations": [
            f"client gateway={client['gateway']}",
            f"router LAN={router['gateway']}",
            f"server interface={server['interface']}",
        ],
    }


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    topology = load_topology(root / "data" / "topology.json")
    print(json.dumps(run_connectivity_tests(topology), indent=2))


if __name__ == "__main__":
    main()
