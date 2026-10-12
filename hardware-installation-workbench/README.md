# Hardware Installation Workbench

This Python simulation records post-install evidence for a workstation and
returns a handoff decision.

## Run the demonstration

From this directory:

```bash
python -m src.main
```

The demonstration first reports `BLOCKED` because storage evidence is false.
It then records the corrected storage connection and reports `READY`.

## Run tests

From this directory:

```bash
python -m unittest discover -s tests -v
```

## Verification rule

The required checks are power, memory, storage, display, and cooling. Every
check must be present and true before the result can be `READY`. Missing
observations are treated as failures so an incomplete checklist cannot close a
work order.
