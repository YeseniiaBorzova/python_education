"""This module contains simple calculator class.
This class has 4 static methods responsible for
simple arithmetic operations like +-*/"""


class SimpleCalc:
    """This class contains static methods sum,
    difference, multiply and divide responsible for
    +, -, *, / respectively"""

    @staticmethod
    def sum(first_number, second_number):
        """Takes two numbers and return their sum"""
        return first_number+second_number

    @staticmethod
    def difference(first_number, second_number):
        """Takes two numbers and return their difference"""
        return first_number-second_number

    @staticmethod
    def multiply(first_number, second_number):
        """Takes two numbers and return their product"""
        return first_number*second_number

    @staticmethod
    def divide(first_number, second_number):
        """Takes two numbers and return their quotient"""
        return first_number/second_number
