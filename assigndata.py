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
group = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/section[4]/div/div/div[1]/button')))
group.click()
time.sleep(2)
nam = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[1]/input')))
nam.click()
nam.send_keys("Bhoo")
time.sleep(2)

a=wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/button')))
a.click()
time.sleep(2)

d = Select(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[1]/button'))))
d.select_by_visible_text("Validator")
time.sleep(5)

a=wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[2]/div[2]/div/table/tbody/tr[1]/td[1]/div/div/button')))
a.click()
time.sleep(2)

ano = Select(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/button'))))
ano.select_by_visible_text("Ner")

driver.quit()


dropdown = Select(wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/button/svg'))))
dropdown.select_by_visible_text("Ner")

time.sleep(2)
driver.quit()
