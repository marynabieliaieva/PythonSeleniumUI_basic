import unittest
from UnitTestDemo.TestCaseDemo import TestCaseDemo
from UnitTestDemo.TestCaseDemo1 import TestCaseDemo1


# get all tests from TestClass1 and TestClass2
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestCaseDemo1)


# create a test suite combining TestClass 1 and TestClass2
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)