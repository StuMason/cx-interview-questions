import math


class OfferCalculator:

    def handle(self, offers, basket_item):
        discount = 0.00
        for offer in offers:
            if hasattr(self.__class__, offer['discount_type']) and callable(getattr(self.__class__, offer['discount_type'])):
                discount += getattr(self, offer['discount_type'])(offer, basket_item)
        return {"discount": discount}

    def formatted_discount(self, discount):
        multiplier = 10 ** 2
        return math.floor(discount*multiplier + 0.5) / multiplier

    def bogof(self, offer, basket_item):
        discount_total = offer['details']['buy'] + offer['details']['free']
        discount_required = basket_item['quantity'] // discount_total
        return self.formatted_discount(basket_item['price'] * discount_required)

    def percentage(self, offer, basket_item):
        return self.formatted_discount(basket_item['total'] * (offer['details']['amount']/100))

