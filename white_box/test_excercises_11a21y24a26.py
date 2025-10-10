# -*- coding: utf-8 -*-
"""
Unit tests for white_box exercises 4 to 10, and 23.
"""

import unittest

from white_box.class_exercises import (
    DocumentEditingSystem,
    ElevatorSystem,
    UserAuthentication,
    authenticate_user,
    calculate_quantity_discount,
    calculate_shipping_cost,
    check_file_size,
    check_flight_eligibility,
    check_loan_eligibility,
    get_weather_advisory,
    grade_quiz,
    validate_credit_card,
    validate_date,
    validate_url,
)


class TestWhiteBoxValidateCreditCard(unittest.TestCase):
    """
    White-box tests for function 11: validate_credit_card.
    """

    def test_valid_card_13_length_and_digits(self):
        """Card number with 13 digits, all numeric, should be valid."""
        self.assertEqual(validate_credit_card("1234567890123"), "Valid Card")

    def test_valid_card_16_length_and_digits(self):
        """Card number with 16 digits, all numeric, should be valid."""
        self.assertEqual(validate_credit_card("1234567890123456"), "Valid Card")

    def test_invalid_card_non_digit_characters(self):
        """Card number with non-digit characters should be invalid."""
        self.assertEqual(validate_credit_card("1234abcd5678"), "Invalid Card")

    def test_invalid_card_too_short(self):
        """Card number shorter than 13 digits should be invalid."""
        self.assertEqual(validate_credit_card("123456789012"), "Invalid Card")

    def test_invalid_card_too_long(self):
        """Card number longer than 16 digits should be invalid."""
        self.assertEqual(validate_credit_card("12345678901234567"), "Invalid Card")


class TestWhiteBoxValidateDate(unittest.TestCase):
    """
    White-box tests for function 12: validate_date.
    """

    def test_valid_date_with_inferior_range(self):
        """Valid date with year, month, and day in inferior range should return 'Valid Date'."""
        self.assertEqual(validate_date(1900, 1, 1), "Valid Date")

    def test_valid_date_with_superior_range(self):
        """Valid date with year, month, and day in superior range should return 'Valid Date'."""
        self.assertEqual(validate_date(2100, 12, 31), "Valid Date")

    def test_invalid_year_below_1900(self):
        """Year below 1900 should return 'Invalid Date'."""
        self.assertEqual(validate_date(1899, 5, 20), "Invalid Date")

    def test_invalid_year_above_2100(self):
        """Year above 2100 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2101, 5, 20), "Invalid Date")

    def test_invalid_month_above_12(self):
        """Month above 12 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2020, 13, 10), "Invalid Date")

    def test_invalid_month_below_1(self):
        """Month below 1 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2020, 0, 10), "Invalid Date")

    def test_invalid_day_above_31(self):
        """Day above 31 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2020, 12, 32), "Invalid Date")

    def test_invalid_day_below_1(self):
        """Day below 1 should return 'Invalid Date'."""
        self.assertEqual(validate_date(2020, 12, 0), "Invalid Date")


class TestWhiteBoxCheckFlightEligibility(unittest.TestCase):
    """
    White-box tests for function 13: check_flight_eligibility.
    """

    def test_eligible_age_with_inferior_range_no_frequent(self):
        """Passenger aged 18 should be eligible."""
        self.assertEqual(check_flight_eligibility(18, False), "Eligible to Book")

    def test_eligible_age_with_superior_range_no_frequent(self):
        """Passenger aged 65 should be eligible."""
        self.assertEqual(check_flight_eligibility(65, False), "Eligible to Book")

    def test_eligible_age_with_inferior_range_frequent(self):
        """Passenger aged 18 should be eligible."""
        self.assertEqual(check_flight_eligibility(18, True), "Eligible to Book")

    def test_eligible_age_with_superior_range_frequent(self):
        """Passenger aged 65 should be eligible."""
        self.assertEqual(check_flight_eligibility(65, True), "Eligible to Book")

    def test_eligible_frequent_flyer_underage_frequent(self):
        """Underage frequent flyer should be eligible."""
        self.assertEqual(check_flight_eligibility(17, True), "Eligible to Book")

    def test_not_eligible_underage_no_frequent(self):
        """Underage and not a frequent flyer should not be eligible."""
        self.assertEqual(check_flight_eligibility(17, False), "Not Eligible to Book")

    def test_eligible_overage_frequent(self):
        """Overage but frequent flyer should be eligible."""
        self.assertEqual(check_flight_eligibility(66, True), "Eligible to Book")

    def test_eligible_overage_no_frequent(self):
        """Overage but frequent flyer should be eligible."""
        self.assertEqual(check_flight_eligibility(66, False), "Not Eligible to Book")


