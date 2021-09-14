from datetime import datetime
from sys import stdout, stdin
from typing import List

import typer

app = typer.Typer()


def _get_current_timestamp_in_12_hours_format() -> str:
    current_timestamp = datetime.now(
            ).strftime('%I:%M%p').lower()

    return current_timestamp[1:] if current_timestamp.startswith(
            '0') else current_timestamp


def _filter_records(data: List[str], number_of_records: int) -> List[str]:
    filtered_records = []

    current_timestamp = _get_current_timestamp_in_12_hours_format()

    stdout.write('Filtering all records >= '
                 f'{current_timestamp}...\n')

    for line in data:
        # TODO: process the lines here
        filtered_records.append(line)
        if len(filtered_records) == number_of_records:
            return filtered_records


@app.command()
def filter_input(number_of_records: int):
    stdout.write(f'Will filter for the next {number_of_records} records.\n')
    data = stdin.readlines()

    # __import__('pudb').set_trace()
    filtered_records = _filter_records(data, number_of_records)
    for record in filtered_records:
        stdout.write(record)


if __name__ == '__main__':
    app()
