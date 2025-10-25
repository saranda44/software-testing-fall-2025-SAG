# -*- coding: utf-8 -*-
"""Module test function fizzbuzz"""
import unittest

from white_box.validate_password import validate_password, validate_password_v


class TestValidatePassword(unittest.TestCase):
    """White-box tests for password validation"""

    # ---- Requerimiento 1: longitud mínima ----
    def test_password_too_short(self):
        """Password shorter than 8 characters should fail."""
        result = validate_password("Ab1@111")
        self.assertFalse(result["is_valid"])
        self.assertIn("Password must be at least 8 characters", result["errors"])

    def test_password_exactly_8_characters(self):
        """Password with exactly 8 characters passes length rule, but is not valid."""
        result = validate_password("password")
        self.assertNotIn("Password must be at least 8 characters", result["errors"])

    # ---- Requerimiento 2: al menos 2 números ----
    def test_password_with_no_numbers(self):
        """Password without digits should fail."""
        result = validate_password("Abcdef@x")
        self.assertFalse(result["is_valid"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_one_number(self):
        """Password with only one digit should fail."""
        result = validate_password("Abcdef1@")
        self.assertFalse(result["is_valid"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])

    def test_password_with_two_numbers(self):
        """Password with two digits passes that rule, but is not valid yet."""
        result = validate_password("abcdef12")
        self.assertNotIn(
            "The password must contain at least 2 numbers", result["errors"]
        )

    # ---- Requerimiento 3: múltiples errores ----
    def test_password_with_multiple_errors(self):
        """Password failing several validations returns all errors."""
        result = validate_password_v("abc")
        self.assertFalse(result["is_valid"])
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )
        self.assertGreaterEqual(len(result["errors"]), 4)

    # ---- Requerimiento 4: al menos una mayúscula ----
    def test_password_without_capital_letter(self):
        """Password without uppercase should fail."""
        result = validate_password_v("abcde12@")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )

    def test_password_with_capital_letter(self):
        """Password with uppercase passes."""
        result = validate_password_v("Abcde123")
        self.assertFalse(result["is_valid"])
        self.assertNotIn(
            "password must contain at least one capital letter", result["errors"]
        )

    # ---- Requerimiento 5: al menos un carácter especial ----
    def test_password_without_special_character(self):
        """Password without special character should fail."""
        result = validate_password_v("Abcde123")
        self.assertFalse(result["is_valid"])
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )

    def test_password_with_special_character(self):
        """Password with special character passes."""
        result = validate_password_v("Abcde12@")
        self.assertTrue(result["is_valid"])
        self.assertNotIn(
            "password must contain at least one special character", result["errors"]
        )

    # Otros casos
    def test_empty_password(self):
        """Empty password should fail all checks."""
        result = validate_password_v("")
        self.assertFalse(result["is_valid"])
        self.assertIn("Password must be at least 8 characters", result["errors"])
        self.assertIn("The password must contain at least 2 numbers", result["errors"])
        self.assertIn(
            "password must contain at least one capital letter", result["errors"]
        )
        self.assertIn(
            "password must contain at least one special character", result["errors"]
        )

    def test_valid_password(self):
        """Password meets all requirements."""
        result = validate_password_v("Valid12@")
        self.assertTrue(result["is_valid"])
        self.assertEqual(result["errors"], [])
