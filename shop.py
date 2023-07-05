
# Shop: отображение страницы товара

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login_email = driver.find_element_by_css_selector("#username")
# login_email.send_keys("email@email.ru")
# login_password = driver.find_element_by_css_selector("#password")
# login_password.send_keys("Proverka12")
# login_bth = driver.find_element_by_css_selector("[value='Login']")
# login_bth.click()
# shop_bth = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_bth.click()
# html5_book = driver.find_element_by_css_selector("[title='Mastering HTML5 Forms']")
# html5_book.click()
# title_element = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "[itemprop='name']"), "HTML5 Forms"))
# driver.quit()

# Shop: количество товаров в категории

# import time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login_email = driver.find_element_by_css_selector("#username")
# login_email.send_keys("email@email.ru")
# login_password = driver.find_element_by_css_selector("#password")
# login_password.send_keys("Proverka12")
# login_bth = driver.find_element_by_css_selector("[value='Login']")
# login_bth.click()
# shop_bth = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_bth.click()
# html_bth = driver.find_element_by_css_selector("li.cat-item.cat-item-19 > a")
# html_bth.click()
# items_count = driver.find_elements_by_class_name("product")
# if len(items_count) == 3:
#     print("Отображается три товара")
# else:
#     print("Ошибка. Количество товаров на странице не равно 3: " + str(len(items_count)))
# driver.quit()

# Shop: сортировка товаров

# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login_email = driver.find_element_by_css_selector("#username")
# login_email.send_keys("email@email.ru")
# login_password = driver.find_element_by_css_selector("#password")
# login_password.send_keys("Proverka12")
# login_bth = driver.find_element_by_css_selector("[value='Login']")
# login_bth.click()
# shop_bth = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_bth.click()
# sorting_selector = driver.find_element_by_class_name("orderby").click()
# default_sorting = driver.find_element_by_css_selector("[value='menu_order']")
# sorting_selected = default_sorting.get_attribute("selected")
# if sorting_selected is not None:
#     print("sorting default")
# else:
#     print("sorting is not default")
# sorting_selector = Select(driver.find_element_by_class_name("orderby"))
# sorting_selector.select_by_value("price-desc")
# time.sleep(3)
# sorting_selector = driver.find_element_by_class_name("orderby").click()
# sorting_high_to_low = driver.find_element_by_css_selector("[value='price-desc']")
# sort_select = sorting_high_to_low.text
# assert sort_select == "Sort by price: high to low"
# driver.quit()

# Shop: отображение, скидка товара

# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# my_account = driver.find_element_by_css_selector("#menu-item-50 > a")
# my_account.click()
# login_email = driver.find_element_by_css_selector("#username")
# login_email.send_keys("email@email.ru")
# login_password = driver.find_element_by_css_selector("#password")
# login_password.send_keys("Proverka12")
# login_bth = driver.find_element_by_css_selector("[value='Login']")
# login_bth.click()
# shop_bth = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_bth.click()
# android_book = driver.find_element_by_css_selector("[title='Android Quick Start Guide']")
# android_book.click()
# last_price = driver.find_element_by_css_selector("div:nth-child(2) > p > del > span")
# last_price_get_text = last_price.text
# assert last_price_get_text == "₹600.00"
# new_price = driver.find_element_by_css_selector("div:nth-child(2) > p > ins > span")
# new_price_get_text = new_price.text
# assert new_price_get_text == "₹450.00"
# img_android_book = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#product-169 > div.images > a > img"))).click()
# pp_close_bth = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "pp_close"))).click()
# driver.quit()

# Shop: проверка цены в корзине

# import time
# from selenium.webdriver.support.select import Select
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# shop_bth = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop_bth.click()
# html5_book_basket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
# html5_book_basket.click()
# time.sleep(2)
# item_basket = driver.find_element_by_class_name("cartcontents")
# item_text = item_basket.text
# assert item_text == "1 Item"
# time.sleep(2)
# price_book = driver.find_element_by_css_selector("#wpmenucartli > a > span.amount")
# price_text = price_book.text
# assert price_text == "₹180.00"
# time.sleep(2)
# item_basket = driver.find_element_by_id("wpmenucartli")
# item_basket.click()
# subtotal_price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.cart-subtotal > td > span")))
# total_price = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "tr.order-total > td > strong > span")))
# driver.quit()

