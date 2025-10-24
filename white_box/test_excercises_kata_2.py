# -*- coding: utf-8 -*-
"""Module test function add"""
import unittest

from white_box.string_calculator import add


class TestStringCalculator(unittest.TestCase):
    """Pruebas de los requerimientos del String Calculator"""

    # Requerimiento 1
    def test_should_return_zero_when_input_is_empty_string(self):
        """Cadena vacía: devuelve 0"""
        self.assertEqual(add(""), 0)

    def test_should_return_same_number_when_input_has_single_number(self):
        """Un número: devuelve el mismo número"""
        self.assertEqual(add("1"), 1)

    def test_should_return_sum_when_input_has_two_numbers_separated_by_comma(self):
        """Dos números separados por coma: devuelve su suma"""
        self.assertEqual(add("1,2"), 3)

    # Requerimiento 2
    def test_should_return_sum_when_input_has_multiple_numbers_separated_by_comma(self):
        """Manejar varios números separados por coma: devuelve su suma"""
        self.assertEqual(add("1,2,3,4,5"), 15)

    # Requerimiento 3
    def test_should_return_sum_when_input_contains_newline_separators(self):
        """Permitir separación por salto de línea además de comas"""
        self.assertEqual(add("1,2\n3"), 6)

    def test_should_raise_value_error_when_comma_and_newline_are_mixed_as_separators(
        self,
    ):
        """No permitir coma seguida de salto de línea como separación"""
        with self.assertRaises(ValueError):
            add("2,\n3")

    # Requerimiento 4
    def test_should_raise_value_error_when_input_ends_with_separator(self):
        """Mostrar error si hay separador al final de la cadena"""
        with self.assertRaises(ValueError):
            add("1,2,")

    # Requerimiento 5
    def test_should_return_sum_when_custom_delimiter_is_semicolon(self):
        """Permitir delimitador personalizado ';'"""
        self.assertEqual(add("//;\n1;3"), 4)

    def test_should_return_sum_when_custom_delimiter_is_pipe(self):
        """Permitir delimitador personalizado '|'"""
        self.assertEqual(add("//|\n1|2|3"), 6)

    def test_should_return_sum_when_custom_delimiter_is_word(self):
        """Permitir delimitador personalizado con palabra, ej. 'sep'"""
        self.assertEqual(add("//sep\n2sep5"), 7)

    def test_should_raise_value_error_when_mixed_delimiters_are_used(self):
        """Mostrar error si se mezclan delimitadores distintos"""
        with self.assertRaisesRegex(
            ValueError, r"'|' expected but ',' found at position 3"
        ):
            add("//|\n1|2,3")

    # Requerimiento 6
    def test_should_return_error_message_when_negative_number_is_present(self):
        """Mostrar mensaje de error si hay un número negativo"""
        self.assertEqual(add("1,-2"), "Negative number(s) not allowed: -2")

    def test_should_return_error_message_when_multiple_negative_numbers_are_present(
        self,
    ):
        """Mostrar mensaje de error con todos los números negativos encontrados"""
        self.assertEqual(add("2,-4,-9"), "Negative number(s) not allowed: -4, -9")

    # Requerimiento 7
    def test_should_return_all_error_messages_when_multiple_errors_occur(self):
        """Mostrar todos los mensajes de error combinados (negativos y delimitador incorrecto)"""
        with self.assertRaisesRegex(
            ValueError,
            r"Negative number(s) not allowed: -3\n'|' expected but ',' found at position 3.",
        ):
            add("//|\n1|2,-3")

    # Requerimiento 8
    def test_should_ignore_numbers_greater_than_1000_when_calculating_sum(self):
        """Ignorar números mayores a 1000"""
        self.assertEqual(add("2,1001"), 2)

    def test_should_include_numbers_less_or_equal_to_1000_when_calculating_sum(self):
        """Incluir números menores o iguales a 1000 en la suma"""
        self.assertEqual(add("2,1000"), 1002)
