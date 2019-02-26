import pytest
from pytestPackage.class_to_test import SomeClassToTest

@pytest.mark.usefixtures("setUp", "OneTimeSetUp")
class TestClassDemo():

    @pytest.fixture(autouse = True)
    def classSetup(self):
        self.abc = SomeClassToTest(10)

    def test_methodA(self):
        result = self.abc.sumNumber(2, 8)
        assert result == 20
        print("running A")


    def test_methodB(self):
        print("running B")