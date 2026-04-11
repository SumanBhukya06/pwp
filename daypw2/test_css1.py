from playwright.sync_api import Page,expect
def test_verify_css(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #tag id we can remove tag name also
    tag_id=page.locator("input#small-searchterms")
    tag_id.fill("T-shirts")
    tag_id.clear()
    page.wait_for_timeout(1000)
#tag class
    tag_class=page.locator("input.search-box-text")
    tag_class.fill("shirts")
    tag_class.clear()
    page.wait_for_timeout(1000)
#tag any other attribute
    tag_any=page.locator("input[name=q]")
    tag_any.fill("Jeans")
    tag_any.clear()
    page.wait_for_timeout(2000)
#tag class attribute
    tag_class_1=page.locator("input.search-box-text[value='Search store']")
    tag_class_1.fill("Shorts")
    page.wait_for_timeout(2000)

