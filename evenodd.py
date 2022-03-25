import unittest

def EvenorOdd(x):
    if x%2 == 0:
        return "even"
    else:
        return "odd"

class myeoapp(unittest.TestCase):

    def test_case_evenorodd(self):
        result = EvenorOdd(2)
        self.assertEqual("even", result)

    def test_case_evenorodd1(self):
        result = EvenorOdd(15)
        self.assertEqual("odd", result)



if __name__ == "__main__":
    unittest.main()