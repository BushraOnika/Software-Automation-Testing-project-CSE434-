

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

con= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[5]/a')))
con.click()
wait.until(EC.url_contains("http://182.163.99.86/configuration"))
time.sleep(2)
cat= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[1]/input')))
cat.click()
cat.send_keys("BUSH")
time.sleep(2)

tag=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[2]/input')))
tag.click()
time.sleep(1)
tag.send_keys("Bush")

short=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[3]/input')))
short.click()
time.sleep(1)
short.send_keys("Bush")

d=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[2]/div/div[1]/div[4]/textarea')))
d.click()
time.sleep(1)
d.send_keys("DO Bush things")

add_button=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[2]/div/div[2]/button')))
add_button.click()
time.sleep(5)

delete =wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[3]/div/div/span[10]/button')))

delete.click()

time.sleep(2)

yes=wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button[1]')))
yes.click()
time.sleep(2)
driver.quit()