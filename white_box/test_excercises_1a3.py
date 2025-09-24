import unittest

from white_box.class_exercises import (
    check_number_status,
    validate_password,
    calculate_total_discount
)


class TestWhiteBox(unittest.TestCase):
    """
    White-box unittest class.
    """
    # 1
    def test_check_number_status_with_positive_number(self):
        """
        Checks if a number is positive.
        """
        self.assertEqual(check_number_status(0.01), 'Positive')

    def test_check_number_status_with_negative_number(self):
        """
        Checks if a number is negative.
        """
        self.assertEqual(check_number_status(-0.01), 'Negative')

    def test_check_number_status_with_zero(self):
        """
        Checks if a number is zero.
        """
        self.assertEqual(check_number_status(0),'Zero')

    #2
    def test_password_too_short(self):
        """
        Password shorter than 8 characters.
        """
        self.assertFalse(validate_password("Ab1!"))

    def test_password_with_no_uppercase(self):
        """
        Password without uppercase.
        """
        self.assertFalse(validate_password("ab1!ab1!"))

    def test_password_with_no_lowercase(self):
        """
        Password without lowercase.
        """
        self.assertFalse(validate_password("AB1!AB1!"))

    def test_password_with_no_digit(self):
        """
        Password without digits.
        """
        self.assertFalse(validate_password("Abc!Abcd"))

    def test_password_with_no_special_character(self):
        """
        Password without special character.
        """
        self.assertFalse(validate_password("Abc12345"))

    def test_password_valid(self):
        """
        Password with all requirements
        """
        self.assertTrue(validate_password("Abc123!d"))

    #3
    def test_amount_below_100(self):
        """
        Amount less than 100.
        """
        self.assertEqual(calculate_total_discount(99.99), 0)

    def test_amount_equal_100(self):
        """
        Amount equal to 100.
        """
        self.assertEqual(calculate_total_discount(100), 10)

    def test_amount_between_100_and_500(self):
        """
        Amount between 100 and 500.
        """
        self.assertEqual(calculate_total_discount(250), 25)

    def test_amount_equal_500(self):
        """
        Amount equal to 500
        """
        self.assertEqual(calculate_total_discount(500), 50)

    def test_amount_above_500(self):
        """
        Amount greater than 500.
        """
        self.assertEqual(round(calculate_total_discount(500.01),3), 100.002)
    