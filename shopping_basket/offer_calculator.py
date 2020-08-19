from helpers import Helpers


class OfferCalculator:
    def handle(self, offers: list, basket_item: dict) -> dict:
        discount = 0.00
        for offer in offers:
            if hasattr(self.__class__, offer["discount_type"]) and callable(
                getattr(self.__class__, offer["discount_type"])
            ):
                discount += getattr(self, offer["discount_type"])(offer, basket_item)
        return {"discount": discount}

    def bogof(self, offer: dict, basket_item: dict) -> float:
        discount_total = offer["details"]["buy"] + offer["details"]["free"]
        discount_required = basket_item["quantity"] // discount_total
        return Helpers.formatted(basket_item["price"] * discount_required)

    def percentage(self, offer: dict, basket_item: dict) -> float:
        return Helpers.formatted(
            basket_item["total"] * (offer["details"]["amount"] / 100)
        )
