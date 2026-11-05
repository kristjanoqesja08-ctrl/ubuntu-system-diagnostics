import json

from diagnostics.cpu import get_cpu_info
from diagnostics.memory import get_memory_info
from diagnostics.disk import get_disk_info
from diagnostics.report import save_report


def test_cpu_info():
    result = get_cpu_info()

    assert "cpu_usage_percent" in result
    assert "logical_cores" in result
    assert 0 <= result["cpu_usage_percent"] <= 100


def test_memory_info():
    result = get_memory_info()

    assert result["total_gb"] > 0
    assert result["available_gb"] >= 0
    assert 0 <= result["used_percent"] <= 100


def test_disk_info():
    result = get_disk_info()

    assert result["total_gb"] > 0
    assert result["free_gb"] >= 0
    assert 0 <= result["used_percent"] <= 100


def test_save_report(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    data = {"status": "success"}

    report_path = save_report(data)

    with open(report_path, encoding="utf-8") as file:
        saved_data = json.load(file)

    assert saved_data == data
