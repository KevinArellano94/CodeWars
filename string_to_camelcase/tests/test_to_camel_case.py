import unittest
from to_camel_case import to_camel_case

def test(func):
    def wrapper(*args, **kwargs):
        print("\rRunning test: ", func.__name__)
        return func(*args, **kwargs)
    return wrapper

class TestToCamelCase(unittest.TestCase):
    @test
    def test_empty_string(self):
        self.assertEqual(to_camel_case(""), "")
    
    @test
    def test_underscores(self):
        self.assertEqual(to_camel_case("the_stealth_warrior"), "theStealthWarrior")
    
    @test
    def test_dashes(self):
        self.assertEqual(to_camel_case("The-Stealth-Warrior"), "TheStealthWarrior")
    
    @test
    def test_mixed_delimiters(self):
        self.assertEqual(to_camel_case("A-B-C"), "ABC")
        
if __name__ == '__main__':
    unittest.main()