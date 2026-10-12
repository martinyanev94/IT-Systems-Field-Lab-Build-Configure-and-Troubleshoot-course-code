from src.main import analyze


def test_apipa_and_missing_gateway_identifies_dhcp_failure():
    result = analyze({
        "ip_address": "169.254.10.22",
        "default_gateway": "",
        "hostname_resolves": False,
        "direct_ip_reachable": False,
    })
    assert result["classification"] == "DHCP_FAILURE"
    assert "Renew" in result["next_test"]


def test_failed_direct_ip_path_precedes_dns_classification():
    result = analyze({
        "ip_address": "192.168.10.44",
        "default_gateway": "192.168.10.1",
        "hostname_resolves": False,
        "direct_ip_reachable": False,
    })
    assert result["classification"] == "IP_FAILURE"


def test_failed_hostname_resolution_after_ip_success_is_dns_failure():
    result = analyze({
        "ip_address": "192.168.10.44",
        "default_gateway": "192.168.10.1",
        "hostname_resolves": False,
        "direct_ip_reachable": True,
    })
    assert result["classification"] == "DNS_FAILURE"


def test_successful_ip_and_dns_moves_to_service_test():
    result = analyze({
        "ip_address": "192.168.10.44",
        "default_gateway": "192.168.10.1",
        "hostname_resolves": True,
        "direct_ip_reachable": True,
    })
    assert result["classification"] == "IP_AND_DNS_VERIFIED"
    assert "service port" in result["next_test"]
