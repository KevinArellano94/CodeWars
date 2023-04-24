import unittest
from xo.solution import xo

def test(func):
    def wrapper(*args, **kwargs):
        print("\rRunning test: ", func.__name__)
        return func(*args, **kwargs)
    return wrapper

class TestXO(unittest.TestCase):
    @test
    def test_xo(self):
        self.assertEqual(xo('xo'), True)
    
    @test
    def test_xo0(self):
        self.assertEqual(xo('xo0'), True)
    
    @test
    def test_xxxoo(self):
        self.assertEqual(xo('xxxoo'), False)