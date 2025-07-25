import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.arg_parser import Parser
from src.logs_worker import read_logs
from src.average_report import AverageReport
from src.print_table import show_table


def main():
    args_parser = Parser()
    args = args_parser.parse_args()

    logs = read_logs(args.file, args.date)

    if args.report == 'average':
        report = AverageReport()
        result = report.generate(logs)
        show_table(
            [(r['endpoint'], r['count'], r['avg_time']) for r in result],
            headers=['Endpoint', 'Requests', 'Avg Time']
        )
    else:
        raise ValueError(f"Неизвестный тип отчета:")

if __name__ == "__main__":
    main()