from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

driver =webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.get("http://cubecart.unitedcoderschool.com/ecommerce/admin_w4vqap.php?_g=customers&node=email")

driver.implicitly_wait(10)

assert "welcom:Admin Control Panel" in driver.title

driver.find_element_by_name("username").send_keys("testautomation")
driver.find_element_by_name("password").send_keys("automation123!")

driver.find_element_by_name("login").click()
