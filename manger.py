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
manager = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[5]/div/button')))
manager.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/users?page=1&user_role=2"))

delete=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[1]/td[8]/div/span[3]/img')))
delete.click()
time.sleep(2)
no=wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[2]')))
no.click()
time.sleep(2)

view=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[3]/div[2]/div/table/tbody/tr[2]/td[8]/div/span[2]/a/img')))
view.click()
time.sleep(5)
driver.quit()



driver.quit()