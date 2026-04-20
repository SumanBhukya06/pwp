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
    titles = page.locator("h4.card-title").all_inner_texts()
    #titles = page.locator("h4.card-title")
    # for t in titles:
    #     print(t)

    prices=page.locator("div.card-block>h5").all_inner_texts()
    #prices = page.locator("div.card-block>h5")
    # for p in prices:
    #     print(p)

    #using nth(i)
    # count=titles.count()
    # for i in range(count):
    #     t=titles.nth(i).inner_text()
    #     p=prices.nth(i).inner_text()
    #     print(f"{t},{p}")

    #using zip()
    for t,p in zip(titles,prices):
        print(f"{t},{p}")




