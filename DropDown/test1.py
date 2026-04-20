from playwright.sync_api import Page,expect
def test_dropdown_assignment(page:Page):
    page.goto("https://www.bstackdemo.com/")
    #Order by dropdown visible or not
    order_by=page.locator("div.sort>select")
    expect(order_by).to_be_visible() #visible
    expect(order_by).to_be_enabled() #enable

#sort the products [select lowest to highest option]
    order_by.select_option(label="Lowest to highest")
    page.wait_for_timeout(4000)

# Get all product price and name elements
    price_element=page.locator("div.val")
    name_elements=page.locator("p.shelf-item__title")

    all_prices=price_element.all_text_contents()
    all_names=name_elements.all_text_contents()
    # print("All prices:",all_prices)
    # print(("All elements name: ",all_names))

    # Print product names and prices
    for i in range (len(all_names)):
        print(f"{all_names[i]}: {all_prices[i]}")

# Print lowest and highest priced products
    print(f"Lowest Priced Product: {all_names[0]} : {all_prices[0]}")
    print(f"Highest Priced Product: {all_names[-1]} : {all_prices[-1]}")
