# import pytest
from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

    def test_subtraction(self):
        assert self.calc.subtraction(self, 2, 1) == 1

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 3) == 6

    def test_division(self):
        assert self.calc.division(self, 6, 3) == 2

    def teardown(self):
        print('Выполнение метода Teardown')
