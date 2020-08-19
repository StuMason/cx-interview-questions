import math


class Helpers:
    @staticmethod
    def formatted(discount: float) -> float:
        multiplier = 10 ** 2
        return math.floor(discount * multiplier + 0.5) / multiplier
