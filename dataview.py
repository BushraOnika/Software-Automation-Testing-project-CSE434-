from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
driver = webdriver.Chrome()

url = "http://182.163.99.86/login"
user = "bushrahossainonika@gmail.com"
p = "1234Aa@"

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

data= wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/aside/div/div/div/div[4]/a/div')))
data.click()
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)

p1=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section/div[2]/div/table/tbody/tr[1]/td[5]/div/a')))
time.sleep(2)
p1.click()
time.sleep(2)

data.click()
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)
p2=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section/div[2]/div/table/tbody/tr[2]/td[5]/div/a')))
time.sleep(2)
p2.click()
time.sleep(2)


wait.until(EC.url_contains("http://182.163.99.86/data/8"))
data.click()
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)
p3=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section/div[2]/div/table/tbody/tr[3]/td[5]/div/a')))
time.sleep(2)
p3.click()
time.sleep(2)

wait.until(EC.url_contains("http://182.163.99.86/data/4"))
data.click()
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)
p4=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section/div[2]/div/table/tbody/tr[4]/td[5]/div/a')))
time.sleep(2)
p4.click()
time.sleep(2)

data.click()
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)
p5=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section/div[2]/div/table/tbody/tr[5]/td[5]/div/a')))
time.sleep(2)
p5.click()
time.sleep(2)

data.click()
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)
p6=wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section/div[2]/div/table/tbody/tr[6]/td[5]/div/a')))
time.sleep(2)
p6.click()
time.sleep(2)
wait.until(EC.url_contains("http://182.163.99.86/data"))
time.sleep(2)
driver.quit()