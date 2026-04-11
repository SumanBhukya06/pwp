from playwright.sync_api import  Page,expect
from pygments.lexers import go


def test_css_loc(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    # loc=page.locator("#small-searchterms")
    # loc.fill("Jeans")
    # page.locator("input[type=submit]").click()
    #expect(page.get_by_text("Blue Jeans")).to_be_visible()
    page.wait_for_timeout(4000)
    page.locator(".block-category-navigation").get_by_role("link", name="Books").click()
