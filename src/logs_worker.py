import json


def read_logs(file_paths, filter_date=None):
    logs = []
    for file_path in file_paths:
        with open(file_path) as f:
            for line in f:
                try:
                    log = json.loads(line)
                    if filter_date and not _matches_date(log['@timestamp'], filter_date):
                        continue
                    logs.append(log)
                except json.JSONDecodeError:
                    continue
    return logs


def _matches_date(timestamp, filter_date):
    log_date = timestamp.split('T')[0]
    return log_date == filter_date