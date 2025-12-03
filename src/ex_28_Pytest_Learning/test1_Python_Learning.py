# Not a Pytest test case
def method1():
    print("hello World")


def test_method1():
    print("I am a pytest test case")
    assert 5 == 5
