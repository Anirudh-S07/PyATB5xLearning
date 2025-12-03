# Not a Pytest test case
def method1():
    print("hello World")


def test_method1():
    print("I am a pytest test case")
    assert 5 == 6


def test_method2():
    print("Test 2")
    assert 1 + 1 == 2

# To run multiple test cases from a single file then you should use command pytest and copy the content root path of the
# file and press enter in the terminal
