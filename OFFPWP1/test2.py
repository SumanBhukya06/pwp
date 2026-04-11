from playwright.sync_api import Page,expect
def test_verify_orange(page:Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.wait_for_timeout(5000)
    expect(page).to_have_title("OrangeHRM")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    #page.wait_for_timeout(5000)
    # text=page.get_by_text("Dashboard")
    # page.wait_for_timeout(4000)
    # expect(text).to_have_text("Dashboard")
    expect(page.get_by_role("heading", name="Dashboard")).to_be_visible()

