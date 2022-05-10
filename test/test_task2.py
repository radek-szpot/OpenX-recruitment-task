from task2 import auth, get, post, put, delete
import json
import pytest

# global variable POSTED_ID will be id of created in POST testcase -> test_post_booking()
# it will be used to UPDATE and DELETE testcases
global POSTED_ID


def test_token_creation():
    # test case checks:
    # if response to create auth token were 200 (OK)
    token = auth()
    assert token.status_code == 200


def test_get_booking_ids():
    # test case checks:
    # if response to get booking ids were 200 (OK)
    json_, response = get("https://restful-booker.herokuapp.com/booking")
    assert response.status_code == 200


def test_post_booking():
    # test case checks if request was posted. Test by asserting response status code
    response = post("https://restful-booker.herokuapp.com/booking")
    assert response.status_code == 200
    # get posted data id
    response_json = json.loads(response.text)
    global POSTED_ID
    POSTED_ID = response_json["bookingid"]


def test_put_booking():
    # test case checks if posted data was updated. Test by asserting response status code
    response = put(f"https://restful-booker.herokuapp.com/booking/{POSTED_ID}")
    assert response.status_code == 200


def test_delete_booking():
    # test case checks if posted data gets deleted. Test by asserting response status code
    response = delete(f"https://restful-booker.herokuapp.com/booking/{POSTED_ID}")
    assert response.status_code == 201


# # I had to comment out this test because this base is being modified continually
# # but here is example how I would test contents of specific id
# def test_get_booking_id_1():
#     # test case checks:
#     # if response to get booking id 1 were 200 (OK)
#     # is response 100% compatible with example from
#     # https://restful-booker.herokuapp.com/apidoc/index.html#api-Booking-GetBooking
#     json_, response = get("https://restful-booker.herokuapp.com/booking/1")
#     assert response.status_code == 200
#     assert json_["firstname"] == "Sally"
#     assert json_["lastname"] == "Brown"
#     assert json_["totalprice"] == 111
#     assert json_["depositpaid"] is True
#     assert json_["bookingdates"]["checkin"] == "2013-02-23"
#     assert json_["bookingdates"]["checkout"] == "2014-10-23"
#     assert json_["additionalneeds"] == "Breakfast"
