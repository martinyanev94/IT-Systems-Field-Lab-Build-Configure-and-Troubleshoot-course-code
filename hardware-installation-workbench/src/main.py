"""Post-install verification for a simulated workstation build."""

REQUIRED_CHECKS = ("power", "memory", "storage", "display", "cooling")


def verify_build(checks: dict[str, bool]) -> dict[str, object]:
    """Return a handoff decision and the required checks that failed.

    Missing evidence is treated as a failure so an unchecked subsystem cannot
    accidentally produce a READY result.
    """
    failures = [name for name in REQUIRED_CHECKS if not checks.get(name, False)]
    return {
        "status": "READY" if not failures else "BLOCKED",
        "failures": failures,
    }


def build_report(checks: dict[str, bool]) -> str:
    """Format a compact work-order result for a technician."""
    result = verify_build(checks)
    failure_text = ", ".join(result["failures"]) or "none"
    return f"Status: {result['status']}\nFailed checks: {failure_text}"


if __name__ == "__main__":
    checks = {
        "power": True,
        "memory": True,
        "storage": False,
        "display": True,
        "cooling": True,
    }

    print("Initial verification")
    print(build_report(checks))

    # The storage cable path was corrected and recorded as new evidence.
    checks["storage"] = True

    print("\nVerification after corrective action")
    print(build_report(checks))
