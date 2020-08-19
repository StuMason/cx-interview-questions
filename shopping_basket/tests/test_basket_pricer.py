from unittest import TestCase
import json
import os

from basket_pricer import BasketPricer


class TestBasketPricer(TestCase):
    def setUp(self):
        cwd = os.getcwd()
        with open(cwd + '/shopping_basket_tests/fixtures/test_basket_one.json') as f:
            self.basket_one = json.load(f)
        with open(cwd + '/shopping_basket_tests/fixtures/test_catalogue.json') as f:
            self.catalogue = json.load(f)
        with open(cwd + '/shopping_basket_tests/fixtures/test_offers.json') as f:
            self.offers = json.load(f)

    def test_return_value(self):
        pricer = BasketPricer([], [], {})
        results = pricer.handle()

        expected = {
            "sub-total": 0.00,
            "discount": 0.00,
            "total": 0.00
        }

        self.assertEqual(expected, results)
        self.assertEqual([], pricer.basket_catalogue)

    def test_combines_default_basket_with_catalogue_prices(self):
        pricer = BasketPricer(self.basket_one, self.catalogue, {})
        pricer.basket_catalogue_calc()
        expected = [
            {
                "name": "Baked Beans", 
                "quantity": 4,
                "price": 0.99,
                "total": 3.96
            },
            {
                "name": "Biscuits", 
                "quantity": 1,
                "price": 1.20,
                "total": 1.20
            },
        ]
        self.assertEqual(expected, pricer.basket_catalogue)

    def test_combines_basket_with_single_catalogue_prices(self):
        pricer = BasketPricer([{"name": "Sardines", "quantity": 10}], self.catalogue, {})
        pricer.basket_catalogue_calc()
        expected = [
            {
                "name": "Sardines", 
                "quantity": 10,
                "price": 1.89,
                "total": 18.90
            }
        ]
        self.assertEqual(expected, pricer.basket_catalogue)

    def test_combines_basket_with_non_existant_catalogue_prices(self):
        pricer = BasketPricer([{"name": "Foo", "quantity": 10}], self.catalogue, {})
        pricer.basket_catalogue_calc()
        expected = [{"name": "Foo", "quantity": 10}]
        self.assertEqual(expected, pricer.basket_catalogue)

    def test_basket_offers_calculator(self):
        pricer = BasketPricer(self.basket_one, self.catalogue, self.offers)
        pricer.basket_offers_calc()


