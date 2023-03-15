import unittest
from engine.capulet_engine import CapuletEngine

class TestCapulet(unittest.TestCase):
    def test_engine_needs_service(self):
        current_mileage = 15000
        last_service_mileage = 11000
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        current_mileage = 15000
        last_service_mileage = 14000
        engine = CapuletEngine(current_mileage=current_mileage,last_service_mileage=last_service_mileage)
        self.assertFalse(engine.needs_service())

