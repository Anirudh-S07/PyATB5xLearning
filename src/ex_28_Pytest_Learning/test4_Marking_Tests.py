import pytest


# Not a Pytest test case
def method1():
    print("hello World")


def test_method1():
    print("I am a pytest test case")
    assert 5 == 6


@pytest.mark.smoke
def test_method2():
    print("Test 2")
    assert 1 + 1 == 2

# To run basic html report first install pytest-HTM by pip install pytest-html then while running
# pytest --html=report.html --self-contained-html
