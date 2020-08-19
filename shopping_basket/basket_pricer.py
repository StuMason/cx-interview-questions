import argparse
import json
import traceback
import copy

from offer_calculator import OfferCalculator
from helpers import Helpers


class BasketPricer:
    def __init__(self, basket, catalogue, offers):
        self.basket = basket
        self.basket_catalogue = copy.copy(self.basket)
        self.catalogue = catalogue
        self.offers = offers
        self.pricer = {"sub-total": 0.00, "discount": 0.00, "total": 0.00}
        self.offer_calc = OfferCalculator()

    def handle(self):
        self.basket_catalogue_calc()
        self.basket_offers_calc()
        self.calculate_totals()
        return self.pricer

    def basket_catalogue_calc(self):
        for item in self.basket_catalogue:
            catalogue_listing = list(
                filter(lambda x: x["name"] == item["name"], self.catalogue)
            )
            if catalogue_listing:
                item["price"] = catalogue_listing[0]["price"]
                item["total"] = item["price"] * item["quantity"]

    def basket_offers_calc(self):
        for item in self.basket_catalogue:
            on_offer = list(
                filter(lambda x: item["name"] in x["products"], self.offers)
            )
            if on_offer:
                item.update(self.offer_calc.handle(on_offer, item))

    def calculate_totals(self):
        for item in self.basket_catalogue:
            self.pricer["sub-total"] = Helpers.formatted(
                self.pricer["sub-total"] + item["total"]
            )
            if "discount" in item:
                self.pricer["discount"] += item["discount"]
                if item['discount'] > item['total']:
                    item['discount'] = item['total']
                self.pricer["total"] += item["total"] - item["discount"]
            else:
                self.pricer["total"] += item["total"]


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Get data for basket pricer")

        parser.add_argument(
            "basket", help="JSON file location for basket of goods for customer"
        )
        parser.add_argument("catalogue", help="supermarkets catalogue of products")
        parser.add_argument("offers", help="offers currently available")

        args = parser.parse_args()

        basket = json.load(open(args.basket))
        catalogue = json.load(open(args.catalogue))
        offers = json.load(open(args.offers))

        pricer = BasketPricer(basket, catalogue, offers)
        print(json.dumps(pricer.handle()))

    except Exception:
        traceback.print_exc()
