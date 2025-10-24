# -*- coding: utf-8 -*-
"""Versiones de la funcion validate_password"""


def validate_password_v1(password):
    """version dummy"""
    print(password)
    return {"is_valid": False, "errors": []}


def validate_password(password):
    """version 2: 8 caracteracteres de longitud"""
    valid = False
    errors = []

    if len(password) < 8:
        valid = False
        errors.append("Password must be at least 8 characters")
    else:
        valid = True

    return {"is_valid": valid, "errors": errors}


def validate_password_v2(password):
    """version dummy"""
    print(password)
    return {"is_valid": False, "errors": []}
