# Printer deployment

This project records a narrow next action for common print-output symptoms and keeps deployment blocked until required evidence passes.

## Run

From this directory:

```bash
python src/main.py
```

## Test

From this directory:

```bash
python -m pytest
```

The helper does not perform live printer operations. It produces a documented recommendation; the technician must inspect the device, repeat the controlled print, and record the physical result.
