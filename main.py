from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys
from datetime import date

#shemomyavs library
curryear = date.today().year

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
driver.get("https://accounts.google.com/signup/v2/webcreateaccount?flowName=GlifWebSignIn&flowEntry=SignUp")

#driver initializing
print("sheiyvanet nomeri")
realphonenumber  = input()
name = driver.find_element_by_name("firstName")
surname = driver.find_element_by_name("lastName")
print("axla saxeli da gvari")
accname = input()
accsurname = input()
name.send_keys(accname)
surname.send_keys(accsurname)
mail = driver.find_element_by_id("username")
mail.send_keys(f"{accname}{accsurname}{curryear}")
password = driver.find_element_by_name("Passwd")
password.send_keys("Tbilisi123")
confpassword = driver.find_element_by_name("ConfirmPasswd")
confpassword.send_keys("Tbilisi123")
confpassword.send_keys(Keys.RETURN)
driver.implicitly_wait(3)
phonenum = driver.find_element_by_id("phoneNumberId")
phonenum.send_keys(realphonenumber + Keys.RETURN)
codeinput = driver.find_element_by_id("code")
codeinput.send_keys(input() + Keys.RETURN)
driver.implicitly_wait(1)
driver.find_element_by_id("phoneNumberId").send_keys(Keys.CONTROL + "a" + Keys.BACKSPACE)
birthday = driver.find_element_by_name("day")
birthday.send_keys("1")
birthmonth = driver.find_element_by_xpath("//*[@id='month']/option[2]")
birthmonth.click()
birthyear = driver.find_element_by_name("year")
birthyear.send_keys("2000")
sex = driver.find_element_by_xpath("//*[@id='gender']/option[4]")
sex.click()
driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button/span").click()
driver.implicitly_wait(1)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
driver.find_element_by_xpath("//*[@id='view_container']/div/div/div[2]/div/div[2]/div/div[1]/div/div/button").click()
driver.implicitly_wait(1)
