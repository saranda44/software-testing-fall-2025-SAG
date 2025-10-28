# -*- coding: utf-8 -*-
"""function barcode_scanner"""

PRICES = {
    "12345": 7.25,
    "23456": 12.50,
}


def barcode_scanner(barcode, command=None):
    """
    function barcode_scanner
    """
    total_print = ""
    if command is None:
        total_print = f"${PRICES[barcode]:.2f}"
    return total_print
