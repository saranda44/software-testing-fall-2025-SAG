# -*- coding: utf-8 -*-
"""
Unit tests for white_box exercises 4 to 10, and 23.
"""

import unittest

from white_box.class_exercises import (
    calculate_order_total,
    calculate_items_shipping_cost,
    validate_login,
    verify_age,
    categorize_product,
    validate_email,
    celsius_to_fahrenheit,
    TrafficLight
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
        self.assertEqual(round(calculate_order_total(items),0), 285)

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
            {"quantity": 2, "price": 100},   # no discount → 200
            {"quantity": 7, "price": 50},    # 5% discount → 332.5
            {"quantity": 15, "price": 10},   # 10% discount → 135
        ]
        expected_total = 200 + 332.5 + 135  # = 667.5
        self.assertEqual(calculate_order_total(items), expected_total)

class TestWhiteBoxCalculateItemsShippingCost(unittest.TestCase):
    """
    White-box tests for calculate_items_shipping_cost.
    """
    
    #5
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
        self.assertEqual(validate_login("user5", "password"), "Login Successful")

    def test_login_successful_on_upper_bounds(self):
        username = "u" * 20
        password = "p" * 15
        self.assertEqual(validate_login(username, password), "Login Successful")

    def test_login_failed_short_username(self):
        self.assertEqual(validate_login("usr", "password"), "Login Failed")

    def test_login_failed_short_password(self):
        self.assertEqual(validate_login("username", "123"), "Login Failed")

    def test_login_failed_long_password(self):
        self.assertEqual(validate_login("username", "p" * 16), "Login Failed")


class TestWhiteBoxVerifyAge(unittest.TestCase):
    """
    White-box tests for functions 7.
    """

    # 7 verify_age
    def test_age_exactly_18(self):
        self.assertEqual(verify_age(18), "Eligible")

    def test_age_exactly_65(self):
        self.assertEqual(verify_age(65), "Eligible")

    def test_age_below_18(self):
        self.assertEqual(verify_age(17), "Not Eligible")

    def test_age_above_65(self):
        self.assertEqual(verify_age(70), "Not Eligible")


class TestWhiteBoxCategorizeProduct(unittest.TestCase):
    """
    White-box tests for functions 8.
    """

    # 8 categorize_product
    def test_price_category_a_lower_bound(self):
        self.assertEqual(categorize_product(10), "Category A")

    def test_price_category_a_upper_bound(self):
        self.assertEqual(categorize_product(50), "Category A")

    def test_price_category_b_lower_bound(self):
        self.assertEqual(categorize_product(51), "Category B")

    def test_price_category_b_upper_bound(self):
        self.assertEqual(categorize_product(100), "Category B")

    def test_price_category_c_lower_bound(self):
        self.assertEqual(categorize_product(101), "Category C")

    def test_price_category_c_upper_bound(self):
        self.assertEqual(categorize_product(200), "Category C")

    def test_price_category_d_below_10(self):
        self.assertEqual(categorize_product(5), "Category D")

    def test_price_category_d_above_200(self):
        self.assertEqual(categorize_product(500), "Category D")


class TestWhiteBoxValidateEmail(unittest.TestCase):
    """
    White-box tests for functions 9.
    """

    # 9 validate_email
    def test_valid_email_with_min_length(self):
        email = "a@b.c"  # len = 5
        self.assertEqual(validate_email(email), "Valid Email")

    def test_valid_email_with_max_length(self):
        email = "a" * 42 + "@ab.com"  # len = 50
        self.assertEqual(validate_email(email), "Valid Email")

    def test_invalid_email_too_short(self):
        email = "a@b"  # len = 3
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_no_at_symbol(self):
        email = "userexample.com"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_no_dot(self):
        email = "user@examplecom"
        self.assertEqual(validate_email(email), "Invalid Email")

    def test_invalid_email_too_long(self):
        email = "a" * 51 + "@example.com"
        self.assertEqual(validate_email(email), "Invalid Email")


class TestWhiteBoxCelsiusToFahrenheit(unittest.TestCase):
    """
    White-box tests for functions 10.
    """

    # 10 celsius_to_fahrenheit
    def test_temperature_lower_bound(self):
        self.assertEqual(celsius_to_fahrenheit(-100), -148.0)

    def test_temperature_upper_bound(self):
        self.assertEqual(celsius_to_fahrenheit(100), 212.0)

    def test_temperature_within_range(self):
        self.assertEqual(celsius_to_fahrenheit(0), 32.0)

    def test_temperature_below_range(self):
        self.assertEqual(celsius_to_fahrenheit(-101), "Invalid Temperature")

    def test_temperature_above_range(self):
        self.assertEqual(celsius_to_fahrenheit(101), "Invalid Temperature")


class TestWhiteBoxTrafficLight(unittest.TestCase):
    """
    TrafficLight unit tests.
    """

    #23
    def setUp(self):
        self.traffic_light = TrafficLight()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_initial_state(self):
        """
        Verifies that the initial state is Red.
        """
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_change_state_red_to_green(self):
        """
        Verifies state transition: Red -> Green.
        """
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

    def test_change_state_green_to_yellow(self):
        """
        Verifies state transition: Green -> Yellow.
        """
        self.traffic_light.state = "Green"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

    def test_change_state_yellow_to_red(self):
        """
        Verifies state transition: Yellow -> Red.
        """
        self.traffic_light.state = "Yellow"
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")

    def test_full_cycle(self):
        """
        Verifies a complete cycle: Red -> Green -> Yellow -> Red.
        """
        # Red -> Green
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Green")

        # Green -> Yellow
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Yellow")

        # Yellow -> Red
        self.traffic_light.change_state()
        self.assertEqual(self.traffic_light.get_current_state(), "Red")
