import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.average_report import AverageReport
from src.logs_worker import read_logs


def get_test_file_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def test_average_report():
    log_file = get_test_file_path('example3.log')
    logs = read_logs([log_file])
    
    report = AverageReport()
    result = report.generate(logs)
    
    assert len(result) == 2
    assert result[0]['count'] == 4
    assert result[0]['avg_time'] == 0.152