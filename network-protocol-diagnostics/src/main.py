import json
import sys


def analyze(evidence):
    address = evidence.get("ip_address", "")
    gateway = evidence.get("default_gateway", "")

    if address.startswith("169.254.") or not gateway:
        return {
            "classification": "DHCP_FAILURE",
            "hypothesis": "The client lacks a usable DHCP lease or gateway.",
            "next_test": "Renew the DHCP lease and inspect the new IP and gateway.",
        }

    if not evidence.get("direct_ip_reachable", False):
        return {
            "classification": "IP_FAILURE",
            "hypothesis": "The IP path is not reaching the destination.",
            "next_test": "Test the gateway, then test the upstream address path.",
        }

    if not evidence.get("hostname_resolves", False):
        return {
            "classification": "DNS_FAILURE",
            "hypothesis": "The IP path works but hostname resolution fails.",
            "next_test": "Query the configured resolver and inspect the DNS result.",
        }

    return {
        "classification": "IP_AND_DNS_VERIFIED",
        "hypothesis": "Address reachability and name resolution succeeded.",
        "next_test": "Test the required application service port.",
    }


def main():
    evidence = json.load(sys.stdin)
    print(json.dumps(analyze(evidence), indent=2))


if __name__ == "__main__":
    main()
