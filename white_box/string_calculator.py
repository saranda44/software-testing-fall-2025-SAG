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
    """version 3"""
    if string_number == "":
        return 0

    if ",\n" in string_number or "\n," in string_number:
        raise ValueError("Separadores inválidos mezclados")

    # Reemplazar saltos de línea por comas para unificar
    numbers = string_number.replace("\n", ",")
    parts = numbers.split(",")

    return sum(int(num) for num in parts if num)


def add_v4(string_number):
    """version 4"""
    if string_number == "":
        return 0

    if string_number.endswith(",") or string_number.endswith("\n"):
        raise ValueError("Separador al final no permitido")

    numbers = string_number.replace("\n", ",")
    parts = numbers.split(",")

    return sum(int(num) for num in parts if num)


def add_v5(string_number):
    """version 5"""
    if string_number == "":
        return 0

    delimiter = ","
    if string_number.startswith("//"):
        header, string_number = string_number.split("\n", 1)
        delimiter = header[2:]

    result = 0
    index = 0
    while index < len(string_number):
        if string_number[index].isdigit():
            num_str = ""
            while index < len(string_number) and string_number[index].isdigit():
                num_str += string_number[index]
                index += 1
            result += int(num_str)
        elif string_number.startswith(delimiter, index):
            index += len(delimiter)
        else:
            raise ValueError(
                f"'{delimiter}' expected but '{string_number[index]}' found at position {index}."
            )
    return result


def add_v6(string_number):
    """version dummy"""
    return string_number


def add_v7(string_number):
    """version dummy"""
    return string_number


def add_v8(string_number):
    """version dummy"""
    return string_number
