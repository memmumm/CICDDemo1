import unittest
import src.calculator as summa

class TestCalculator(unittest.TestCase):
    # plusfunktio
    def test_plus_function_works_with_integers(self):
        # Arrange
        num1 = num2 = 2
        expected_result = 4
        # Act
        result = summa.plus(num1, num2)
        # Assert
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
