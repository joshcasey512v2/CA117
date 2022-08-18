#!/usr/bin/env python3

class BankAccount(object):

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, i):
        self.balance += i

    def withdraw(self, w):
        if w <= self.balance:
            self.balance -= w
        return f'broke ass'

    def __str__(self):
        return f'Your current balance is {self.balance:.02f} euro'
