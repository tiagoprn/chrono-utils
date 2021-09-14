from sys import stdout, stdin

import typer

app = typer.Typer()


@app.command()
def filter_input(number_of_records: int):
    stdout.write(f'Will filter for the next {number_of_records} records.\n')
    data = stdin.read()
    for line in data:
        stdout.write(line)


if __name__ == '__main__':
    app()
