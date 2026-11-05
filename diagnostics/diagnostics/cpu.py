import psutil


def get_cpu_info():
    cpu_usage = psutil.cpu_percent(interval=1)
    cpu_count = psutil.cpu_count(logical=True)

    return {
        "cpu_usage_percent": cpu_usage,
        "logical_cores": cpu_count
    }


if __name__ == "__main__":
    print(get_cpu_info())
