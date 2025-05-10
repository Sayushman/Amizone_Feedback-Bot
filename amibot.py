from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# taking input for login_id & password
login_id=input("Enter your log_id here: ")
password=input("Enter your password here: ")

# ser_obj=Service("/home/aayu/Documents/PROJECTS/amiz_feed/chromedriver-linux64 (1)/chromedriver-linux64/")
ser_obj=Service("/home/aayu/Documents/PROJECTS/amiz_feed/chromedriver-linux64 (3)/chromedriver-linux64/chromedriver")
driver=webdriver.Chrome(service=ser_obj)

driver.maximize_window()

driver.implicitly_wait(5)

driver.get("https://s.amizone.net/")

driver.find_element(By.XPATH,'//*[@id="loginform"]/div[1]/input[1]').send_keys(login_id)
driver.find_element(By.XPATH,'//*[@id="loginform"]/div[2]/input').send_keys(password)
driver.find_element(By.XPATH,'//*[@id="loginform"]/div[4]/button').click()

driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//*[@id="ModalPopAppAyf"]/div/div/div[1]/button').click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,'//*[@id="M27"]').click()

# driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//*[@id="Div_Partial"]/div/div/div[2]/div[2]/div/ul/li/div[3]/div[2]/div/div/div/div[2]/div/div/div[2]/a').click()

driver.implicitly_wait(5)

# driver.find_element(By.XPATH,'//*[@id="1"]').click()

driver.implicitly_wait(5)

# 1st
for i in range(1, 5):
    xpath= f'//*[@id="no-more-tables"]/table/tbody/tr[{i}]/td[5]/label/span'
    driver.find_element(By.XPATH, xpath).click()
# driver.find_element(By.XPATH,'//*[@id="no-more-tables"]/table/tbody/tr[1]/td[5]/label/span').click()
# driver.find_element(By.XPATH,'//*[@id="no-more-tables"]/table/tbody/tr[2]/td[5]/label/span').click()
# driver.find_element(By.XPATH,'//*[@id="no-more-tables"]/table/tbody/tr[3]/td[5]/label/span').click()

driver.implicitly_wait(5)

# 2nd
for i in range(1, 8):
    xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[{i}]/td[5]/label/span'
    driver.find_element(By.XPATH, xpath).click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[1]/td[5]/label/span').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[2]/td[5]/label/span').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[3]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[4]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[5]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[6]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[2]/div[2]/div/div/table/tbody/tr[7]/td[5]/label').click()

driver.implicitly_wait(5)

# # 3rd
for i in range(1, 7):
    xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr[{i}]/td[5]/label/span'
    driver.find_element(By.XPATH, xpath).click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr[1]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr[2]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr[3]/td[5]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[3]/div[2]/div/div/table/tbody/tr[4]/td[5]/label').click()

driver.implicitly_wait(5)

# # 4th
for i in range(1, 5):
    # xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[4]/div[2]/div/div/table/tbody/tr[{i}]/td[5]/label'
    xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[4]/div[2]/div/div/table/tbody/tr[{i}]/td[5]/label/span'
    driver.find_element(By.XPATH, xpath).click()

driver.implicitly_wait(5)

# # 5th
for i in range(1, 5):
    # xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[5]/div[2]/div/div/table/tbody/tr[{i}]/td[5]/label'
    xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[5]/div[2]/div/div/table/tbody/tr[{i}]/td[5]/label/span'
    driver.find_element(By.XPATH, xpath).click()


driver.implicitly_wait(5)

for i in range(1, 4):
    xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[{i}]/td[3]/label/span'
    # xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[1]/td[3]/label'
    driver.find_element(By.XPATH, xpath).click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[1]/td[3]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[2]/td[3]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[3]/td[3]/label').click()
# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[4]/td[3]/label').click()

xpath= f'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[6]/table/tbody/tr[4]/td[2]/textarea'
driver.find_element(By.XPATH, xpath).send_keys("......")


driver.implicitly_wait(5)

# driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[7]/input').click()
driver.find_element(By.XPATH,'/html/body/div[3]/div/div[2]/div[2]/div[2]/form/div/div/div[7]/input').click()

driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//*[@id="navbar-container"]/div[3]/ul/li[5]/a/i').click()

driver.implicitly_wait(5)

driver.find_element(By.XPATH,'//*[@id="navbar-container"]/div[3]/ul/li[5]/ul/li[3]/a').click()


time.sleep(2)
print("Thanks: Your Feedback is filled by a #robot")
driver.close