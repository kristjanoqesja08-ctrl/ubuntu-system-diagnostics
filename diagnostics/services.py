import subprocess


def get_services():
    try:
        result = subprocess.run(
            ["systemctl", "list-units", "--type=service",
             "--no-pager", "--no-legend"],
            capture_output=True,
            text=True,
            check=True,
            timeout=15
        )

        services = []

        for line in result.stdout.splitlines():
            parts = line.split(None, 4)

            if len(parts) >= 4:
                services.append({
                    "name": parts[0],
                    "load": parts[1],
                    "active": parts[2],
                    "sub": parts[3]
                })

        return {
            "total_services": len(services),
            "services": services
        }

    except FileNotFoundError:
        return {"error": "systemctl is not available"}

    except subprocess.CalledProcessError as error:
        return {"error": error.stderr.strip()}

    except subprocess.TimeoutExpired:
        return {"error": "Service check timed out"}


if __name__ == "__main__":
    print(get_services())
