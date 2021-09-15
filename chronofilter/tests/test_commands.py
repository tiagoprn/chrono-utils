from datetime import datetime

import pytest
import time_machine

from chronofilter.commands import _get_datetime_instance_from_12_hours_format


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
    with time_machine.travel(fake_current_datetime):
        datetime_instance = _get_datetime_instance_from_12_hours_format(hour)
        expected_datetime_instance = datetime.fromisoformat(expected_datetime)
        assert datetime_instance == expected_datetime_instance
