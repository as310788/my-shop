# Registration_login: регистрация аккаунта
import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()
register_email = driver.find_element_by_css_selector("#reg_email")
register_email.send_keys("email@email.ru")
reg_password = driver.find_element_by_css_selector("#reg_password")
reg_password.send_keys("Proverka12")
register_bth = driver.find_element_by_css_selector("[value='Register']")
register_bth.click()
driver.quit()

# Registration_login: логин в систему
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
my_account.click()
login_email = driver.find_element_by_css_selector("#username")
login_email.send_keys("email@email.ru")
login_password = driver.find_element_by_css_selector("#password")
login_password.send_keys("Proverka12")
login_bth = driver.find_element_by_css_selector("[value='Login']")
login_bth.click()
logout_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.LINK_TEXT, 'Logout'), "Logout"))
driver.quit()
