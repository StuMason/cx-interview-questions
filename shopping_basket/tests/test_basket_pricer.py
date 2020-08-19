from unittest import TestCase
import json
import os

from basket_pricer import BasketPricer


class TestBasketPricer(TestCase):
    def setUp(self):
        cwd = os.getcwd()
        with open(cwd + "/tests/fixtures/test_basket_one.json") as f:
            self.basket_one = json.load(f)
        with open(cwd + "/tests/fixtures/test_catalogue.json") as f:
            self.catalogue = json.load(f)
        with open(cwd + "/tests/fixtures/test_offers.json") as f:
            self.offers = json.load(f)

    def test_return_value(self):
        pricer = BasketPricer([], [], {})
        results = pricer.handle()

        expected = {"sub-total": 0.00, "discount": 0.00, "total": 0.00}

        self.assertEqual(expected, results)
        self.assertEqual([], pricer.basket_catalogue)

    def test_combines_default_basket_with_catalogue_prices(self):
        pricer = BasketPricer(self.basket_one, self.catalogue, {})
        pricer.basket_catalogue_calc()
        expected = [
            {"name": "Baked Beans", "quantity": 4, "price": 0.99, "total": 3.96},
            {"name": "Biscuits", "quantity": 1, "price": 1.20, "total": 1.20},
        ]
        self.assertEqual(expected, pricer.basket_catalogue)

    def test_combines_basket_with_single_catalogue_prices(self):
        pricer = BasketPricer(
            [{"name": "Sardines", "quantity": 10}], self.catalogue, {}
        )
        pricer.basket_catalogue_calc()
        expected = [{"name": "Sardines", "quantity": 10, "price": 1.89, "total": 18.90}]
        self.assertEqual(expected, pricer.basket_catalogue)

    def test_combines_basket_with_non_existant_catalogue_prices(self):
        pricer = BasketPricer([{"name": "Foo", "quantity": 10}], self.catalogue, {})
        pricer.basket_catalogue_calc()
        expected = [{"name": "Foo", "quantity": 10}]
        self.assertEqual(expected, pricer.basket_catalogue)

    def test_basket_offers_calculator(self):
        basket = [{"name": "Sardines", "quantity": 10, "price": 1.89, "total": 18.90}]
        pricer = BasketPricer(basket, self.catalogue, self.offers)
        pricer.basket_offers_calc()
        self.assertEqual(4.72, pricer.basket_catalogue[0]["discount"])

    def test_calculate_total_one(self):
        pricer = BasketPricer([], [], [])
        pricer.basket_catalogue = [
            {
                "name": "Baked Beans",
                "quantity": 4,
                "price": 0.99,
                "total": 3.96,
                "discount": 0.99,
            },
            {
                "name": "Biscuits",
                "quantity": 1,
                "price": 1.20,
                "total": 1.20,
                "discount": 0.00,
            },
        ]
        pricer.calculate_totals()
        expected = {"sub-total": 5.16, "discount": 0.99, "total": 4.17}
        self.assertEqual(expected, pricer.pricer)

    def test_calculate_total_two(self):
        pricer = BasketPricer([], [], [])
        pricer.basket_catalogue = [
            {
                "name": "Baked Beans",
                "quantity": 2,
                "price": 0.99,
                "total": 1.98,
                "discount": 0.00,
            },
            {
                "name": "Biscuits",
                "quantity": 1,
                "price": 1.20,
                "total": 1.20,
                "discount": 0.00,
            },
            {
                "name": "Sardines",
                "quantity": 2,
                "price": 1.89,
                "total": 3.78,
                "discount": 0.95,
            },
        ]
        pricer.calculate_totals()
        expected = {"sub-total": 6.96, "discount": 0.95, "total": 6.01}
        self.assertEqual(expected, pricer.pricer)
