from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time



driver = webdriver.Firefox()



link="https://accounts.google.com/ServiceLogin/signinchooser?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
mail_ele=".whsOnd.zHQkBf"
next_ele="identifierNext"
pass_ele=".whsOnd.zHQkBf"
login=".ZFr60d.CeoRYc"




def login_mail(mail_id,passwd):
         driver.get(link)
         emailid=driver.find_element_by_css_selector(mail_ele)
         emailid.send_keys(mail_id)
         driver.find_element_by_id(next_ele).click()
         time.sleep(3)
         keywd=driver.find_element_by_css_selector(pass_ele)
         keywd.send_keys(passwd)
         driver.find_element_by_css_selector(login).click()
         return



mail_id="enter your mail id here"
passwd="enter your password here"

login_mail(mail_id,passwd)


