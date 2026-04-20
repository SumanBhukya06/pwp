from playwright.sync_api import Page,expect
def test_built(page:Page):
    page.goto("https://www.demoblaze.com/")
    #print(page.get_by_title(title))
    # title=page.get_by_alt_text("STORE")
    # print(title.get_attribute("title"))
    page.locator("a#signin2").click()#sign up
    #page.wait_for_timeout(3000)

    user_name=page.locator("input#sign-username")
    name="Joy007"
    user_name.fill(name)
    password=page.locator("input#sign-password")
    pwd="joy123"
    password.fill(pwd)

    page.locator("button[onclick='register()']").click()
    page.on("dialog", lambda dialog: dialog.accept())#handle alert
    page.wait_for_timeout(2000)
def test_login(page:Page):
    page.goto("https://www.demoblaze.com/")
    #click on login
    page.locator("a#login2").click()
    page.locator("input#loginusername").fill("Joy007")
    page.locator("input#loginpassword").fill("joy123")
    page.locator("button[onclick='logIn()']").click()

    text=page.locator("a#nameofuser")
    expect(text).to_be_visible()
    page.wait_for_timeout(3000)
    #itles = page.locator("h4.card-title").all_inner_texts()
    titles = page.locator("h4.card-title")
    # for t in titles:
    #     print(t)

    #prices=page.locator("div.card-block>h5").all_inner_texts()
    #prices = page.locator("div.card-block>h5")
    # for p in prices:
    #     print(p)

    #using nth(i)
    count=titles.count()
    for i in range(count):
        t=titles.nth(i).inner_text()
        #p=prices.nth(i).inner_text()
        #print(f"{t},{p}")
        print(t)
        if t=="Samsung galaxy s6":
            titles.nth(i).click()
        break
        # using zip()
        # for t,p in zip(titles,prices):
        #     print(f"{t},{p}")
     #add to cart
    page.locator("a[onclick='addToCart(1)']").click()
    page.on("dialog", lambda dialog: dialog.accept())  # handle alert
    page.locator("a#cartur").click()
    page.locator("button[data-target='#orderModal']").click()
    page.wait_for_timeout(5000)

    #place order
    page.locator("input#name").fill("Joy")
    page.locator("input#country").fill("USA")
    page.locator("input#city").fill("Toronto")
    page.locator("input#card").fill("123456789")
    page.locator("input#month").fill("Jun")
    page.locator("input#year").fill("2026")
    page.locator("button[onclick='purchaseOrder()']").click()
    #verify purchase text
    purchase_text=page.locator("//h2[normalize-space()='Thank you for your purchase!']")
    expect(purchase_text).to_be_visible()
    #purchase ok
    page.locator(".confirm.btn.btn-lg.btn-primary").click()
    #page logo
    page_logo=page.locator("a#nava")
    expect(page_logo).to_be_visible()







