import pytest


@pytest.mark.run(order='2')
def test_run_order_methodA(setUp, OneTimeSetUp):
    print('Running method A')


@pytest.mark.run(order='1')
def test_run_order_methodB(setUp, OneTimeSetUp):
    print('Running method B')


@pytest.mark.run(order='5')
def test_run_order_methodC(setUp, OneTimeSetUp):
    print('Running method C')


@pytest.mark.run(order='4')
def test_run_order_methodD(setUp, OneTimeSetUp):
    print('Running method D')


@pytest.mark.run(order='3')
def test_run_order_methodF(setUp, OneTimeSetUp):
    print('Running method F')
