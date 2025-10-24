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

    if ",\n" in string_number or "\n," in string_number:
        raise ValueError("Separadores inválidos mezclados")

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

    if ",\n" in string_number or "\n," in string_number:
        raise ValueError("Separadores inválidos mezclados")

    if string_number.endswith(",") or string_number.endswith("\n"):
        raise ValueError("Separador al final no permitido")

    if delimiter != "\n":
        string_number = string_number.replace("\n", delimiter)

    tokens = string_number.split(delimiter)
    result = 0

    for token in tokens:
        if token == "":
            continue

        try:
            result += int(token)
        except ValueError as exc:
            raise ValueError(f"'{delimiter}' expected but '{token}' found.") from exc

    return result


def add_v6(string_number):
    """version 6"""

    if string_number == "":
        return 0

    delimiter = ","
    if string_number.startswith("//"):
        header, string_number = string_number.split("\n", 1)
        delimiter = header[2:]

    # Validación de mezcla de separadores
    if ",\n" in string_number or "\n," in string_number:
        raise ValueError("Separadores inválidos mezclados")

    # Validación de separador al final
    if string_number.endswith(delimiter) or string_number.endswith("\n"):
        raise ValueError("Separador al final no permitido")

    # Reemplazar saltos de línea por el delimitador si no es personalizado
    if delimiter != "\n":
        string_number = string_number.replace("\n", delimiter)

    tokens = string_number.split(delimiter)
    result = 0
    negatives = []

    for token in tokens:
        if token == "":
            continue
        if token.startswith("-"):
            negatives.append(token)
        else:
            try:
                result += int(token)
            except ValueError as exc:
                raise ValueError(
                    f"'{delimiter}' expected but '{token}' found."
                ) from exc

    if negatives:
        return f"Negative number(s) not allowed: {', '.join(negatives)}"

    return result


def add_v7(string_number):
    """version 7"""
    if string_number == "":
        return 0

    delimiter = ","
    errors = []
    negatives = []

    # Detectar delimitador personalizado
    if string_number.startswith("//"):
        header, string_number = string_number.split("\n", 1)
        delimiter = header[2:]

    # Validaciones iniciales
    if ",\n" in string_number or "\n," in string_number:
        raise ValueError("Separadores inválidos mezclados")

    if string_number.endswith(delimiter) or string_number.endswith("\n"):
        raise ValueError("Separador al final no permitido")

    # Reemplazar saltos de línea por el delimitador
    if delimiter != "\n":
        string_number = string_number.replace("\n", delimiter)

    tokens = string_number.split(delimiter)
    result = 0

    for token in tokens:
        if token == "":
            continue

        # Si hay delimitador mezclado incorrecto (como “|2,3”)
        if not token.replace("-", "").isdigit():
            pos = string_number.find(",")
            errors.append(f"'{delimiter}' expected but ',' found at position {pos}.")
            continue

        num = int(token)

        # Negativos
        if num < 0:
            negatives.append(str(num))
            continue

        result += num

    # Si hay negativos y errores combinados
    if negatives and errors:
        return f"Negative number(s) not allowed: {', '.join(negatives)}\n" + "\n".join(
            errors
        )

    # Solo negativos
    if negatives:
        return f"Negative number(s) not allowed: {', '.join(negatives)}"

    # lanzar ValueError
    if errors:
        raise ValueError("\n".join(errors))

    return result


def add(string_number):
    """version 8"""
    if string_number == "":
        return 0

    delimiter = ","
    errors = []
    negatives = []

    # Detectar delimitador personalizado
    if string_number.startswith("//"):
        header, string_number = string_number.split("\n", 1)
        delimiter = header[2:]

    # Validaciones iniciales
    if ",\n" in string_number or "\n," in string_number:
        raise ValueError("Separadores inválidos mezclados")

    if string_number.endswith(delimiter) or string_number.endswith("\n"):
        raise ValueError("Separador al final no permitido")

    # Reemplazar saltos de línea por el delimitador
    if delimiter != "\n":
        string_number = string_number.replace("\n", delimiter)

    tokens = string_number.split(delimiter)
    result = 0

    for token in tokens:
        if token == "":
            continue

        # Si hay delimitador mezclado incorrecto (como “|2,3”)
        if not token.replace("-", "").isdigit():
            pos = string_number.find(",")
            errors.append(f"'{delimiter}' expected but ',' found at position {pos}.")
            continue

        num = int(token)

        # Negativos
        if num < 0:
            negatives.append(str(num))
            continue

        # Ignorar mayores a 1000
        if num <= 1000:
            result += num

    # Solo negativos
    if negatives:
        return f"Negative number(s) not allowed: {', '.join(negatives)}"

    # lanzar ValueError
    if errors:
        raise ValueError("\n".join(errors))

    return result
