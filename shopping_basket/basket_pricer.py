import argparse
import json
import traceback
import copy


class BasketPricer:
    def __init__(self, basket, catalogue, offers):
        self.basket = basket
        self.basket_catalogue = copy.copy(self.basket)
        self.catalogue = catalogue
        self.offers = offers
        self.pricer = {
            "sub-total": 0.00,
            "discount": 0.00,
            "total": 0.00
        }

    def handle(self):
        self.basket_catalogue_calc()
        return self.pricer

    def basket_catalogue_calc(self):
        for item in self.basket_catalogue:
            catalogue_listing = list(
                filter(lambda x: x["name"] == item['name'], self.catalogue))
            if catalogue_listing:
                item['price'] = catalogue_listing[0]['price']
                item['total'] = item['price'] * item['quantity']
    
    def basket_offers_calc(self):
        for item in self.basket_catalogue:
            on_offer = list(
                filter(lambda x: item['name'] in x["products"], self.offers))
            if on_offer:
                item['discount'] = on_offer[0]['name']

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(
            description="Get data for basket pricer")

        parser.add_argument(
            "basket", help="JSON file location for basket of goods for customer")
        parser.add_argument(
            "catalogue", help="supermarkets catalogue of products")
        parser.add_argument("offers", help="offers currently available")

        args = parser.parse_args()

        basket = json.load(open(args.basket))
        catalogue = json.load(open(args.catalogue))
        offers = json.load(open(args.offers))

        pricer = BasketPricer(basket, catalogue, offers)
        print(json.dumps(pricer.handle()))

    except Exception as e:
        traceback.print_exc()
