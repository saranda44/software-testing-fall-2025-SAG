# -*- coding: utf-8 -*-
"""function barcode_scanner"""

PRICES = {
    "12345": 7.25,
    "23456": 12.50,
}


def barcode_scanner(barcode, command=None):
    """
    function barcode_sacanner
    """
    total_print = ""
    if command == "total":
        if not barcode:
            return "Error: empty list of barcodes"

        total = 0
        for code in barcode:
            if code not in PRICES:
                return "Error: barcode not found"
            total += PRICES[code]
            total_print = f"${total:.2f}"
    else:
        if barcode == "":
            return "Error: empty barcode"
        if barcode not in PRICES:
            return "Error: barcode not found"
        total_print = f"${PRICES[barcode]:.2f}"

    return total_print
