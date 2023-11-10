from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome()

url = "http://182.163.99.86/login"
user = "admin@gigatech.com"
p = "Abc@123"

driver.get(url)
driver.maximize_window()
wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))

username_input.send_keys(user)
password_input.send_keys(p)
login_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/button')))
login_button.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/dashboard"))
time.sleep(2)
vali = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[2]/div/button')))
vali.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/users?page=1&user_role=4"))
view = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div/span[2]/a/img')))
view.click()
time.sleep(2)

g = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="left-tabs-example-tab-second"]')))
g.click()
time.sleep(5)

v2= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="left-tabs-example-tabpane-second"]/section/div/div/div[2]/div/table/tbody/tr/td[7]/a')))
v2.click()
time.sleep(5)

export = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[2]')))
export.click()
time.sleep(2)

e = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button')))
e.click()
time.sleep(2)

assign_data = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]')))
assign_data.click()
time.sleep(2)




data_num = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section/div/input')))
data_num.click()
time.sleep(2)


