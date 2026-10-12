# Network Protocol Diagnostics

This project classifies supplied network evidence. It does not perform live network tests.

## Run

From the project directory, pipe a JSON evidence record to the analyzer:

```sh
printf '%s\n' '{"ip_address":"169.254.10.22","default_gateway":"","hostname_resolves":false,"direct_ip_reachable":false}' | python3 src/main.py
```

The result contains a classification, a ranked hypothesis, and the next confirming test.

## Test

```sh
python3 -m pytest network-protocol-diagnostics/tests
```

The rules evaluate address assignment first, then IP reachability, then DNS evidence. Successful IP and DNS checks move the investigation to the required application service port.