class TestWhiteBoxValidateURL(unittest.TestCase):
    """
    White-box tests for function 14: validate_url.
    """

    def test_valid_https_url(self):
        """Valid HTTPS URL should be accepted."""
        self.assertEqual(validate_url("https://example.com"), "Valid URL")

    def test_valid_http_url(self):
        """Valid HTTP URL should be accepted."""
        self.assertEqual(validate_url("http://example.com"), "Valid URL")

    def test_invalid_protocol_url(self):
        """URL without http/https prefix should be invalid."""
        self.assertEqual(validate_url("ftp://example.com"), "Invalid URL")

    def test_invalid_http_url_too_long(self):
        """URL longer than 255 characters should be invalid."""
        long_url = "http://" + "a" * 260 + ".com"
        self.assertEqual(validate_url(long_url), "Invalid URL")


class TestWhiteBoxCalculateQuantityDiscount(unittest.TestCase):
    """
    White-box tests for function 15: calculate_quantity_discount.
    """

    def test_quantity_1_no_discount(self):
        """Quantity 1 should have no discount."""
        self.assertEqual(calculate_quantity_discount(1), "No Discount")

    def test_quantity_5_no_discount(self):
        """Quantity 5 should have no discount."""
        self.assertEqual(calculate_quantity_discount(5), "No Discount")

    def test_five_percent_discount_quantity_6(self):
        """Quantity 6 should apply 5% discount."""
        self.assertEqual(calculate_quantity_discount(6), "5% Discount")

    def test_five_percent_discount_quantity_10(self):
        """Quantity 10 should apply 5% discount."""
        self.assertEqual(calculate_quantity_discount(10), "5% Discount")

    def test_ten_percent_discount_above_10(self):
        """Quantity greater than 10 should apply 10% discount."""
        self.assertEqual(calculate_quantity_discount(11), "10% Discount")


class TestWhiteBoxCheckFileSize(unittest.TestCase):
    """
    White-box tests for function 16: check_file_size.
    """

    def test_valid_file_size_with_inferior_limit(self):
        """File size within range should be valid."""
        self.assertEqual(check_file_size(0), "Valid File Size")

    def test_valid_file_size_at_upper_bound(self):
        """File size exactly 1MB should be valid."""
        self.assertEqual(check_file_size(1048576), "Valid File Size")

    def test_invalid_file_size_negative(self):
        """Negative file size should be invalid."""
        self.assertEqual(check_file_size(-1), "Invalid File Size")

    def test_invalid_file_size_above_limit(self):
        """File size above 1MB should be invalid."""
        self.assertEqual(check_file_size(1048577), "Invalid File Size")


