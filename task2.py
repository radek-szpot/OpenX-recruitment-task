import requests
from requests.structures import CaseInsensitiveDict
import json
import os


def auth():
    url = "https://restful-booker.herokuapp.com/auth"
    headers_ = CaseInsensitiveDict()
    headers_["Content-Type"] = "application/json"
    data_ = """
    {
        "username" : "admin",
        "password" : "password123"
    }
    """
    token = requests.post(url, headers=headers_, data=data_)
    return token


def get(url):
    response = requests.get(url)
    json_response = json.loads(response.text)
    return json_response, response


def post(url):
    headers_ = CaseInsensitiveDict()
    headers_["Content-Type"] = "application/json"
    data_ = """
    {
        "firstname" : "Test_name",
        "lastname" : "Test_lastname",
        "totalprice" : 120,
        "depositpaid" : true,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    """
    response = requests.post(url, headers=headers_, data=data_)
    return response


def put(url):
    headers_ = CaseInsensitiveDict()
    headers_["Content-Type"] = "application/json"
    headers_["Accept"] = "application/json"
    headers_["Cookie"] = "token=" + str(json.loads(auth().text)["token"])

    data_ = """
    {
        "firstname" : "Test_name_UPDATED",
        "lastname" : "Test_lastname_UPDATED",
        "totalprice" : 120,
        "depositpaid" : true,
        "bookingdates" : {
            "checkin" : "2018-01-01",
            "checkout" : "2019-01-01"
        },
        "additionalneeds" : "Breakfast"
    }
    """

    response = requests.put(url, headers=headers_, data=data_)
    return response


def delete(url):
    headers_ = CaseInsensitiveDict()
    headers_["Content-Type"] = "application/json"
    headers_["Cookie"] = "token=" + str(json.loads(auth().text)["token"])

    response = requests.delete(url, headers=headers_)
    return response
