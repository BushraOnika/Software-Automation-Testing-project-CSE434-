from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

import pyautogui

driver = webdriver.Firefox()

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
project = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button')))
project.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/dashboard/projects"))

view = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[1]/td[9]/div/span[1]/a/img')))
view.click()
time.sleep(2)

upload = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[1]/div/div[2]/button[1]')))
upload.click()
time.sleep(2)

n= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="1"]')))
n.click()
time.sleep(2)
# Click the "Browse" button
browse = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section/div[2]/div/span')))
browse.click()

# Type the file path and press Enter
file_path = 'C:\\upload_data_sample.xlsx'  # Adjust the file path as needed
pyautogui.write(file_path)
pyautogui.press('enter')

time.sleep(5)

submit=browse = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button')))
submit.click()

time.sleep(5)

driver.quit()