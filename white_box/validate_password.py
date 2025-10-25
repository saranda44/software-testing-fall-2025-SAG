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


def validate_password(password):
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


def validate_password_v(password):
    """version dummy"""
    print(password)
    return {"is_valid": False, "errors": []}
