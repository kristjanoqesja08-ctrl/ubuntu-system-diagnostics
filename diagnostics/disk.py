import psutil


def get_disk_info():
    disk = psutil.disk_usage("/")

    return {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "used_gb": round(disk.used / (1024 ** 3), 2),
        "free_gb": round(disk.free / (1024 ** 3), 2),
        "used_percent": disk.percent
    }


if __name__ == "__main__":
    print(get_disk_info())
