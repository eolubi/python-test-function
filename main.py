import unittest


# Function to test
def add_numbers(x, y):
    return x + y


# Test class
class TestAddNumbers(unittest.TestCase):
    # Test case 1: Test adding positive integers
    def test_add_positive_integers(self):
        self.assertEqual(add_numbers(2, 3), 5)
        self.assertEqual(add_numbers(100, 200), 300)

    # Test case 2: Test adding negative integers
    def test_add_negative_integers(self):
        self.assertEqual(add_numbers(-2, -3), -5)
        self.assertEqual(add_numbers(-100, -200), -300)

    # Test case 3: Test adding positive and negative integers
    def test_add_mixed_integers(self):
        self.assertEqual(add_numbers(-2, 3), 1)
        self.assertEqual(add_numbers(100, -200), -100)

    # Test case 4: Test adding zero to an integer
    def test_add_zero(self):
        self.assertEqual(add_numbers(2, 0), 2)
        self.assertEqual(add_numbers(-100, 0), -100)


# Run the tests
if __name__ == '__main__':
    unittest.main()