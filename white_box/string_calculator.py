# -*- coding: utf-8 -*-
"""Versiones de la funcion add"""


def add_v1(string_number):
    """version 1"""
    result = 0

    if string_number != "":
        parts = string_number.split(",")

        if len(parts) == 1:
            result = int(parts[0])

        if len(parts) == 2:
            result = int(parts[0]) + int(parts[1])
    return result


def add_v2(string_number):
    """version 2"""
    if string_number == "":
        return 0

    parts = string_number.split(",")
    total = 0

    for num in parts:
        total += int(num)

    return total


def add_v3(string_number):
    """version dummy"""
    return string_number


def add_v4(string_number):
    """version dummy"""
    return string_number


def add_v5(string_number):
    """version dummy"""
    return string_number


def add_v6(string_number):
    """version dummy"""
    return string_number


def add_v7(string_number):
    """version dummy"""
    return string_number


def add_v8(string_number):
    """version dummy"""
    return string_number