class TestWhiteBoxCheckLoanEligibility(unittest.TestCase):
    """
    White-box tests for function 17: check_loan_eligibility.
    """

    def test_not_eligible_low_income(self):
        """Income below 30000 should be not eligible."""
        self.assertEqual(check_loan_eligibility(29999, 800), "Not Eligible")

    def test_standard_loan_30000_income_701_score(self):
        """Income between 30000-60000 and credit score >700 should get standard loan."""
        self.assertEqual(check_loan_eligibility(30000, 701), "Standard Loan")

    def test_standard_loan_60000_income_701_score(self):
        """Income between 30000-60000 and credit score >700 should get standard loan."""
        self.assertEqual(check_loan_eligibility(60000, 701), "Standard Loan")

    def test_secured_loan_30000_income_700_score(self):
        """Income between 30000-60000 and credit score <=700 should get secured loan."""
        self.assertEqual(check_loan_eligibility(30000, 700), "Secured Loan")

    def test_secured_loan_60000_income_700_score(self):
        """Income between 30000-60000 and credit score <=700 should get secured loan."""
        self.assertEqual(check_loan_eligibility(60000, 700), "Secured Loan")

    def test_premium_loan_high_income_751_score(self):
        """High income and high credit score should get premium loan."""
        self.assertEqual(check_loan_eligibility(70000, 751), "Premium Loan")

    def test_standard_loan_high_income_750_score(self):
        """High income but low credit score should get standard loan."""
        self.assertEqual(check_loan_eligibility(70000, 750), "Standard Loan")


class TestWhiteBoxCalculateShippingCost(unittest.TestCase):
    """
    White-box tests for function 18: calculate_shipping_cost.
    """

    def test_small_package_low_weight_and_dimensions(self):
        """Small package should cost 5."""
        self.assertEqual(calculate_shipping_cost(1, 10, 10, 10), 5)

    def test_medium_package_inferior_range(self):
        """Medium package with weight and dimensions in range should cost 10."""
        self.assertEqual(calculate_shipping_cost(2, 11, 11, 11), 10)

    def test_medium_package_superior_range(self):
        """Medium package with weight and dimensions in range should cost 10."""
        self.assertEqual(calculate_shipping_cost(5, 30, 30, 30), 10)

    def test_large_package_out_of_range(self):
        """Large package outside defined ranges should cost 20."""
        self.assertEqual(calculate_shipping_cost(6, 31, 31, 31), 20)


class TestWhiteBoxGradeQuiz(unittest.TestCase):
    """
    White-box tests for function 19: grade_quiz.
    """

    def test_pass_condition(self):
        """Correct answers >=7 and incorrect <=2 should result in Pass."""
        self.assertEqual(grade_quiz(7, 2), "Pass")

    def test_conditional_pass_condition(self):
        """Correct answers >=5 and incorrect <=3 should result in Conditional Pass."""
        self.assertEqual(grade_quiz(5, 3), "Conditional Pass")

    def test_fail_condition(self):
        """Other combinations should result in Fail."""
        self.assertEqual(grade_quiz(4, 4), "Fail")


class TestWhiteBoxAuthenticateUser(unittest.TestCase):
    """
    White-box tests for function 20: authenticate_user.
    """

    def test_admin_login(self):
        """Admin credentials should return 'Admin'."""
        self.assertEqual(authenticate_user("admin", "admin123"), "Admin")

    def test_valid_user_login(self):
        """Username and password with valid lengths should return 'User'."""
        self.assertEqual(authenticate_user("user5", "password"), "User")

    def test_invalid_login(self):
        """Invalid credentials should return 'Invalid'."""
        self.assertEqual(authenticate_user("user", "passwor"), "Invalid")


class TestWhiteBoxGetWeatherAdvisory(unittest.TestCase):
    """
    White-box tests for function 21: get_weather_advisory.
    """

    def test_high_temp_and_humidity(self):
        """High temperature and humidity should return hydration advisory."""
        self.assertEqual(
            get_weather_advisory(31, 71),
            "High Temperature and Humidity. Stay Hydrated.",
        )

    def test_low_temperature(self):
        """Temperature below 0 should return bundle up advisory."""
        self.assertEqual(get_weather_advisory(-1, 50), "Low Temperature. Bundle Up!")

    def test_no_specific_advisory(self):
        """Normal conditions should return no specific advisory."""
        self.assertEqual(get_weather_advisory(30, 70), "No Specific Advisory")


