import unittest

def Divisibleby7(x):
    if x%7 == 0:
        return True
    else:
        return False
    
class Checkdivisible1(unittest.TestCase):
    
    def test_divisibleby7_1(self):
        result = Divisibleby7(14)
        self.assertTrue(result)
        
    def test_divisibleby7_2(self):
        result = Divisibleby7(4)
        self.assertFalse(result)

if __name__ == "__name__":
    unittest.main()