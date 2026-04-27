from playwright.sync_api import Playwright

def test_cookie_in_response(playwright:Playwright):
    request_context=playwright.request.new_context()
    response=request_context.get("https://www.google.com")

    assert response.status_text=="OK"
    assert response.status==200
    #extract all the cookies from the presence
    cookies=request_context.storage_state()["cookies"]
    for c in cookies:
        print(f"{c['name']}==>{c['value']}==>{c['domain']}")

    #check if 'AEC' cookie is exist
    aec_cookie=None
    for c in cookies:
        if c["name"]=="AEC":
            aec_cookie=c
            break
    #Fail
    #assert aec_cookie is not None, "cookie 'AEC' not found"
    assert aec_cookie is not None, "cookie 'AEC' not found"
    #printing details of 'AEC' cookie
    print(aec_cookie['name'])
    print(aec_cookie['value'])
    print(aec_cookie['domain'])
    print(aec_cookie['path'])
    print(aec_cookie['expires'])



