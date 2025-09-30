# -*- coding: utf-8 -*-
"""
Unit tests for white_box exercises 4 to 10, and 23.
"""

import unittest

from white_box.class_exercises import (
    TrafficLight,
    calculate_items_shipping_cost,
    calculate_order_total,
    categorize_product,
    celsius_to_fahrenheit,
    validate_email,
    validate_login,
    verify_age,
)


class TestWhiteBoxCalculateOrderTotal(unittest.TestCase):
    """
    White-box unittest class.
    """

    # 4
    def test_calculate_order_total_with_no_items(self):
        """
        Order with no items should return total 0.
        """
        self.assertEqual(calculate_order_total([]), 0)

    def test_calculate_order_total_with_items_quantity_exactly_1(self):
        """
        Quantity = 1 should apply no discount.
        """
        items = [{"quantity": 1, "price": 100}]
        self.assertEqual(calculate_order_total(items), 100)

    def test_calculate_order_total_with_items_quantity_exactly_5(self):
        """
        Quantity = 5 should still apply no discount.
        """
        items = [{"quantity": 5, "price": 20}]  # 5*20 = 100
        self.assertEqual(calculate_order_total(items), 100)

    def test_calculate_order_total_with_items_quantity_between_1_and_5(self):
        """
        Items with quantity between 1 and 5 should have no discount.
        """
        items = [{"quantity": 3, "price": 100}]  # 3 * 100 = 300
        self.assertEqual(calculate_order_total(items), 300)

    def test_calculate_order_total_with_items_quantity_exactly_6(self):
        """
        Quantity = 6 should apply 5% discount.
        """
        items = [{"quantity": 6, "price": 50}]  # 6*50 = 300 → 285
        self.assertEqual(round(calculate_order_total(items), 0), 285)

    def test_calculate_order_total_with_items_quantity_exactly_10(self):
        """
        Quantity = 10 should apply 5% discount.
        """
        items = [{"quantity": 10, "price": 10}]  # 10*10 = 100 → 95
        self.assertEqual(calculate_order_total(items), 95)

    def test_calculate_order_total_with_items_quantity_between_6_and_10(self):
        """
        Items with quantity between 6 and 10 should get 5% discount.
        """
        items = [{"quantity": 8, "price": 50}]  # 8*50=400 → 5% desc = 380
        self.assertEqual(calculate_order_total(items), 380)

    def test_calculate_order_total_with_items_quantity_above_10(self):
        """
        Quantity = 11 should apply 10% discount.
        """
        items = [{"quantity": 11, "price": 10}]  # 11*10 = 110 → 99
        self.assertEqual(calculate_order_total(items), 99)

    def test_calculate_order_total_with_multiple_items_mixed_quantities(self):
        """
        Multiple items with mixed quantities should apply correct discounts.
        """
        items = [
            {"quantity": 2, "price": 100},  # no discount → 200
            {"quantity": 7, "price": 50},  # 5% discount → 332.5
            {"quantity": 15, "price": 10},  # 10% discount → 135
        ]
        expected_total = 200 + 332.5 + 135  # = 667.5
        self.assertEqual(calculate_order_total(items), expected_total)


