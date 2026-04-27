from playwright.sync_api import Playwright

def test_headers_response(playwright:Playwright):
    request_context=playwright.request.new_context()
    response=request_context.get("https://www.google.com")

    assert response.status_text=="OK"
    assert response.status==200

    #Extract all the headers
    headers=response.headers
    for key,value in headers.items():
        #print(key,value)
        print(f"{key}==>{value}")

#validate specific headers
    print(headers.get("content-type"))
    assert "text/html" in headers.get("content-type")
    assert "gzip"== headers.get("content-encoding")

    #validate specific presence
    assert "server" in headers
    assert "set-cookie" in headers




