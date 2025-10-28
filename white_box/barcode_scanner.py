# -*- coding: utf-8 -*-
"""function barcode_scanner"""


def barcode_scanner(barcode, command=None):
    """
    function barcode_scanner
    """
    total_print = ""
    if command is None and barcode == "12345":
        total_print = "$7.25"
    return total_print