# Shop: работа в корзине

# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
# driver.get("https://practice.automationtesting.in/")
# time.sleep(3)
#
# shop = driver.find_element_by_css_selector("#menu-item-40 > a")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5_book_basket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
# html5_book_basket.click()
# time.sleep(3)
# js_data_book_basket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=180']")
# js_data_book_basket.click()
# time.sleep(3)
# basket = driver.find_element_by_css_selector("#wpmenucartli > a > span.cartcontents")
# basket.click()
# time.sleep(5)
# remove = driver.find_element_by_css_selector("td.product-remove > a")
# remove.click()
# time.sleep(3)
# undo = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > div.woocommerce-message > a")
# undo.click()
# time.sleep(3)
# quantity_js_book = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
# quantity_js_book.clear()
# time.sleep(3)
# quantity_js_book = driver.find_element_by_css_selector("tr:nth-child(1) > td.product-quantity > div > input")
# quantity_js_book.send_keys(3)
# update_basket = driver.find_element_by_css_selector("tr:nth-child(3) > td > input.button")
# update_basket.click()
# time.sleep(3)
# element = driver.find_element_by_css_selector("[inputmode=numeric]")
# element_check = element.get_attribute("value")
# assert element_check == "3"
# time.sleep(3)
# apply_coupon_bt = driver.find_element_by_css_selector("tr:nth-child(3) > td > div > input.button")
# apply_coupon_bt.click()
# time.sleep(3)
# element = driver.find_element_by_css_selector("#page-34 > div > div.woocommerce > ul > li")
# element_get_text = element.text
# assert element_get_text == "Please enter a coupon code."
# driver.quit()

# Shop: покупка товара

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()  # позволяет открывать бразуер в полном окне, рекомендуется к дальнейшему использованию
driver.get("https://practice.automationtesting.in/")
time.sleep(3)
shop = driver.find_element_by_css_selector("#menu-item-40 > a")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(2)
html5_book_basket = driver.find_element_by_css_selector("[href='/shop/?add-to-cart=182']")
html5_book_basket.click()
time.sleep(2)
basket = driver.find_element_by_id("wpmenucartli")
basket.click()
time.sleep(3)
proceed_to_checkout = WebDriverWait(driver, 20).until(
EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="checkout-button button alt wc-forward"]'))).click()
time.sleep(3)
first_name = WebDriverWait(driver, 10).until(
EC.element_to_be_clickable((By.ID, "billing_first_name")))
first_name.send_keys("Name")
time.sleep(3)
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("Lastname")
time.sleep(3)
email = driver.find_element_by_id("billing_email")
email.send_keys("email@email.ru")
time.sleep(3)
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("8888888888")
time.sleep(3)
country_select = driver.find_element_by_id("s2id_billing_country")
country_select.click()
country = driver.find_element_by_css_selector("#select2-drop>div>input")
country.send_keys("Zimbabwe")
time.sleep(3)
country_opt = driver.find_element_by_css_selector("[class='select2-results-dept-0 select2-result select2-result-selectable select2-highlighted']")
country_opt.click()
time.sleep(3)
addres = driver.find_element_by_id("billing_address_1")
addres.send_keys("Zimbabwe street")
time.sleep(3)
town_city = driver.find_element_by_id("billing_city")
town_city.send_keys("Harare")
time.sleep(3)
state = driver.find_element_by_id("billing_state")
state.send_keys("Afrika")
time.sleep(3)
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(3)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
place_order_btn = driver.find_element_by_id("place_order")
place_order_btn.click()
time.sleep(2)
thank_you = WebDriverWait(driver, 10).until(
EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_payments_text = WebDriverWait(driver, 20).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tr:nth-child(3) > td"), "Check Payments"))
driver.quit()





