import unittest

class Test2(unittest.TestCase):
    def test_A(self):
        self.assertTrue('FOO'.isupper())

if __name__ == '__main__':
    unittest.main()
