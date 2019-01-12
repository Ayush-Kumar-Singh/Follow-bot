from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
chromedriver ="/Users/Lenovo/Downloads/chromedriver"
browser = webdriver.Chrome(chromedriver)

browser.get('https://www.twitter.com')

a = browser.find_element_by_xpath('//input[@autocomplete="username"]')
a.click()
a.send_keys('Your Email')
sleep(2)
b = browser.find_element_by_xpath('//input[@type="password"]')
b.click()
b.send_keys('Your Password')
sleep(2)
c = browser.find_element_by_xpath('//input[@value="Log in"]')
c.click()
sleep(2)

d = browser.find_element_by_xpath('//a[text()="View all"]')
d.click()

sleep(2)
body_elem = browser.find_element_by_tag_name('body')
for _ in range(3):
	body_elem.send_keys(Keys.END)
	sleep(1)
	body_elem.send_keys(Keys.HOME)
	sleep(1)
sleep(1)
f = browser.find_element_by_xpath('//div[@class="user-actions btn-group not-following not-muting  "]/span/button[@type="button"]/span[text()="Follow"]')

count = 0
while (count < 30):
	f.click()
	sleep(3)
	f = browser.find_element_by_xpath('//div[@class="user-actions btn-group not-following not-muting  "]/span/button[@type="button"]/span[text()="Follow"]')
