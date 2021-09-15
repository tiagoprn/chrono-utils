from datetime import datetime

import pytest
import time_machine

from chronofilter.commands import (
    _get_datetime_instance_from_12_hours_format,
    _filter_records
)


@pytest.mark.parametrize(
        'fake_current_datetime,hour,expected_datetime',
        [
            ['2021-01-01T08:00', '9:00am', '2021-01-01T09:00'],
            ['2021-01-01T08:00', '1:00pm', '2021-01-01T13:00'],
            ['2021-01-01T08:00', '12:00am', '2021-01-01T00:00'],
            ['2021-01-01T08:00', '12:00pm', '2021-01-01T12:00']
        ]
)
def test_get_datetime_instance_from_12_hours_format(
        fake_current_datetime, hour, expected_datetime):
    with time_machine.travel(fake_current_datetime, tick=False):
        datetime_instance = _get_datetime_instance_from_12_hours_format(hour)
        expected_datetime_instance = datetime.fromisoformat(expected_datetime)
        assert datetime_instance == expected_datetime_instance


@time_machine.travel('2021-01-01T08:00', tick=False)
def test_filter_records():
    records = [
        '5:00am Do 01',
        '7:59am Do 02',
        '8:00am Do 03',
        '8:01am Do 04',
        '1:00pm Do 05',
        '2:00pm Do 06'
    ]
    filtered_records = _filter_records(records, 3)
    expected_filtered_records = [
        '8:00am Do 03',
        '8:01am Do 04',
        '1:00pm Do 05'
    ]
    assert filtered_records == expected_filtered_records
