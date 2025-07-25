from argparse import ArgumentParser

class Parser:
    def __init__(self):
        self.parser = ArgumentParser()
        self._setup_arguments()

    def _setup_arguments(self):
        self.parser.add_argument('--file', nargs='+', required=True)
        self.parser.add_argument('--report', required=True)
        self.parser.add_argument('--date')

    def parse_args(self):
        return self.parser.parse_args()
