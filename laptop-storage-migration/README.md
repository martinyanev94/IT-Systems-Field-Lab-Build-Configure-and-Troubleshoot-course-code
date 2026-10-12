# Laptop Storage Migration

A Python simulation for documenting and verifying an HDD-to-SSD migration.

## Run the demonstration

From this directory:

```bash
python src/main.py
```

The demonstration uses three acceptance checks:

1. The installed drive is identified as `Replacement SSD`.
2. The laptop booted from the replacement SSD.
3. A known restored user file opened successfully.

The migration is `verified` only when all three checks are true. Otherwise the report returns `investigate` so the failed evidence can direct the next diagnostic action.

## Run tests

From this directory:

```bash
python -m unittest discover -s tests
```

The simulation does not modify disks or restore real files. It records the evidence a technician would collect after completing the physical migration.
