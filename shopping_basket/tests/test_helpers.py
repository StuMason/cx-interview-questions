from unittest import TestCase

from helpers import Helpers


class TestHelpers(TestCase):
    def test_formatted_statis_method(self):
        result = Helpers.formatted(2.33433553)
        self.assertEqual(2.33, result)

        result = Helpers.formatted(0.9566666)
        self.assertEqual(0.96, result)

        result = Helpers.formatted(0.945)
        self.assertEqual(0.95, result)
