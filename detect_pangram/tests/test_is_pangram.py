import unittest
from is_pangram import is_pangram


def test(func):
    def wrapper(*args, **kwargs):
        print("\rRunning test: ", func.__name__)
        return func(*args, **kwargs)
    return wrapper

class TestIsPangram(unittest.TestCase):
    
    @test
    def test_pangram(self):
        self.assertEqual(is_pangram("The quick, brown fox jumps over the lazy dog!"), True)
        self.assertEqual(is_pangram("pbcfemiyvhudxlkwzjroqtnags"), True)

    @test
    def test_not_pangram(self):
        self.assertEqual(is_pangram("1bcdefghijklmnopqrstuvwxyz"), False)
        self.assertEqual(is_pangram("01234567891011121314151617"), False)

if __name__ == '__main__':
    unittest.main()