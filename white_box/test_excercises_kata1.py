# -*- coding: utf-8 -*-
"""Module test function fizzbuzz"""
import unittest

from white_box.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """Class for testing function fizzbuzz"""

    def test_fizzbuzz_no_multiple_of_three_or_five(self):
        """If the number in not multiple of three or five, return the number as a string"""
        self.assertEqual(fizzbuzz(4), "4")

    def test_fizzbuzz_multiples_of_three(self):
        """If the number multiple of three, return Fizz"""
        self.assertEqual(fizzbuzz(3), "Fizz")

    def test_fizzbuzz_multiples_of_five(self):
        """If the number multiple of five, return Buzz"""
        self.assertEqual(fizzbuzz(5), "Buzz")

    def test_fizzbuzz_multiples_of_both(self):
        """If the number multiple of three, return Fizz"""
        self.assertEqual(fizzbuzz(15), "FizzBuzz")
