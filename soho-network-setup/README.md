# SOHO Network Setup

This project records and validates the basic configuration for a small office router.
It checks the LAN gateway, DHCP scope, reserved addresses, wireless identity, and
security status without storing a real wireless passphrase or administrator password.

## Run the configuration check

From the repository root:

```bash
python3 soho-network-setup/src/main.py
```

Expected result for the included example:

```text
READY
Gateway: 192.168.10.1
DHCP: 192.168.10.100 - 192.168.10.149
SSID: Northstar-Office
Security: WPA2-Personal
```

## Run tests

From the repository root:

```bash
python3 -m unittest discover -s soho-network-setup/tests
```

The project is a planning and validation record. It does not connect to or modify a
physical router. Enter the approved values in the router interface, then verify wired
and wireless clients in the following lesson.
