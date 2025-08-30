import unittest
from mean_var_std import calculate

class TestMeanVarStd(unittest.TestCase):
    
    def test_valid_input(self):
        data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        result = calculate(data)
        # Test sum of all elements
        self.assertEqual(result['sum'][-1], 36)
        # Test mean of all elements
        self.assertEqual(result['mean'][-1], 4.0)
        # Test max of all elements
        self.assertEqual(result['max'][-1], 8)
    
    def test_invalid_input(self):
        data = [1, 2, 3]  # less than 9 elements
        with self.assertRaises(ValueError):
            calculate(data)

if __name__ == "__main__":
    unittest.main()
