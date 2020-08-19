import math


class Helpers:
    @staticmethod
    def formatted(discount):
        multiplier = 10 ** 2
        return math.floor(discount * multiplier + 0.5) / multiplier
