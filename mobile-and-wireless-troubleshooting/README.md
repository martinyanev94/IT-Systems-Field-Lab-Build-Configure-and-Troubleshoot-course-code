# Mobile and Wireless Troubleshooting

This project models a small support triage and verification workflow for mobile and wireless incidents. It records observations; it does not inspect live devices or perform live network tests.

## Run the example

From this directory:

```bash
python src/main.py
```

The example represents a repaired wireless incident. Verification requires every recorded check to pass and no escalation condition to exist.

## Run tests

From this directory:

```bash
python -m unittest discover -s tests -v
```

## Decision states

- `VERIFIED`: every required verification check passed and no escalation condition exists.
- `OPEN`: at least one required check failed and no escalation condition exists.
- `ESCALATE`: an explicit safety or support-boundary condition was recorded.

The verification result must be compared with the original symptom. A recommendation, restart, or successful lower-layer test is not proof that the required service works.
