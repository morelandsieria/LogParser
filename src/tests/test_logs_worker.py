import os
from src.logs_worker import read_logs


def get_test_file_path(filename):
    return os.path.join(os.path.dirname(__file__), 'test_data', filename)


def test_read_logs():
    log_file = get_test_file_path('example3.log')
    logs = read_logs([log_file])
    
    assert len(logs) == 5
    assert logs[0]['url'] == '/api/context/...'
    assert logs[0]['response_time'] == 0.01


def test_filter_by_date():
    log_file = get_test_file_path('example3.log')
    logs = read_logs([log_file], filter_date="2025-06-22")
    
    assert len(logs) == 2
    assert all('2025-06-22' in log['@timestamp'] for log in logs)


def test_multiple_files():
    file1 = get_test_file_path('example3.log')
    file2 = get_test_file_path('example1.log')
    logs = read_logs([file1, file2])
    
    assert len(logs) == 105