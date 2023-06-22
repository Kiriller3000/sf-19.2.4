import pytest
from app.calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):
        self.calc.subtraction(self, 2, 1) == 1

    def test_multiply(self):
        self.calc.multiply(self, 2, 3) == 6

    def test_division(self):
        self.calc.division(self, 6, 3) == 2

    def teardown(self):
        print('Выполнение метода Teardown')