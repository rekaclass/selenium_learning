from selenium import webdriver
#from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\projects\learning\drivers\chromedriver.exe")
driver.get("http://billbooks.co.in/demo/bills/index.php")

userName = driver.find_element_by_name("uname").send_keys("admin")
password = driver.find_element_by_name("pass").send_keys("admin")
enterkey = driver.find_element_by_xpath("//*[@id='sign_in']/div[3]/button").click()

#click two man icon
twoman = driver.find_element_by_id("navbarDropdownMenuLink").click()

#click add a manager
driver.find_element_by_link_text("group_add Add New Manager").click()

#create new manager
