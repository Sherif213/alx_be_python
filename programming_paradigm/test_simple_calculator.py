import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(10,5),5)
        self.assertEqual(self.calc.subtract(5,5),0)
        self.assertEqual(self.calc.subtract(0,5),-5)
        
    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(10,5),50)
        self.assertEqual(self.calc.multiply(0,5),0)
        self.assertEqual(self.calc.multiply(1,1),1)
        
    def test_division(self):
        self.assertEqual(self.calc.divide(10,0),None)
        self.assertEqual(self.calc.divide(0,5),0)
        self.assertEqual(self.calc.divide(1,1),1)
        self.assertEqual(self.calc.divide(5,10),0.5)