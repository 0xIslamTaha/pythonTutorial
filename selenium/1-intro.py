from selenium import webdriver
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome()
driver.get('http://google.com')
search = driver.find_element_by_name('q')
search.send_keys('hamda')
search.send_keys(Keys.RETURN)
item = driver.find_element_by_name('btnk')
item.click()