class TestUserAuthentication(unittest.TestCase):
    """
    White-box tests for UserAuthentication class problem 24.
    """

    def setUp(self):
        """Initialize a UserAuthentication instance with default state 'Logged Out'."""
        self.auth = UserAuthentication()
        self.assertEqual(self.auth.state, "Logged Out")

    def test_login_successful(self):
        """Test that login works correctly when the user is logged out."""
        result = self.auth.login()
        self.assertEqual(result, "Login successful")
        self.assertEqual(self.auth.state, "Logged In")

    def test_login_invalid_when_already_logged_in(self):
        """Test that logging in twice returns an invalid operation message."""
        self.auth.login()  # log in first
        result = self.auth.login()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged In")

    def test_logout_successful(self):
        """Test that logout works correctly when the user is logged in."""
        self.auth.login()
        result = self.auth.logout()
        self.assertEqual(result, "Logout successful")
        self.assertEqual(self.auth.state, "Logged Out")

    def test_logout_invalid_when_logged_out(self):
        """Test that trying to logout while already logged out is invalid."""
        result = self.auth.logout()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.auth.state, "Logged Out")


class TestDocumentEditingSystem(unittest.TestCase):
    """
    White-box tests for DocumentEditingSystem class problem 25.
    """

    def setUp(self):
        """Initialize a DocumentEditingSystem instance with default state 'Editing'."""
        self.doc = DocumentEditingSystem()
        self.assertEqual(self.doc.state, "Editing")

    def test_save_document_success(self):
        """Test that saving a document while editing changes the state to 'Saved'."""
        result = self.doc.save_document()
        self.assertEqual(result, "Document saved successfully")
        self.assertEqual(self.doc.state, "Saved")

    def test_save_document_invalid_when_saved(self):
        """Test that saving again when already saved returns an invalid operation."""
        self.doc.save_document()
        result = self.doc.save_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Saved")

    def test_edit_document_success(self):
        """Test that editing a document after saving resumes editing mode."""
        self.doc.save_document()
        result = self.doc.edit_document()
        self.assertEqual(result, "Editing resumed")
        self.assertEqual(self.doc.state, "Editing")

    def test_edit_document_invalid_when_editing(self):
        """Test that editing a document already being edited is invalid."""
        result = self.doc.edit_document()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.doc.state, "Editing")


class TestElevatorSystem(unittest.TestCase):
    """
    White-box tests for ElevatorSystem class problem 26.
    """

    def setUp(self):
        """Initialize an ElevatorSystem instance with default state 'Idle'."""
        self.elevator = ElevatorSystem()
        self.assertEqual(self.elevator.state, "Idle")

    def test_move_up_success(self):
        """Test that moving up from idle works correctly."""
        result = self.elevator.move_up()
        self.assertEqual(result, "Elevator moving up")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_up_invalid_when_moving(self):
        """Test that trying to move up again while already moving up is invalid."""
        self.elevator.move_up()
        result = self.elevator.move_up()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Up")

    def test_move_down_success(self):
        """Test that moving down from idle works correctly."""
        self.elevator = ElevatorSystem()  # reset
        result = self.elevator.move_down()
        self.assertEqual(result, "Elevator moving down")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_move_down_invalid_when_moving(self):
        """Test that trying to move down again while already moving down is invalid."""
        self.elevator.move_down()
        result = self.elevator.move_down()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Moving Down")

    def test_stop_success_from_moving_up(self):
        """Test that stopping works when elevator is moving up."""
        self.elevator.move_up()
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_success_from_moving_down(self):
        """Test that stopping works when elevator is moving down."""
        self.elevator.move_down()
        result = self.elevator.stop()
        self.assertEqual(result, "Elevator stopped")
        self.assertEqual(self.elevator.state, "Idle")

    def test_stop_invalid_when_idle(self):
        """Test that stopping while idle returns an invalid operation message."""
        result = self.elevator.stop()
        self.assertEqual(result, "Invalid operation in current state")
        self.assertEqual(self.elevator.state, "Idle")
