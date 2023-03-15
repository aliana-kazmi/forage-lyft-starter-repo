import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_battery_needs_service_true(self):
        current_date = date.fromisoformat("2022-04-30")
        last_service_date = date.fromisoformat("2017-01-25")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_battery_needs_service_false(self):
        current_date = date.fromisoformat("2022-02-01")
        last_service_date = date.fromisoformat("2021-12-10")
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())
