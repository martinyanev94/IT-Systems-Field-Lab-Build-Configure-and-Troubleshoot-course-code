# Hardware Troubleshooting Playbook

A small Python decision helper for recording evidence about thermal and expansion-card symptoms.

## Run

From this directory:

```bash
python src/main.py
```

## Test

From this directory, with pytest installed:

```bash
python -m pytest
```

The helper provides recommendations from supplied observations. It does not inspect live hardware or prove that a repair succeeded; verification requires repeating the original symptom test and recording its result.
