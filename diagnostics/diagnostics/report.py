import json
from pathlib import Path
from datetime import datetime, timezone


def save_report(data):
    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    timestamp = datetime.now(timezone.utc).strftime(
        "%Y%m%d_%H%M%S"
    )

    report_file = reports_dir / f"diagnostic_{timestamp}.json"

    with report_file.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return str(report_file)


if __name__ == "__main__":
    sample_report = {
        "status": "test",
        "message": "Diagnostic report generated successfully"
    }

    print(save_report(sample_report))
