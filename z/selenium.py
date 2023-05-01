from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Users\\nazeer\\OneDrive\\Desktop\\Web-Drivers\\chromedriver_win32.zip\\chromedriver.exe")
driver.get("http://www.google.com/")
print(driver.title)   ## Title of the page
driver.close()    ## close the browser