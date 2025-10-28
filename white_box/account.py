# -*- coding: utf-8 -*-
"""class Account"""


class Account:
    """class Account kata 6"""

    def __init__(self, printer=None):
        """setup"""
        self.balance = 0
        self.transactions = []
        self.printer = printer

    def deposit(self, amount, date=None):
        """deposit: add amount to balance"""
        self.balance += amount
        self.transactions.append((date, amount, self.balance))

    def withdraw(self, amount, date=None):
        """withdraw: substract from balance"""
        self.balance -= amount
        self.transactions.append((date, -amount, self.balance))

    def print_statement(self):
        """print transactions"""
        print("DATE       | AMOUNT  | BALANCE")
        for date, amount, balance in reversed(self.transactions):
            print(f"{date} | {amount:.2f}  | {balance:.2f}")