class TestWhiteBoxCalculateItemsShippingCost(unittest.TestCase):
    """
    White-box tests for calculate_items_shipping_cost.
    """

    # 5
    def test_standard_shipping_weight_0(self):
        """
        Standard shipping with weight 0 should cost 10.
        """
        items = [{"weight": 0}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_weight_exactly_5(self):
        """
        Standard shipping with weight = 5 should cost 10.
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 10)

    def test_standard_shipping_weight_between_6_and_10(self):
        """
        Standard shipping with weight = 6 should cost 15.
        """
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_weight_exactly_10(self):
        """
        Standard shipping with weight = 10 should cost 15.
        """
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 15)

    def test_standard_shipping_weight_above_10(self):
        """
        Standard shipping with weight = 11 should cost 20.
        """
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "standard"), 20)

    def test_express_shipping_weight_0(self):
        """
        Express shipping with weight 0 should cost 20.
        """
        items = [{"weight": 0}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_weight_exactly_5(self):
        """
        Express shipping with weight = 5 should cost 20.
        """
        items = [{"weight": 5}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 20)

    def test_express_shipping_weight_between_6_and_10(self):
        """
        Express shipping with weight = 6 should cost 30.
        """
        items = [{"weight": 6}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_weight_exactly_10(self):
        """
        Express shipping with weight = 10 should cost 30.
        """
        items = [{"weight": 10}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 30)

    def test_express_shipping_weight_above_10(self):
        """
        Express shipping with weight = 11 should cost 40.
        """
        items = [{"weight": 11}]
        self.assertEqual(calculate_items_shipping_cost(items, "express"), 40)

    def test_invalid_shipping_method(self):
        """
        Invalid shipping method should raise ValueError.
        """
        items = [{"weight": 5}]
        with self.assertRaises(ValueError):
            calculate_items_shipping_cost(items, "overnight")


class TestWhiteBoxValidateLogin(unittest.TestCase):
    """
    White-box tests for functions 6.
    """

    # 6 validate_login
    def test_login_successful_on_lower_bounds(self):
        """Login succeeds with username length 5 and password length 8."""
        self.assertEqual(validate_login("user5", "password"), "Login Successful")

    def test_login_successful_on_upper_bounds(self):
        """Login succeeds with username length 20 and password length 15."""
        username = "u" * 20
        password = "p" * 15
        self.assertEqual(validate_login(username, password), "Login Successful")

    def test_login_failed_short_username(self):
        """Login fails if username is too short (< 5)."""
        self.assertEqual(validate_login("usr", "password"), "Login Failed")

    def test_login_failed_short_password(self):
        """Login fails if password is too short (< 8)."""
        self.assertEqual(validate_login("username", "123"), "Login Failed")

    def test_login_failed_long_password(self):
        """Login fails if password is too long (> 15)."""
        self.assertEqual(validate_login("username", "p" * 16), "Login Failed")


class TestWhiteBoxVerifyAge(unittest.TestCase):
    """
    White-box tests for function verify_age (function 7).
    """

    def test_age_exactly_18(self):
        """Verify that age 18 is considered Eligible."""
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_exactly_65(self):
        """Verify that age 65 is considered Eligible."""
        self.assertEqual(verify_age(65), "Eligible")

    def test_age_below_18(self):
        """Verify that age below 18 is considered Not Eligible."""
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_above_65(self):
        """Verify that age above 65 is considered Not Eligible."""
        self.assertEqual(verify_age(70), "Not Eligible")


class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    """
    White-box tests for function categorize_product (function 8).
    """

    def test_price_category_a_lower_bound(self):
        """Verify that price = 10 falls into Category A."""
        self.assertEqual(categorize_product(10), "Category A")

    def test_price_category_a_upper_bound(self):
        """Verify that price = 50 falls into Category A."""
        self.assertEqual(categorize_product(50), "Category A")

    def test_price_category_b_lower_bound(self):
        """Verify that price = 51 falls into Category B."""
        self.assertEqual(categorize_product(51), "Category B")

    def test_price_category_b_upper_bound(self):
        """Verify that price = 100 falls into Category B."""
        self.assertEqual(categorize_product(100), "Category B")

    def test_price_category_c_lower_bound(self):
        """Verify that price = 101 falls into Category C."""
        self.assertEqual(categorize_product(101), "Category C")

    def test_price_category_c_upper_bound(self):
        """Verify that price = 200 falls into Category C."""
        self.assertEqual(categorize_product(200), "Category C")

    def test_price_category_d_below_10(self):
        """Verify that price < 10 falls into Category D."""
        self.assertEqual(categorize_product(5), "Category D")

    def test_price_category_d_above_200(self):
        """Verify that price > 200 falls into Category D."""
        self.assertEqual(categorize_product(500), "Category D")


class TestWhiteBoxValidateEmail(unittest.TestCase):
    """
    White-box tests for function validate_email (function 9).
    """

    def test_valid_email_with_min_length(self):
        """Verify that an email with minimum length (5) is valid."""
        email = "a@b.c"  # len = 5
        self.assertEqual(validate_email(email), "Valid Email")

    def test_valid_email_with_max_length(self):
        """Verify that an email with maximum length (50) is valid."""
        email = "a" * 42 + "@ab.com"  # len = 50
        self.assertEqual(validate_email(email), "Valid Email")

    def test_invalid_email_too_short(self):
        """Verify that email shorter than 5 characters is invalid."""
        email = "a@b"  # len = 3
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_no_at_symbol(self):
        """Verify that email without '@' is invalid."""
        email = "userexample.com"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_no_dot(self):
        """Verify that email without '.' is invalid."""
        email = "user@examplecom"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_too_long(self):
        """Verify that email longer than 50 characters is invalid."""
        email = "a" * 51 + "@example.com"
        self.assertEqual(validate_email(email), "Invalid Email")


class TestWhiteBoxCelsiusToFahrenheit(unittest.TestCase):
    """
    White-box tests for function celsius_to_fahrenheit (function 10).
    """

    def test_temperature_lower_bound(self):
        """Verify that -100°C converts correctly to -148°F."""
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_temperature_upper_bound(self):
        """Verify that 100°C converts correctly to 212°F."""
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_temperature_within_range(self):
        """Verify that 0°C converts correctly to 32°F."""
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_temperature_below_range(self):
        """Verify that temperature below -100°C is invalid."""
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_temperature_above_range(self):
        """Verify that temperature above 100°C is invalid."""
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestWhiteBoxTrafficLight(unittest.TestCase):
    """
    White-box tests for the TrafficLight class (function 23).
    """

    def setUp(self):
        """Initialize TrafficLight instance with default state Red."""
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_initial_state(self):
        """Verify that the initial state is Red."""
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_change_state_red_to_green(self):
        """Verify state transition from Red to Green."""
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

    def test_change_state_green_to_yellow(self):
        """Verify state transition from Green to Yellow."""
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

    def test_change_state_yellow_to_red(self):
        """Verify state transition from Yellow to Red."""
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_full_cycle(self):
        """Verify a complete cycle: Red -> Green -> Yellow -> Red."""
        # Red -> Green
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

        # Green -> Yellow
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

        # Yellow -> Red
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")
