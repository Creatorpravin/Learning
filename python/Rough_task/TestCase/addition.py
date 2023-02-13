import unittest

def add(a, b):
    return a + b

class TestAddition(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(1, 2), 3)
        self.assertEqual(add(0, 0), 0)
        self.assertEqual(add(-1, -1), -2)

if __name__ == '__main__':
    unittest.main()
