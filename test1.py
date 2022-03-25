import unittest

def add(x,y):
    return x+y

class myapp(unittest.TestCase):

    def test_case_add(self):
        a=10
        b=5
        c= add(a,b)
        self.assertEqual(c,a+b)

    def test_case_add2(self):
        a=10.90
        b=5.7
        c=add(a,b)
        self.assertEqual(a+b,c)

    def test_case_add3(self):
        a= -10
        b=-20
        c= add(a,b)
        self.assertEqual(c,a+b)

if __name__ == "__main__":
    unittest.main()