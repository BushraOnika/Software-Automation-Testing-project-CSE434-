from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select  # Import the Select class
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

url = "http://182.163.99.86/login"
user = "admin@gigatech.com"
p = "Abc@123"

driver.get(url)
time.sleep(2)

wait = WebDriverWait(driver, 10)
signup = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/p/a')))
signup.click()
wait.until(EC.url_contains("http://182.163.99.86/signup"))
time.sleep(1)

n = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r0:"]')
n.click()
n.send_keys("Bushra Hossain")

email = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r5:"]')
email.click()
email.send_keys("Bushra")
time.sleep(1)
roled = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r1:"]')

role = Select(roled)

role.select_by_visible_text("Annotator")

g = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r6:"]')

gender = Select(g)

gender.select_by_visible_text("Female")
time.sleep(1)
mobile = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r2:"]')
mobile.click
mobile.send_keys("01977503085")

qua = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r3:"]')
qua.click
qua.send_keys("BSC CSE")

institute = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r8:"]')
institute.click
institute.send_keys("North South University")

p= driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r4:"]')
p.click
p.send_keys("120Aa")
p2 = driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r9:"]')
p2.click
p2.send_keys("120Aa")
see=driver.find_element(By.XPATH, '//*[@id="root"]/div/section[1]/div/div/div[2]/section[2]/div[5]/div/div[2]/button/img')
see.click()
time.sleep(2)
bday= driver.find_element(By.XPATH, '//*[@id="floating-label-input-:r7:"]')

bday.click()
bday.send_keys("06/05/2000")

submit= driver.find_element(By.XPATH, '//*[@id="root"]/div/section[1]/div/div/div[3]/button')
submit.click()

time.sleep(5)

driver.quit()