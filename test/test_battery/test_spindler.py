import unittest
from datetime import date

from battery.spindler_battery import SpindlerBattery


class TestSpindlerBattery(unittest.TestCase):
    def test_battery_needs_service_true(self):
        current_date = date.fromisoformat("2022-04-30")
        last_service_date = date.fromisoformat("2019-01-25")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_needs_service_false(self):
        current_date = date.fromisoformat("2022-02-01")
        last_service_date = date.fromisoformat("2021-12-10")
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
