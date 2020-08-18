import argparse
import json
import traceback

class BasketPricer:
    def __init__(self, basket, catalogue, offers):
        self.basket = basket
        self.catalogue = catalogue
        self.offers = offers

    def handle(self):
        return {"sub-total": 0.00, "discount": 0.00, "total": 0.00}


if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser(description="Get data for basket pricer")

        parser.add_argument("basket", help="JSON file location for basket of goods for customer")
        parser.add_argument("catalogue", help="supermarkets catalogue of products")
        parser.add_argument("offers", help="offers currently available")

        args = parser.parse_args()

        basket = json.load(open(args.basket))
        catalogue = json.load(open(args.catalogue))
        offers = json.load(open(args.offers))

        pricer = BasketPricer(basket, catalogue, offers)
        print(pricer.handle())

    except Exception as e:
        traceback.print_exc()