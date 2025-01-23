from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

import time
from datetime import datetime

# QUANTITY = 12
ORDER_TIME = datetime(2024, 5, 4, 19, 56)

service = Service(executable_path="D:\Hobbies\click-bot\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://member.lazada.co.th/user/login?spm=a2o4m.home-th.header.d5.11257f6diIaJsp")

driver \
    .find_element  (
        By.CSS_SELECTOR, 
        "input[type='text'][data-meta='Field']"
    ) \
    .send_keys("0922782349")

driver \
    .find_element  (
        By.CSS_SELECTOR, 
        "input[type='password'][data-meta='Field']"
    ) \
    .send_keys("Lazada_137587")

time.sleep((ORDER_TIME - datetime.now()).total_seconds())

print(f"Before Redirection: {datetime.now()}")

driver.get("https://www.lazada.co.th/products/gege-bear-gege-bear-glossy-lip-glaze-lasting-moist-dudu-lip-pure-white-mirror-lipstick-i4954638252-s20826193059.html?dsource=share&laz_share_info=995414343_100_100_100043979789_995414343_null&laz_token=3f749a02e84368af77dde882d6bb6d38&exlaz=e_iqeJxmuQOjPGip8qo24MCSTeQCjDld4siVQ4kY1ODqrCXvTKdNAtBb55%2BgIiSkmNnXkPoNuoMIIpR8IEI%2FLi1U0sC6tUOx2TD3WnASIas1Y%3D&sub_aff_id=social_share&sub_id2=995414343&sub_id3=100043979789&sub_id6=CPI_EXLAZ")

# add_button = driver.find_element(By.CSS_SELECTOR, ".next-number-picker-handler-up-inner")

# for i in range(QUANTITY - 1):
#     add_button.click()

print(f"Redirection: {datetime.now()}")

driver \
    .find_element(
        By.CSS_SELECTOR,
        "input[step='1'][type='text'][autocomplete='off']"
    ) \
    .send_keys("2")

print(f"Select Quantity: {datetime.now()}")

driver \
    .find_element(
        By.CSS_SELECTOR, 
        ".add-to-cart-buy-now-btn.pdp-button_theme_yellow"
    ) \
    .click()

print(f"Checkout: {datetime.now()}")

time.sleep(1000)

driver.quit()