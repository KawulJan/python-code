import time

from selenium import webdriver

driver =webdriver.Chrome(executable_path="C:\webdriver\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get("https://www.expedia.com/")
driver.find_element_by_link_text("Flights").click()

driver.find_element_by_id("uitk-field-label").send_keys("SFO")
#driver.find_element_by_id("uitk-field-label").send_keys("NYC")



time.sleep(2)


