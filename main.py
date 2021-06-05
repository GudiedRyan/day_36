from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time

pw = os.environ["yesmantwitterpass"]

chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# Get a wikipedia Search

driver.get("https://en.wikipedia.org/wiki/Main_Page")

driver.find_element_by_link_text("Random article").click()

time.sleep(1)

headline_text = driver.find_element_by_id("firstHeading").text

split_text = headline_text.split(" ")

url_end = "_".join(split_text)

driver.quit()

wiki_url = f"https://en.wikipedia.org/wiki/{url_end}"

#Twitter portion
chrome_driver_path = "D:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://twitter.com/login")

user = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
user.send_keys("yesmanvong@gmail.com")

password = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')
password.send_keys(pw)

password.send_keys(Keys.ENTER)

#Create a tweet

tweet_box = driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div')
tweet_box.send_keys(wiki_url)
driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span').click()

time.sleep(2)

driver.quit()