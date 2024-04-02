
"""
Created By *Abdullah EL-Yamany*
-------------------------------
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
import time, urllib.request


driver = webdriver.Chrome()
driver.get("https://www.instagram.com/")

time.sleep(2)

# -------- Login ------- #
while True:
    try:
        username = driver.find_element(By.CSS_SELECTOR, 'input[name="username"]')
        password = driver.find_element(By.CSS_SELECTOR, 'input[name="password"]')
        break
    except:
        time.sleep(3)

username.clear()
password.clear()
username.send_keys("xxxxxxxxxxx") # Write Email or Phone
password.send_keys("xxxxxxxxxxx") # Write Password

time.sleep(1)
login = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

#save your login info?
while True:
    time.sleep(5)
    try:
        notnow = driver.find_element(By.XPATH, '//div[@class="_ac8f"]/div[@role="button"]').click()
        break
    except:
        continue


#turn on notif
time.sleep(2)
notnow2 = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]").click()

# post
post_link = "https://www.instagram.com/p/xxxxxxxxxxxxxxxxxxxxxxxx" # Write Link Of Post


#get videos and images
download_url = ''

driver.get(post_link)
shortcode = driver.current_url.split('/')[-2]
time.sleep(5)

main_div = driver.find_element(By.CSS_SELECTOR, 'div[class="x6s0dn4 x1dqoszc xu3j5b3 xm81vs4 x78zum5 x1iyjqo2 x1tjbqro"]')

imgs_link = []

while True:
    imgs = main_div.find_elements(By.CSS_SELECTOR, "img[style='object-fit: cover;']")
    for img in imgs:
        if img.get_attribute('src') not in imgs_link:
            imgs_link.append(img.get_attribute('src'))
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next"]').click()
        time.sleep(5)
    except:
        break


num = 1
time.sleep(3)
for link in imgs_link:
    urllib.request.urlretrieve(link, f'img_{num}{shortcode}.jpg')
    num += 1
    time.sleep(6)

