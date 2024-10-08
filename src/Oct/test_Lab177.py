# Create Booking Testcase
# Verify that booking is not null
# status code, Headers...

# Request Module - requests

import pytest # pip install pytest
import allure # pip install allure-pytest
import requests

@allure.title("Test GET Request - RestFUL BOOKER Project#1")
@allure.description("TC#1 -> Verify that GET Request with ID works")
@allure.tag("regression", "p0", "smoke")
@allure.label("owner", "Pramod Dutta")
@allure.testcase("TC#1")
@pytest.mark.smoke
def test_get_single_request_by_id_positive():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    print(response_data.text)
    print(response_data.json())
    print(response_data.headers)
    assert response_data.status_code == 200


@allure.title("Test GET Request - RestFUL BOOKER Project#2")
@allure.description("TC#2 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negaitve():
    url = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url)
    assert response_data.status_code == 404

@allure.title("Test GET Request - RestFUL BOOKER Project#3")
@allure.description("TC#3 -> Verify that GET Request with invalid bookingID")
@pytest.mark.smoke
def test_get_single_request_by_id_negative():
    url = "https://restful-booker.herokuapp.com/booking/invalid"
    responseData  = requests.get(url)
    print(responseData.text)
    assert responseData.status_code == 404