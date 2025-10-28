# -*- coding: utf-8 -*-
"""Data-driven tests for Account class"""

from unittest.mock import patch

# pylint: disable=import-error
import pytest

from white_box.account import Account


@pytest.mark.parametrize(
    "initial_balance, deposit_amount, expected_balance",
    [
        (0, 1000, 1000),
        (500, 500, 1000),
        (200, 0, 200),
    ],
)
def test_should_increase_balance_when_deposit(
    initial_balance, deposit_amount, expected_balance
):
    """Req 1: Deposit into Account"""
    account = Account()
    account.balance = initial_balance
    account.deposit(deposit_amount)
    assert account.balance == expected_balance


@pytest.mark.parametrize(
    "initial_balance, withdraw_amount, expected_balance",
    [
        (1000, 100, 900),
        (500, 200, 300),
        (1000, 1000, 0),
    ],
)
def test_should_decrease_balance_when_withdraw(
    initial_balance, withdraw_amount, expected_balance
):
    """Req 2: Withdraw from Account"""
    account = Account()
    account.balance = initial_balance
    account.withdraw(withdraw_amount)
    assert account.balance == expected_balance


@pytest.mark.parametrize(
    "transactions, expected_output",
    [
        (
            [
                ("01/04/2014", 1000),
                ("02/04/2014", -100),
                ("10/04/2014", 500),
            ],
            (
                "DATE       | AMOUNT  | BALANCE\n"
                "10/04/2014 | 500.00  | 1400.00\n"
                "02/04/2014 | -100.00  | 900.00\n"
                "01/04/2014 | 1000.00  | 1000.00"
            ),
        ),
    ],
)
def test_should_print_statement_when_transactions_exist(transactions, expected_output):
    """
    Req 3: Print the account statement to the console
    """
    account = Account()

    for date, amount in transactions:
        if amount >= 0:
            account.deposit(amount, date)
        else:
            account.withdraw(abs(amount), date)

    with patch("builtins.print") as mock_print:
        account.print_statement()

        # Construimos la lista de llamadas esperadas

        expected_lines = expected_output.split("\n")
        actual_lines = [args[0] for args, *_ in mock_print.call_args_list]

        assert actual_lines == expected_lines
