import unittest
from engine.willoughby_engine import WilloughbyEngine


class TestWilloughby(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 13000
        last_service_mileage = 6000
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        current_mileage = 15000
        last_service_mileage = 14000
        engine = WilloughbyEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())
