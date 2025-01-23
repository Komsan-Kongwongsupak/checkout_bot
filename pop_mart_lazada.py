from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
from datetime import datetime

ORDER_TIME = datetime(2024, 5, 4, 23, 59, 59, 999000)
# ORDER_TIME = datetime(2024, 5, 4, 23, 48, 59, 999000)

def get_element(driver, input):
    return driver.find_element(By.CSS_SELECTOR, input)

service = Service(executable_path="D:\Hobbies\click-bot\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://member.lazada.co.th/user/login?spm=a2o4m.home-th.header.d5.11257f6diIaJsp")
time.sleep((ORDER_TIME - datetime.now()).total_seconds())

# print(f"Before Redirection: {datetime.now()}")
driver.get("https://www.lazada.co.th/products/restock-on-44-0000-am-local-timepop-mart-the-monsters-exciting-vinyl-face-blind-box-action-figures-i4924072141-s20729168260.html?dsource=share&laz_share_info=955346119_100_100_100019094477_955346119_null&laz_token=7f044f2270ec0b3dbcbfcc2d119acb94&dsource=share&laz_share_info=955342639_1_9300_100019094477_955342639_copy-linktool-campaign-default&laz_token=2c4d171a9f0c7d475b2fa9d46c2aff97&dsource=share&laz_share_info=988235748_1_9300_100205907756_988235748_copy-linktool-campaign-default&laz_token=824f34da9a31176a81e7c813bc38a117&trafficFrom=17449020_303586&laz_trackid=2:mm_287851169_159152655_2115952654:clkgk2dlf1ht21g8901c5f&mkttid=clkgk2dlf1ht21g8901c5f")
# print(f"Redirection: {datetime.now()}")
# get_element(driver, "input[step='1'][type='text'][autocomplete='off']").send_keys("2")
# time.sleep(3)
# print(f"Select Quantity: {datetime.now()}")
# get_element(driver, ".add-to-cart-buy-now-btn.pdp-button_theme_yellow").click()
# print(f"Checkout: {datetime.now()}")
time.sleep(1000)

driver.quit()