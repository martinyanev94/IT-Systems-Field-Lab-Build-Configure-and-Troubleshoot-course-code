"""Interpret wired and wireless SOHO connectivity observations."""

from dataclasses import dataclass
from ipaddress import ip_address


@dataclass(frozen=True)
class ClientObservation:
    name: str
    medium: str
    ip_address: str
    gateway: str
    gateway_ping: bool
    upstream_ping: bool


def evaluate_client(
    ip_address_text: str,
    gateway: str,
    gateway_ping: bool,
    upstream_ping: bool,
    expected_gateway: str,
) -> str:
    """Return the failure boundary supported by validated observations."""
    try:
        client = ip_address(ip_address_text)
        observed_gateway = ip_address(gateway)
        recorded_gateway = ip_address(expected_gateway)
    except ValueError:
        return "LOCAL_FAILURE"

    if any(value.version != 4 for value in (client, observed_gateway, recorded_gateway)):
        return "LOCAL_FAILURE"
    if client.is_link_local or observed_gateway != recorded_gateway:
        return "LOCAL_FAILURE"
    if not gateway_ping:
        return "LOCAL_FAILURE"
    return "VERIFIED" if upstream_ping else "UPSTREAM_FAILURE"


def build_report(
    observations: list[ClientObservation], expected_gateway: str
) -> list[dict[str, object]]:
    """Convert observations into report rows without changing evidence."""
    report = []
    for observation in observations:
        status = evaluate_client(
            observation.ip_address,
            observation.gateway,
            observation.gateway_ping,
            observation.upstream_ping,
            expected_gateway,
        )
        report.append(
            {
                "client": observation.name,
                "medium": observation.medium,
                "ip_address": observation.ip_address,
                "gateway": observation.gateway,
                "gateway_ping": observation.gateway_ping,
                "upstream_ping": observation.upstream_ping,
                "status": status,
            }
        )
    return report


if __name__ == "__main__":
    observations = [
        ClientObservation("Lee", "wireless", "192.168.10.24", "192.168.10.1", True, False),
        ClientObservation("Dana", "wired", "169.254.10.1", "", False, False),
    ]
    for row in build_report(observations, expected_gateway="192.168.10.1"):
        print(row)
