from unittest import TestCase
import json

from basket_pricer import BasketPricer


class TestBasketPricer(TestCase):
    def init(self):
        self.basket_one = json.load(open('./fixtures/test_basket_one.json'))
        self.catalogue = json.load(open('./fixtures/test_catalogue.json'))
        self.offers = json.load(open('./fixtures/test_offers.json'))

    def test_return_value(self):
        pricer = BasketPricer({}, {}, {})
        results = pricer.handle()

        expected = {"sub-total": 0.00, "discount": 0.00, "total": 0.00}

        self.assertEqual(expected, results)
