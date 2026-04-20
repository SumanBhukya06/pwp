from playwright.sync_api import Page,expect
def test_dummy_blaze(page:Page):
    page.goto("https://blazedemo.com/")
    page.wait_for_timeout(2000)
    #welcome text
    wel_text=page.locator("div[class='container'] h1")
    print("welcome text is: ",wel_text.text_content())
    #source city
    page.locator("select[name='fromPort']").select_option("Mexico City")
    #page.wait_for_timeout(2000)
    #destination city
    page.locator("select[name='toPort']").select_option("Dublin")

    #Find flights
    page.locator("input[value='Find Flights']").click()
    #page.wait_for_timeout(1000)

    #After clicking on find flights
    to_from_text=page.locator("div[class='container'] h3")
    print("To from text is: ",to_from_text.text_content())

    # 5. Count number of rows (flights) in the table
    rows = page.locator("table.table tbody tr")
    row_count = rows.count()
    print("Number of flight rows:", row_count)#5

    # 6. Capture all prices into a list
    prices = []
    for i in range(row_count):
        price_text = rows.nth(i).locator("td").nth(5).inner_text()  # 6th column
        prices.append(price_text)

    print("Flight Prices:", prices)

    # 7. Sort the prices (string sort)
    sorted_prices = sorted(prices)
    lowest_price = sorted_prices[0]
    print("Lowest Price:", lowest_price)  # Printing lowest price

    # 8. Find row with lowest price and click "Choose This Flight"
    for i in range(row_count):
        price_text = rows.nth(i).locator("td").nth(5).inner_text()
        if price_text == lowest_price:
            rows.nth(i).locator('td input[type="submit"]').click()
            break
    #page.wait_for_timeout(3000)
    # 9. Fill passenger details on the purchase page
    page.locator("#inputName").fill("Joy")
    page.locator("#address").fill("123 Hyd")
    page.locator("#city").fill("BLR")
    page.locator("#state").fill("KA")
    page.locator("#zipCode").fill("54231")
    page.locator("#cardType").select_option("American Express")
    page.locator("#creditCardNumber").fill("512345456789")
    page.locator("#creditCardMonth").fill("10")
    page.locator("#creditCardYear").fill("2024")
    page.locator("#nameOnCard").fill("Joy k")

    # Click on Purchase Flight
    page.locator("input[value='Purchase Flight']").click()

    # # 10. Validate success message
    page.locator("div[class='container hero-unit'] h1")

    page.wait_for_timeout(3000)