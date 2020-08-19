from unittest import TestCase

from offer_calculator import OfferCalculator


class TestOfferCalculator(TestCase):
    def test_offer_calc_return_value(self):
        calc = OfferCalculator()
        basket_item = {
            "name": "Baked Beans",
            "quantity": 4,
            "price": 0.99,
            "total": 3.96,
        }

        offers = [
            {
                "name": "buy two get one free",
                "discount_type": "bogof",
                "details": {"buy": 2, "free": 1},
                "products": ["Baked Beans"],
            }
        ]

        results = calc.handle(offers, basket_item)
        expected = {"discount": 0.99}
        self.assertEqual(expected, results)

    def test_bogof_with_beans(self):
        calc = OfferCalculator()

        basket_item = {
            "name": "Baked Beans",
            "quantity": 6,
            "price": 0.99,
            "total": 3.96,
        }

        offer = {
            "name": "buy two get one free",
            "discount_type": "bogof",
            "details": {"buy": 2, "free": 1},
            "products": ["Baked Beans"],
        }

        results = calc.bogof(offer, basket_item)

        self.assertEqual(1.98, results)

    def test_bogof_perm_one(self):
        calc = OfferCalculator()
        basket_item = {"quantity": 4, "price": 0.99}
        offer = {"discount_type": "bogof", "details": {"buy": 2, "free": 1}}
        results = calc.bogof(offer, basket_item)

        self.assertEqual(0.99, results)

    def test_bogof_perm_two(self):
        calc = OfferCalculator()
        basket_item = {"quantity": 9, "price": 0.99}
        offer = {"discount_type": "bogof", "details": {"buy": 2, "free": 1}}
        results = calc.bogof(offer, basket_item)

        self.assertEqual(2.97, results)

    def test_bogof_perm_three(self):
        calc = OfferCalculator()
        basket_item = {"quantity": 10, "price": 0.99}
        offer = {"discount_type": "bogof", "details": {"buy": 2, "free": 1}}
        results = calc.bogof(offer, basket_item)

        self.assertEqual(2.97, results)

    def test_bogof_perm_four(self):
        calc = OfferCalculator()
        basket_item = {"quantity": 1, "price": 0.99}
        offer = {"discount_type": "bogof", "details": {"buy": 2, "free": 1}}
        results = calc.bogof(offer, basket_item)

        self.assertEqual(0.00, results)

    def test_percentage_with_sardines(self):
        calc = OfferCalculator()

        basket_item = {"name": "Sardines", "quantity": 2, "price": 1.89, "total": 3.78}

        offer = {
            "name": "25% off total",
            "discount_type": "percentage",
            "details": {"amount": 25},
            "products": ["Sardines"],
        }

        results = calc.percentage(offer, basket_item)

        self.assertEqual(0.95, results)
