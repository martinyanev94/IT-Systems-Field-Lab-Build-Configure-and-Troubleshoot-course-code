# Timed Certification Readiness

This project records mock-assessment results and turns correctness plus confidence into a next study action.

## Run the example

From the repository root:

```bash
python timed-certification-readiness/src/error_log.py
```

## Run tests

Install `pytest` in your environment, then run:

```bash
python -m pytest timed-certification-readiness/tests
```

The program does not perform live assessment grading. Enter the observed result after checking the assessment key; the code organizes the error log and remediation decision.
