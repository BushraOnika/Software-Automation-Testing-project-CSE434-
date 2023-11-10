from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import string

# Initialize the Chrome WebDriver
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

num_projects_to_create = 5

for _ in range(num_projects_to_create):
    project = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div/div[1]/div[1]/div/button')))
    project.click()
    time.sleep(2)
    wait.until(EC.url_contains("http://182.163.99.86/dashboard/projects"))
    project_name = ''.join(random.choices(string.ascii_letters, k=10))
    project_description = ''.join(random.choices(string.ascii_letters, k=20))

    Pcreate = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="root"]/section/main/div[2]/div[2]/section/div[1]/button')))
    Pcreate.click()
    time.sleep(2)
    n = driver.find_element(By.XPATH, '//*[@id="name"]')
    n.click()
    n.send_keys(project_name)
    d = driver.find_element(By.XPATH, '//*[@id="description"]')
    d.click()
    d.send_keys(project_description)
    time.sleep(1)
    annot = driver.find_element(By.XPATH, '//*[@id="1"]')
    annot.click()
    time.sleep(2)
    tag = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[2]/div/div/section[1]/div[2]/div/div/div/div[4]/button/div')
    tag.click()
    s = driver.find_element(By.XPATH, '/html/body/div[3]/div/div/div[3]/button')
    s.click()
    time.sleep(2)
    driver.get("http://182.163.99.86/dashboard")  # Go back to the dashboard

# Close the browser when done
driver.quit()
