# -*- coding: utf-8 -*-
"""Versiones de la funcion validate_password"""


def validate_password_v1(password):
    """version dummy"""
    print(password)
    return {"is_valid": False, "errors": []}


def validate_password_v2(password):
    """version 2: 8 caracteracteres de longitud"""
    valid = False
    errors = []

    if len(password) < 8:
        valid = False
        errors.append("Password must be at least 8 characters")
    else:
        valid = True

    return {"is_valid": valid, "errors": errors}


def validate_password_v3(password):
    """version 3: longitud y minimo 2 numeros"""
    errors = []
    valid = True

    if len(password) < 8:
        valid = False
        errors.append("Password must be at least 8 characters")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        valid = False
        errors.append("The password must contain at least 2 numbers")

    return {"is_valid": valid, "errors": errors}


def validate_password_v4(password):
    """version 4: multiples errores"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        errors.append("The password must contain at least 2 numbers")

    # No cambiamos la estructura, ya admite múltiples errores
    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_password(password):
    """version 5: al menos una letra mayuscula"""
    errors = []

    if len(password) < 8:
        errors.append("Password must be at least 8 characters")

    digits = sum(ch.isdigit() for ch in password)
    if digits < 2:
        errors.append("The password must contain at least 2 numbers")

    if not any(ch.isupper() for ch in password):
        errors.append("password must contain at least one capital letter")

    return {"is_valid": len(errors) == 0, "errors": errors}


def validate_password_v(password):
    """version dummy"""
    print(password)
    return {"is_valid": False, "errors": []}
