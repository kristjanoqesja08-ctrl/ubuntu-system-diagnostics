import psutil


def get_memory_info():
    memory = psutil.virtual_memory()

    return {
        "total_gb": round(memory.total / (1024 ** 3), 2),
        "available_gb": round(memory.available / (1024 ** 3), 2),
        "used_percent": memory.percent
    }


if __name__ == "__main__":
    print(get_memory_info())
