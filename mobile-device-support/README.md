# Mobile Device Support Decision Helper

This Python project records a first diagnostic action for mobile charging and battery symptoms.

## Run the example

From the `mobile-device-support` directory:

```bash
python3 src/main.py --charge-percent 5
```

The example represents a phone at 5 percent with an unverified charger. The expected first action is to check the charger power rating.

To model overheating, add the flag:

```bash
python3 src/main.py --charge-percent 5 --overheating
```

To indicate that the charger rating has already been confirmed, add `--charger-rating-known`.

## Run tests

From the `mobile-device-support` directory:

```bash
python3 -m unittest discover -s tests
```

The helper is a diagnostic teaching simulation. It does not measure electrical output or replace device-specific service guidance. It returns evidence and a next check so a technician can record what was observed and verify whether the original symptom changed.
