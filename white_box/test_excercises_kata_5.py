# -*- coding: utf-8 -*-
"""Data-driven tests for barcode_scanner """
# pylint: disable=import-error
import pytest

from white_box.barcode_scanner import barcode_scanner


@pytest.mark.parametrize(
    "barcodes, expected",
    [("12345", "$7.25")],
)
def test_should_display_price_when_barcode_12345(barcodes, expected):
    """req 1: Barcode ‘12345’ should display price ‘$7.25’"""
    result = barcode_scanner(barcodes)
    assert result == expected


@pytest.mark.parametrize(
    "barcodes, expected",
    [("23456", "$12.50")],
)
def test_should_display_price_when_barcode_23456(barcodes, expected):
    """req 2:  Barcode ‘23456’ should display price ‘$12.50’"""
    result = barcode_scanner(barcodes)
    assert result == expected


@pytest.mark.parametrize(
    "barcodes, expected",
    [("99999", "Error: barcode not found")],
)
def test_should_display_error_when_barcode_not_found(barcodes, expected):
    """req 3: Barcode ‘99999’ should display ‘Error: barcode not found’"""
    result = barcode_scanner(barcodes)
    assert result == expected


@pytest.mark.parametrize(
    "barcodes, expected",
    [("", "Error: empty barcode")],
)
def test_should_display_error_when_barcode_empty(barcodes, expected):
    """req 4: Empty barcode should display ‘Error: empty barcode’"""
    result = barcode_scanner(barcodes)
    assert result == expected


@pytest.mark.parametrize(
    "barcodes, expected",
    [
        (["12345", "23456"], "$19.75"),
        (["12345"], "$7.25"),
        (["23456", "23456"], "$25.00"),
        (["99999", "12345"], "Error: barcode not found"),
        ([], "Error: empty list of barcodes"),
    ],
)
def test_should_display_total_when_command_is_total(barcodes, expected):
    """req 5: display the sum of the scanned product prices"""
    result = barcode_scanner(barcodes, command="total")
    assert result == expected
