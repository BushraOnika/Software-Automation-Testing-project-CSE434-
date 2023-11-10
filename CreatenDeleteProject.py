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
project = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button')))
project.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/dashboard/projects"))
Pcreate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[1]/button')))
Pcreate.click()
time.sleep(2)
n=driver.find_element(By.XPATH,'//*[@id="name"]')
n.click()
n.send_keys("Bush' Oni's timeline ")
d=driver.find_element(By.XPATH,'//*[@id="description"]')
d.click()

d.send_keys("Bush's workingg playground project for kids")
time.sleep(1)
annot=driver.find_element(By.XPATH,'//*[@id="1"]')
annot.click()
time.sleep(2)
tag=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[4]/button/div')
tag.click()
s=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button')
s.click()
time.sleep(10)
wait.until(EC.url_contains("http://182.163.99.86/dashboard/projects"))
delete = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[2]/div[2]/div/table/tbody/tr[1]/td[9]/div/span[3]/img')))
delete.click()
time.sleep(1)
yes=driver.find_element(By.XPATH,'/html/body/div[3]/div/div/div[3]/button[1]')
time.sleep(1)
yes.click()
wait.until(EC.url_contains("http://182.163.99.86/dashboard/projects"))
time.sleep(5)

driver.quit()
