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
    if command is None and barcode in PRICES:
        total_print = f"${PRICES[barcode]:.2f}"
    elif barcode not in PRICES:
        total_print = "Error: barcode not found"

    return total_print
