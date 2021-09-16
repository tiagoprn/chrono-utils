import logging
import os
from datetime import datetime
from sys import stdin, stdout
from typing import List

import typer

CURRENT_SCRIPT_NAME = os.path.splitext(os.path.basename(__file__))[0]
LOG_FORMAT = (
    '[%(asctime)s PID %(process)s '
    '%(filename)s:%(lineno)s - %(funcName)s()] '
    '%(levelname)s -> \n'
    '%(message)s\n'
)
logging.basicConfig(
    format=LOG_FORMAT,
    level=logging.INFO,
    handlers=[
        logging.FileHandler(f'{CURRENT_SCRIPT_NAME}.log'),
        # logging.StreamHandler(stdout)
    ],
)


app = typer.Typer()


def _get_current_timestamp_in_12_hours_format() -> str:
    current_timestamp = datetime.now().strftime('%I:%M%p').lower()

    return (
        current_timestamp[1:]
        if current_timestamp.startswith('0')
        else current_timestamp
    )


def _get_datetime_instance_from_12_hours_format(
    timestamp_in_12_hours_format: str,
) -> datetime:
    day_str = datetime.now().strftime('%Y-%m-%d')
    full_datetime = f'{day_str} {timestamp_in_12_hours_format.upper()}'
    return datetime.strptime(full_datetime, '%Y-%m-%d %I:%M%p')


def _filter_records(data: List[str], number_of_records: int) -> List[str]:
    filtered_records = []

    current_timestamp = _get_current_timestamp_in_12_hours_format()

    logging.info('Filtering all records >= ' f'{current_timestamp}...\n')

    for line in data:
        if not line.strip():
            continue

        timestamp_string = line.split()[0]
        timestamp_as_datetime = _get_datetime_instance_from_12_hours_format(
            timestamp_string
        )

        if timestamp_as_datetime >= datetime.now():
            filtered_records.append(line)
        else:
            continue

        if len(filtered_records) == number_of_records:
            return filtered_records

    return filtered_records


@app.command()
def filter_input(number_of_records: int):
    logging.info(f'Will filter for the next {number_of_records} records.\n')
    data = stdin.readlines()

    filtered_records = _filter_records(data, number_of_records)
    for record in filtered_records:
        stdout.write(record)


if __name__ == '__main__':
    app()
