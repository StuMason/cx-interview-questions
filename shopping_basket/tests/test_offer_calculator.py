from unittest import TestCase
import json
import os

from offer_calculator import OfferCalculator


class TestOfferCalculator(TestCase):

    def test_offer_calc_return_value(self):
        calc = OfferCalculator()
        results = calc.handle({}, {})
        expected = {"discount": 0.00}
        self.assertEqual(expected, results)

        