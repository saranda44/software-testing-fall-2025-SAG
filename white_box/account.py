# -*- coding: utf-8 -*-
"""class Account"""


class Account:
    """Class account kata 6"""

    def __init__(self):
        """setup"""
        self.balance = 0

    def deposit(self, amount, date=None):
        """deposit function: add amount to the balance"""
        print(date)
        self.balance += amount

    def withdraw(self, amount, date=None):
        """withdraw function: rest amount to the balance"""
        print(date)
        return amount

    def print_statement(self):
        """print_statement function: print deposits and withdraws"""
        return ""
