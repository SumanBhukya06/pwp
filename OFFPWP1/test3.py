from playwright.sync_api import Page,expect
def test_verify_orange(page:Page):
    page.goto("http://localhost:3003/v423111.html")
    #expect(page.get_by_text("2.1 BPP")).to_be_visible()
    #expect(page.locator("div.color-box:has-text('2.1 BPP')")).to_be_visible()
    page.locator("div.color-box", has_text="2.1 BPP")
