Ubuntu System Diagnostics

A Python-based Linux system diagnostics tool designed to monitor system health, analyze system logs, check system services, detect potential errors, and generate automated diagnostic reports.

Features

* CPU Monitoring: Monitor processor usage and system performance.
* Memory Analysis: Display RAM usage and available memory.
* Disk Monitoring: Check disk space, storage usage, and available capacity.
* Log Analyzer: Analyze Linux system logs to identify errors and warnings.
* Service Checker: Inspect the status of running system services.
* Error Detection: Identify potential system issues.
* Diagnostic Reports: Generate structured reports in JSON format.

Technologies

* Python 3
* Linux / Ubuntu
* psutil
* pytest
* Git and GitHub
* Bash

Project Structure

ubuntu-system-diagnostics/
├── diagnostics/
├── tests/
├── reports/
├── main.py
├── requirements.txt
└── README.md

Installation

git clone YOUR_REPOSITORY_URL
cd ubuntu-system-diagnostics
pip install -r requirements.txt

Usage

python main.py

Testing

pytest

Project Status

Currently under development.

Author

Kristjano Qesja
