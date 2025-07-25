from tabulate import tabulate


def show_table(data, headers):
    print(tabulate(data, headers=headers, tablefmt="grid"))