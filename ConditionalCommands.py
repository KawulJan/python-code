from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")
driver.get("http://cubecart.unitedcoderschool.com/ecommerce/admin_w4vqap.php?_g=customers&node=email")
username=driver.find_element_by_name("username")
print(username.is_displayed())
print(username.is_enabled())

username.send_keys("testautomation")

driver.find_element_by_name("password").send_keys("automation123!")
driver.find_element_by_name("login").click()

driver.find_element_by_id('nav_products').click()
driver.find_element_by_link_text("Add Product").click()
driver.find_element_by_link_text("Categories").click()

roundtrip_radio = driver.find_element_by_css_selector("input[name=primary_cat]")
print("atatus of round trip radio button", roundtrip_radio.is_selected())
