import unittest
from my_module import get_numbers

class TestGetNumbers(unittest.TestCase):
    def test_get_numbers(self):
        self.assertEqual(get_numbers(), (10, 20, 30))

if __name__ == '__main__':
    unittest.main()