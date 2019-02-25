import unittest

class TestCaseDemo1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("*#" *30)
        print("I will run only once before all tests")
        print("*#" * 30)

    def setUp(self):
        print("I will run once before every tests")

    def test_MethodA(self):
        print("Running method A")

    def test_MethodB(self):
        print("Running method B")

    def tearDown(self):
        print("I will run once after every tests")

    @classmethod
    def tearDownClass(cls):
        print("*#" * 30)
        print("I will run only once after all tests")
        print("*#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)