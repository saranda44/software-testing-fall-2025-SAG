# -*- coding: utf-8 -*-
"""Funcion fizzbuzz"""


def fizzbuzz_v1(number):
    """funcion fizzbuzz iteracion 1"""
    return number


def fizzbuzz_v2(number):
    """funcion fizzbuzz iteracion 2: return string number"""
    result = ""
    if number % 3 != 0 and number % 5 != 0:
        result = str(number)
    return result


def fizzbuzz_v3(number):
    """funcion fizzbuzz iteracion 3: return "Fizz" cuando el numero es multiplo de 3"""
    result = ""
    if number % 3 != 0 and number % 5 != 0:
        result = str(number)

    if number % 3 == 0:
        result = "Fizz"
    return result


def fizzbuzz_v4(number):
    """funcion fizzbuzz iteracion 4: return "Buzz" cuando el numero es multiplo de 5"""
    result = ""
    if number % 3 != 0 and number % 5 != 0:
        result = str(number)

    if number % 3 == 0:
        result = "Fizz"

    if number % 5 == 0:
        result = "Buzz"

    return result


def fizzbuzz_v5(number):
    """funcion fizzbuzz iteracion 5: return "FizzBuzz" cuando el numero es multiplo de 3 y 5"""
    result = ""
    if number % 3 != 0 and number % 5 != 0:
        result = str(number)

    if number % 3 == 0:
        result = "Fizz"

    if number % 5 == 0:
        result = "Buzz"

    if number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"

    return result


def fizzbuzz(number):
    """funcion fizzbuzz iteracion 6"""
    result = ""
    if number % 3 == 0:
        result = "Fizz"

    if number % 5 == 0:
        result = "Buzz"

    if number % 3 == 0 and number % 5 == 0:
        result = "FizzBuzz"

    return result or str(number)
