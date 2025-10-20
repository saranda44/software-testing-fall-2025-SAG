# -*- coding: utf-8 -*-
"""Funcion fizzbuzz"""


def fizzbuzz(number):
    """funcion fizzbuzz iteracion 2: return string number"""
    result = ""
    if number % 3 != 0 and number % 5 != 0:
        result = str(number)
    return result
