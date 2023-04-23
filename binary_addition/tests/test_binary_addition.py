import unittest
from binary_addition import add_binary
from binary_addition import binary_addition


def test(func):
    def wrapper(*args, **kwargs):
        print("\rRunning test: ", func.__name__)
        return func(*args, **kwargs)
    return wrapper

class TestBinaryAddition(unittest.TestCase):
    
    @test
    def add_binary(self):
        self.assertEqual(binary_addition(1,1),"10")
        # self.assertEqual(add_binary(0,1),"1")
        # self.assertEqual(add_binary(1,0),"1")
        # self.assertEqual(add_binary(2,2),"100")
        # self.assertEqual(add_binary(51,12),"111111")

if __name__ == '__main__':
    unittest.main()