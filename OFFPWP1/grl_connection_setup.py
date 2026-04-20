from playwright.sync_api import Page,expect

def test_grl_connection_panel(page:Page):
    #launch application
    page.goto(("http://localhost:3003/v423111.html"))

#validation
    #Connection Type = Ethernet visible
    connection_type=page.get_by_text("Ethernet")
    expect(connection_type).to_be_visible()
    conn_type=connection_type.text_content()
    if conn_type=="Ethernet":
        print("Yes")
    else:
        print("No")
    page.wait_for_timeout(2000)

    #Scan Network button visible
    scan_button=page.locator("button#connectionsetup_AutoDiscoverIP_button")
    expect(scan_button).to_be_visible()
    print("Scan Network:",scan_button.text_content())

    #IP Address field present
    ip_address=page.locator("//div[normalize-space()='GRL-WP-TPR-C3']")
    expect(ip_address).to_be_visible()
    print("Tp address: ",ip_address.text_content())

    #Connect button present
    connect_button=page.locator("#connectionsetup_connect_button")
    expect(connect_button).to_be_visible()
    print("Connect Button: ",connect_button.text_content())

    #Update Firmware button present
    firmware_button=page.locator("button#connectionsetup_update_firmware_button")
    expect(firmware_button).to_be_visible()
    print("Firmware button: ",firmware_button.text_content())


def test_Scan_Network_Functionality(page:Page):
    page.goto(("http://localhost:3003/v423111.html"))
    # Click Scan Network
    scan_button=page.locator("button#connectionsetup_AutoDiscoverIP_button")
    scan_button.click()

    #page.locator(".loader").wait_for(state="hidden")
    #expect(page.get_by_text("192.168.255.1")).to_be_visible()

def test_Connect_with_Valid_IP(page:Page):
    page.goto("http://localhost:3003/v423111.html")
    #Enter/select IP → 192.168.255.1
    connect_ip=page.locator("input[value='192.168.255.1']")
    connect_ip.clear()
    #connect_ip.select_option("div[id='4fed0bae-e97a-4af3-8794-d61e5b4a0c4b']")
    page.wait_for_timeout(3000)
    #Click Connect
    clk_button=page.locator("#connectionsetup_connect_button")
    clk_button.click()

    page.wait_for_timeout(5000)

def test_licenses(page:Page):
    page.goto("http://localhost:3003/v423111.html")
    bpp=page.locator("//div[contains(text(),'1.3 BPP')]")

    licen=page.get_by_text("//body[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/div[1]")
    expect(licen).to_be_visible()
    expect(bpp).to_be_visible()
    page.wait_for_timeout(3000)







