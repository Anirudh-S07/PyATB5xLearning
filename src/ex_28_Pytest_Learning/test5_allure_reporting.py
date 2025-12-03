import pytest
import allure
from allure_commons.types import LinkType


# To use allure install allure using pip install allure-pytest
# whilst execution use --alluredir=allure_results
# also you need to install allure command line for this there should be pre-installed node.js
# npm -g i allure-commandline
# Then at last we should run allure serve allure_results
# if it won't work use npx --yes allure-commandline serve allure_results
# also you can customize the report
# You can give Title, description, tag, severity, label, links, issue, testcase all these are given decorators


@allure.title("To validate that 5 and 6 are equal")
@allure.description("This test case was a test to know the fundamentals of allure test case and pytest fundamentals")
@allure.tag("Positive Failure")
@allure.label("owner", " Anirudh")
@allure.label("Creator", "Anirudh")
@allure.severity(allure.severity_level.CRITICAL)
@allure.testcase("TMS-456")
@allure.link("http://google.com", link_type=LinkType.LINK, name="Google")
@allure.issue("Auth-123")
@pytest.mark.positive
def test_method1():
    print("testcase 1")
    assert 5 == 6


@allure.title("To validate Negative")
@allure.description("This test case was a test to know the fundamentals of allure test case and pytest fundamentals")
@allure.tag("Negative Pass")
@pytest.mark.negative
def test_method2():
    print("Test 2")
    assert 1 + 1 == 2


@pytest.mark.negative
def test_method3_negative():
    print("Test 3")
    assert 1 + 1 == 2
