from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
 
driver = webdriver.Firefox()
driver.get("https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin") 
#find element id by inspect
emailid=driver.find_element_by_id("identifierId")
emailid.send_keys("write mail id here")
 

#find element id by inspect
driver.find_element_by_id("identifierNext").click()
 
time.sleep(2)
 

#find element class by inspect if it have space use css selector
keywd=driver.find_element_by_css_selector(".whsOnd.zHQkBf")
keywd.send_keys("write password here")
 
 
#find element class name by inspect if it have space use css selector 
driver.find_element_by_css_selector(".ZFr60d.CeoRYc").click()

