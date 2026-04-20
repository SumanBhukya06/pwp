from playwright.sync_api import Page,expect
def test_gui_elements(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
#Name
    page.locator("#name").fill("Joy")

#Phone
    page.locator("#phone").fill("1234567890")
#Email
    page.locator(("#email")).fill("abc@gmail.com")
#Address
    page.locator("//textarea[@id='textarea']").fill("I am from so and so and came here to take an advice from you...")

#Radio
    gender_visible=page.locator("label[for='gender']")
    expect(gender_visible).to_be_visible()

#Select male radio button
    page.locator("#male").click()

#Select Female radio button
    page.locator("#female").click()


#Days
    days_visi=page.locator("label[for='days']")
    expect(days_visi).to_be_visible()

#All days
    all_days = page.locator("//div[@class='form-group'][4]//label")

    count = all_days.count()

    for i in range(count):
        day = all_days.nth(i).inner_text()
        page.get_by_label(day).check()
    # print(all_names.all_text_contents())
    #ite=all_names.all_text_contents()
    #
    #
    #for i in ite:
        #print(i)

 #check days checkbox
    # page.locator("#sunday").click()
    #
    # days = ["Sunday", "Monday", "Wednesday"]
    #
    # for day in days:
    #     page.get_by_label(day).check()






