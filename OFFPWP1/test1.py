from playwright.sync_api import Page,expect
def test_verify_url(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(5000)
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_verify_title(page:Page):
     page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
     expect(page).to_have_title("OrangeHRM")
    #expect(page).to_have_title("OrangeHRM")
