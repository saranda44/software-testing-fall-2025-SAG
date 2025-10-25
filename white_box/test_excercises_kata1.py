# -*- coding: utf-8 -*-
"""Module test function fizzbuzz"""
import unittest

from white_box.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Class for testing function fizzbuzz"""

    def test_should_return_number_as_string_when_not_multiple_of_three_or_five(self):
        """Should return the number as a string when it is not a multiple of three or five."""
        self.assertEqual(fizzbuzz(4), "4")

    def test_should_return_fizz_when_number_is_multiple_of_three(self):
        """Should return 'Fizz' when the number is a multiple of three."""
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_should_return_buzz_when_number_is_multiple_of_five(self):
        """Should return 'Buzz' when the number is a multiple of five."""
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_should_return_fizzbuzz_when_number_is_multiple_of_three_and_five(self):
        """Should return 'FizzBuzz' when the number is a multiple of both three and five."""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
