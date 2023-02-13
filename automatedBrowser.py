#this program automatically logins to a web page passing
#the login authentication test

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

#Portal credentials
userID = ""
password = ""

#initialize the chrome driver
driver = webdriver.Chrome("chromedriver.exe")

#head to TUM campascura
driver.get("https://eregistrar.tum.ac.ke/Campuscura/?TenantID=tum#login;TenantID=tum;Apply=false")

#find registration Number and send the reg no to the input field
driver.find_element("id", "gwt-uid-31").send_keys(userID)

#find password input field and insert password
driver.find_element("id", "gwt-uid-32").send_keys(password)

#click login button
driver.find_element("button","button").click()

driver.close()