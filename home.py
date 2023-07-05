
## Home: добавление комментария

import time
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
selenium_ruby_book = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 > div > ul > li > a.woocommerce-LoopProduct-link > h3")
selenium_ruby_book.click()
reviews_bth = driver.find_element_by_css_selector("li.reviews_tab > a")
reviews_bth.click()
star_five = driver.find_element_by_css_selector("a.star-5")
star_five.click()
your_review = driver.find_element_by_css_selector("#comment")
your_review.send_keys("Nice book!")
name = driver.find_element_by_css_selector("#author")
name.send_keys("Name")
email = driver.find_element_by_css_selector("#email")
email.send_keys("email@email.com")
submit_bth = driver.find_element_by_css_selector("#submit")
submit_bth.click()
driver.quit()