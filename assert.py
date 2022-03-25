import unittest

class mydata(unittest.TestCase):

    def test_case3(self):
        self.assertEqual("hello","hello")

class Myapp(unittest.TestCase):

    def test_case1(self):
        self.assertNotEqual("helloworld","hello")

    def test_case2(self):
        a=10
        b=10
        c= a+b
        self.assertEqual(c,a+b)

if __name__ == "__main__":
    unittest.main()