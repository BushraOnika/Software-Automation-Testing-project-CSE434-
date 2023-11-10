from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.support.ui import Select
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
login_button = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/form/button')))
login_button.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/dashboard"))
time.sleep(2)
vali = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[2]/div/button')))
vali.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/users?page=1&user_role=4"))


add = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/button')))
add.click()
time.sleep(5)

nam = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r2o:"]')))
nam.click()
time.sleep(2)
nam.send_keys('Bushra Hossain Onika')
time.sleep(2)


e = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r2t:"]')))

time.sleep(500)
e.click()
e.send_keys("onikabushrahossain@gmail.com")
time.sleep(2)
g = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r32:"]')

gender = Select(g)

gender.select_by_visible_text("Female")
time.sleep(1)

inst = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r2q:"]')))
inst.click()
inst.send_keys("North South University")
time.sleep(2)



qua = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r2v:"]')))
qua.click()
qua.send_keys("BSC")
time.sleep(2)


mob = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r39:"]')))
mob.click()
mob.send_keys("01977503085")
time.sleep(2)

p = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="floating-label-input-:r34:"]')))
p.click()
p.send_keys("Aa00##")
time.sleep(2)


time.sleep(1)
roled = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r35:"]')

role = Select(roled)

role.select_by_visible_text("Guest")
time.sleep(15)

submit = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[3]/button')))
submit.click()
time.sleep(800)

