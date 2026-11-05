import json
from datetime import datetime, timezone

from diagnostics.cpu import get_cpu_info
from diagnostics.memory import get_memory_info
from diagnostics.disk import get_disk_info
from diagnostics.logs import analyze_logs
from diagnostics.services import get_services


def run_diagnostics():
    print("\n=== UBUNTU SYSTEM DIAGNOSTICS ===\n")

    report = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "logs": analyze_logs(),
        "services": get_services()
    }

    print(json.dumps(report, indent=4))

    return report


if __name__ == "__main__":
    run_diagnostics()
