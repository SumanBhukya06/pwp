from playwright.sync_api import Page,expect
def test_assignment(page:Page):
    page.goto("https://demowebshop.tricentis.com/")
    #page visible
    title=page.get_by_alt_text("Tricentis Demo Web Shop")
    expect(title).to_be_visible()

    #find computers
    computer_count=page.locator("h2>a[href*='computer']")
    print("The computers count is: ",computer_count.count())
    expect(computer_count).to_have_count(computer_count.count())

    #first product
    print("First product: ",computer_count.first.text_content())
    #last product
    print("Last product:",computer_count.last.text_content())
    #nth product
    print("Nth product: ",computer_count.nth(2).text_content())

    #print all products
    pro_titles=computer_count.all_text_contents()
    # print(pro_titles)

    for i in pro_titles:
        print(i)


