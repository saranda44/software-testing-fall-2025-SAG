# -*- coding: utf-8 -*-
"""Funcion fizzbuzz"""


def fizzbuzz(number):
    """funcion fizzbuzz iteracion 3: return "Fizz" cuando el numero es multiplo de 3"""
    result = ""
    if number % 3 == 0:
        result = "Fizz"

    if number % 5 == 0:
        result = "Buzz"

    if number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"

    return result or str(number)
