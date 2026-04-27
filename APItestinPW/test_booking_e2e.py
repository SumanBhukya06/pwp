
import json

import pytest
from playwright.sync_api import Playwright


#base url
base_url="https://restful-booker.herokuapp.com"

#utility function-reading json file
def read_json(file_path):
    file=open(file_path,"r")
    return json.load(file)


#fixture- create playwright request context
@pytest.fixture(scope="session")
def request_context(playwright:Playwright):
    context=playwright.request.new_context()
    yield context
    context.dispose()
#1 create booking(post)--booking id
def test_create_booking(request_context):
    data=read_json("testData/post_request_body.json")
    response=request_context.post(f"{base_url}/booking",data=data)
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print("Create booking response: ",response_body)
    assert ("bookingid" in response_body)
    assert ("booking" in response_body)
    booking=response_body["booking"]
    assert booking["firstname"] == data["firstname"]
    assert booking["lastname"] == data["lastname"]
    assert booking["totalprice"] == data["totalprice"]
    assert booking["depositpaid"] is data["depositpaid"]
    assert booking["bookingdates"]["checkin"] == data["bookingdates"]["checkin"]
    assert booking["bookingdates"]["checkout"] == data["bookingdates"]["checkout"]

    global  booking_id
    booking_id=response_body["bookingid"]

#2. get booking details(GET)- By id, By name, By Dates
def test_get_booking_by_id(request_context):
    response=request_context.get(f"{base_url}/booking/{booking_id}")
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print(f"Booking details fetched by id: {booking_id}",response_body)
    assert "firstname" in response_body
    assert "lastname" in response_body


def test_get_booking_by_name(request_context):
    names_params={"firstname":"Jim","lastname":"Brown"}
    #passing query parameter
    response=request_context.get(f"{base_url}/booking",params=names_params)
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print(f"Booking ID's fetched by Names: {names_params}",response_body)
    assert len(response_body)>0
    for item in response_body:
        assert "bookingid" in item

def test_get_booking_by_dates(request_context):
    dates_params={"checkin":"2025-12-15","lastname":"2025-12-20"}
    #passing query parameter
    response=request_context.get(f"{base_url}/booking",params=dates_params)
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print(f"Booking ID's fetched by Names: {dates_params}",response_body)

    for item in response_body:
        assert "bookingid" in item
 #3.token generation(POST/auth)
def test_create_token(request_context):
    data=read_json("testData/token_request_body.json")
    response=request_context.post(f"{base_url}/auth",data=data)
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print(response_body)
    assert "token" in response_body
    global token
    token=response_body["token"]
    assert len(token)>5
#4. partial update booking(PATCH)
def test_partial_update_booking(request_context):

    data=read_json("testData/put_request_body.json")
    response=request_context.patch(f"{base_url}/booking/{booking_id}",data=data,
                          headers={"Cookie":f"token={token}"})
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print("Partial update response for booking id {booking_id}",response_body)
    for key in data.keys():
        assert key in response_body
        assert response_body[key]==data[key]
#Full update Booking (PUT)
def test_full_update_booking(request_context):

    data=read_json("testData/put_request_body.json")
    response=request_context.patch(f"{base_url}/booking/{booking_id}",data=data,
                          headers={"Cookie":f"token={token}"})
    assert response.ok
    assert response.status==200
    response_body=response.json()
    print("Partial update response for booking id {booking_id}",response_body)
    # for key in data.keys():
    #     assert key in response_body
    #     assert response_body[key]==data[key]
    assert response_body["firstname"] == data["firstname"]
    assert response_body["lastname"] == data["lastname"]
    assert response_body["totalprice"]==data["totalprice"]

def test_delete_booking(request_context):
    response=request_context.delete(f"{base_url}/booking/{booking_id}",headers={"Cookie":f"token={token}"})
    assert response.status == 201
    print("booking deleted successfully..",booking_id)













