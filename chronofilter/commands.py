from datetime import datetime
from sys import stdout, stdin

import typer

app = typer.Typer()


@app.command()
def filter_input(number_of_records: int):
    stdout.write(f'Will filter for the next {number_of_records} records.\n')
    data = stdin.read()

    current_timestamp = datetime.now(
            ).strftime('%I:%M%p').lower()

    if current_timestamp.startswith('0'):
        current_timestamp = current_timestamp[1:]

    stdout.write('Filtering all records >= '
                 f'{current_timestamp}...\n')

    for line in data:
        stdout.write(line)
        # TODO: process the lines here


if __name__ == '__main__':
    app()
