from pathlib import Path


def analyze_logs(log_file="/var/log/syslog"):
    path = Path(log_file)

    if not path.exists():
        return {
            "error": f"Log file not found: {log_file}"
        }

    errors = []
    warnings = []

    try:
        with path.open("r", encoding="utf-8", errors="replace") as file:
            for line in file:
                lower_line = line.lower()

                if "error" in lower_line or "failed" in lower_line:
                    errors.append(line.strip())

                elif "warning" in lower_line:
                    warnings.append(line.strip())

        return {
            "errors_count": len(errors),
            "warnings_count": len(warnings),
            "errors": errors[:20],
            "warnings": warnings[:20]
        }

    except PermissionError:
        return {"error": "Permission denied while reading logs"}


if __name__ == "__main__":
    print(analyze_logs())
