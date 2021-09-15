from datetime import datetime

import time_machine

from chronofilter.commands import _get_datetime_instance_from_12_hours_format


def test_get_current_timestamp_in_12_hours_format():
    fake_current_datetime = datetime.fromisoformat('2021-01-01T08:00')
    with time_machine.travel(fake_current_datetime):
        hour = '9:00am'
        datetime_instance = _get_datetime_instance_from_12_hours_format(hour)
        assert datetime_instance == datetime.fromisoformat('2021-01-01T09:00')
