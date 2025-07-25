from argparse import ArgumentParser

class Parser:
    def __init__(self):
        self.parser = ArgumentParser()
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument('--file', nargs='+', required=True, help='Один или несколько лог-файлов')
        self.parser.add_argument('--report', required=True, help='Тип отчёта average')
        self.parser.add_argument('--date', help='Фильтрация по дате в формате YYYY-MM-DD')

    def parse_args(self):
        return self.parser.parse_args()
