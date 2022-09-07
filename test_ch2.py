from selenium import webdriver
import chromedriver
from selenium.webdriver.common.by import By


def test_google_search():
    driver = webdriver.chrome
    driver.get("")
    #1. go to google.com
    driver.get('https://www.google.com')
     #2.type in a search 'pupies'
    var = driver.find_element(By.NAME, "q").send_keys
    #3.submit on enter the search
     #4.assent we got a search page for puppies


