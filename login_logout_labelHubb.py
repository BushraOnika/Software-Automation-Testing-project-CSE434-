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

wait = WebDriverWait(driver, 10)
username_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="username"]')))
password_input = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="password"]')))

username_input.send_keys(user)
password_input.send_keys(p)
time.sleep(2)
login_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/button')))
login_button.click()

wait.until(EC.url_contains("http://182.163.99.86/dashboard"))

admin_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="radix-:r5:"]')))
admin_button.click()

time.sleep(2)
logout_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="radix-:r6:"]/div')))
logout_button.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/login"))
time.sleep(2)
driver.quit()
