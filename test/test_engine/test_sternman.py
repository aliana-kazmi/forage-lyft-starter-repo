import unittest
from engine.sternman_engine import SternmanEngine

class TestSternman(unittest.TestCase):
    def test_engine_needs_service(self):
        warning_indicator = True
        engine = SternmanEngine(warning_light_is_on=warning_indicator)
        self.assertTrue(engine.needs_service())

    def test_engine_does_not_need_service(self):
        warning_indicator = False
        engine = SternmanEngine(warning_light_is_on=warning_indicator)
        self.assertFalse(engine.needs_service())
