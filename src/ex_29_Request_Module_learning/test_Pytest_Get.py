import allure
import pytest
import requests


@allure.title("Verify the GET Request of Restful Booker")
@allure.description("This testcase checks for the booking id 2 and verify the response")
@pytest.mark.positive
def test_get_request_positive():
    url = "https://restful-booker.herokuapp.com/booking/2"
    response_data = requests.get(url)
    print(response_data.text)
    assert (response_data.status_code == 200)


@allure.title("Verify the GET Request of Restful Booker with -1 as id")
@allure.description("This testcase checks for the booking id -1 and verify the response")
@pytest.mark.negative
def test_get_request_negative_id():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    print(response_data.text)
    assert response_data.status_code == 404



