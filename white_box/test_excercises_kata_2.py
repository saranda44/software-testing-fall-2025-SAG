# -*- coding: utf-8 -*-
"""Module test function add"""
import unittest

from white_box.string_calculator import (
    add_v1,
    add_v2,
    add_v3,
    add_v4,
    add_v5,
    add_v6,
    add_v7,
    add_v8,
)


class TestStringCalculator(unittest.TestCase):
    """Pruebas de los requerimientos del String Calculator"""

    # Requerimiento 1
    def test_empty_string_returns_zero(self):
        """Cadena vacía: devuelve 0"""
        self.assertEqual(add_v1(""), 0)

    def test_single_number_returns_itself(self):
        """Un número: devuelve el mismo número"""
        self.assertEqual(add_v1("1"), 1)

    def test_two_numbers_comma_separated_returns_sum(self):
        """Dos números separados por coma: devuelve su suma"""
        self.assertEqual(add_v1("1,2"), 3)

    # Requerimiento 2
    def test_multiple_numbers_comma_separated_returns_sum(self):
        """Manejar varios números separados por coma: devuelve su suma"""
        self.assertEqual(add_v2("1,2,3,4,5"), 15)

    # Requerimiento 3
    def test_newline_as_separator(self):
        """Permitir separación por salto de línea además de comas"""
        self.assertEqual(add_v3("1,2\n3"), 6)

    def test_invalid_mixed_newline_and_comma(self):
        """No permitir coma seguida de salto de línea como separación"""
        with self.assertRaises(ValueError):
            add_v3("2,\n3")

    # Requerimiento 4
    def test_separator_at_end_raises_error(self):
        """Mostrar error si hay separador al final de la cadena"""
        with self.assertRaises(ValueError):
            add_v4("1,2,")

    # Requerimiento 5
    def test_custom_delimiter_semicolon(self):
        """Permitir delimitador personalizado ';'"""
        self.assertEqual(add_v5("//;\n1;3"), 4)

    def test_custom_delimiter_pipe(self):
        """Permitir delimitador personalizado '|'"""
        self.assertEqual(add_v5("//|\n1|2|3"), 6)

    def test_custom_delimiter_word(self):
        """Permitir delimitador personalizado con palabra, ej. 'sep'"""
        self.assertEqual(add_v5("//sep\n2sep5"), 7)

    def test_mixed_delimiters_should_raise_error(self):
        """Mostrar error si se mezclan delimitadores distintos"""
        with self.assertRaisesRegex(
            ValueError, r"'|' expected but ',' found at position 3"
        ):
            add_v5("//|\n1|2,3")

    # Requerimiento 6
    def test_negative_number_single(self):
        """Mostrar mensaje de error si hay un número negativo"""
        self.assertEqual(add_v6("1,-2"), "Negative number(s) not allowed: -2")

    def test_negative_numbers_multiple(self):
        """Mostrar mensaje de error con todos los números negativos encontrados"""
        self.assertEqual(add_v6("2,-4,-9"), "Negative number(s) not allowed: -4, -9")

    # Requerimiento 7
    def test_multiple_errors_combined(self):
        """Mostrar todos los mensajes de error combinados (negativos y delimitador incorrecto)"""
        self.assertEqual(
            add_v7("//|\n1|2,-3"),
            "Negative number(s) not allowed: -3\n'|' expected but ',' found at position 3.",
        )

    # Requerimiento 8
    def test_ignore_numbers_greater_than_1000(self):
        """Ignorar números mayores a 1000"""
        self.assertEqual(add_v8("2,1001"), 2)

    def test_include_numbers_less_or_equal_to_1000(self):
        """Incluir números menores o iguales a 1000 en la suma"""
        self.assertEqual(add_v8("2,1000"), 1002)
