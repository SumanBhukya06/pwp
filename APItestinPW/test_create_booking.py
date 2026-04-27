#data:hard coded date inside the test
import json

from playwright.sync_api import Playwright,expect
#from urllib import response
def test_create_booking(playwright:Playwright):
    base_url="https://restful-booker.herokuapp.com"
    #to create request
    request_context=playwright.request.new_context()
    file=open("testData/post_request_body.json","r")
    request_body=json.load(file)
    response=request_context.post(f"{base_url}/booking",data=request_body)

    #validation
    #expect(response_body).to_be_ok()
    assert response.ok
    assert response.status==200
    response_body = response.json()
    print("Response body: ",response_body)
    assert "bookingid" in response_body
    assert "booking" in response_body

    #data validation
    booking=response_body["booking"]
    assert booking["firstname"]=="Joy"
    assert booking["lastname"] == "Maya"
    assert booking["totalprice"] == 1500
    assert booking["depositpaid"] is True
    assert booking["additionalneeds"] == "super bowls"
    #nested json data
    assert booking["bookingdates"]["checkin"] == "2018-01-01"
    assert booking["bookingdates"]["checkout"] == "2019-01-01"

    #dispose
    request_context.dispose()




