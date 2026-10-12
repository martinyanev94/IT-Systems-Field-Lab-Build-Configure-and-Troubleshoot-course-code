from dataclasses import dataclass


@dataclass
class MigrationVerification:
    installed_drive: str
    booted_from_ssd: bool
    restored_file_opened: bool

    def checks(self) -> dict[str, bool]:
        return {
            "drive": self.installed_drive == "Replacement SSD",
            "boot": self.booted_from_ssd,
            "data": self.restored_file_opened,
        }

    def status(self) -> str:
        return "verified" if all(self.checks().values()) else "investigate"


def build_report(verification: MigrationVerification) -> dict[str, object]:
    checks = verification.checks()
    return {
        "checks": checks,
        "status": verification.status(),
        "next_action": (
            "handoff"
            if verification.status() == "verified"
            else "investigate the failed check"
        ),
    }


if __name__ == "__main__":
    verification = MigrationVerification(
        installed_drive="Replacement SSD",
        booted_from_ssd=True,
        restored_file_opened=True,
    )
    print(build_report(verification))
