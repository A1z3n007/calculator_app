import unittest
from core import calculate

class TestCalculatorCore(unittest.TestCase):
    
    def test_addition(self):
        self.assertEqual(calculate("2+3"), 5)

    def test_subtraction(self):
        self.assertEqual(calculate("5-2"), 3)

    def test_multiplication(self):
        self.assertEqual(calculate("3*4"), 12)

    def test_division(self):
        self.assertEqual(calculate("10/2"), 5)

    def test_zero_division(self):
        self.assertIn("Ошибка", calculate("5/0"))
        
    def test_invalid_expression(self):
        self.assertIn("Ошибка", calculate("2++2"))

    def test_invalid_characters(self):
        self.assertIn("Ошибка", calculate("import os"))

if __name__ == "__main__":
    unittest.main()