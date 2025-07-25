from collections import defaultdict
from .base_report import BaseReport

class AverageReport(BaseReport):
    def generate(self, logs):
        endpoint_stats = defaultdict(lambda: {'count': 0, 'total_time': 0})
        
        for log in logs:
            url = log['url']
            endpoint_stats[url]['count'] += 1
            endpoint_stats[url]['total_time'] += log['response_time']
        
        result = []
        for url, stats in endpoint_stats.items():
            avg_time = stats['total_time'] / stats['count']
            result.append({
                'endpoint': url,
                'count': stats['count'],
                'avg_time': round(avg_time, 3)
            })
        
        return result