import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

driver = None 

def parse_range(range_str, total_found):
    indices = []
    parts = range_str.replace(" ", "").split(",")
    
    for part in parts:
        try:
            if "-" in part:
                start, end = map(int, part.split("-"))
                indices.extend(range(start - 1, end))
            else:
                indices.append(int(part) - 1)
        except ValueError:
            continue
    
    return [i for i in indices if 0 <= i < total_found]

def init_driver():
    global driver
    if driver is None:
        options = Options()
        options.add_argument("--headless=new")
        options.add_argument("--disable-gpu")
        options.add_argument("--window-size=1920,1080")

        driver = webdriver.Chrome(options=options)
        driver.get('https://www.instagram.com')
    return driver

def login_instagram(username, password):
    driver = init_driver()

    user_input = driver.find_element(By.NAME, "email")
    pass_input = driver.find_element(By.NAME, "pass")

    user_input.send_keys(username)
    pass_input.send_keys(password)

    login    = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Log In']")
    login.click()
    time.sleep(5)

    try:
        not_now  = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//div[@role='button' and text()='Not now']")))
        not_now.click()
    except:
        pass

    try:
        not_now2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='_a9-- _ap36 _a9_1' and text()='Not Now']")))
        not_now2.click()
    except:
        pass

def scrape_comment(target_username, range_mode = "all", custom_range="", maxscroll = 30):
    driver = init_driver()

    BASE_URL = 'https://www.instagram.com/'
    driver.get(f'{BASE_URL}{target_username}')

    time.sleep(10)

    url_postingan_list = []
    scroll_times = 0
    last_height  = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.XPATH, "//a[contains(@href, '/p/')]")
                )
            )
        except:
            pass

        posts = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")

        print("Jumlah post terbaca:", len(posts))  

        for post in posts:
            url = post.get_attribute("href")
            if url:
                url_postingan_list.append(url)

        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height or scroll_times == maxscroll:
            break

        last_height   = new_height
        scroll_times += 1

    url_postingan_list = list(dict.fromkeys(url_postingan_list))

    selected_url = []
    if range_mode == 'all':
        selected_url = url_postingan_list
    else:
        valid_indices = parse_range(custom_range, len(url_postingan_list))
        for idx in valid_indices:
            if idx < len(url_postingan_list):
                selected_url.append(url_postingan_list[idx])

    jml_all_post  = len(url_postingan_list)
    selected_post = len(selected_url)

    print(f"Jumlah semua postingan: {jml_all_post}")
    print(f"Jumlah postingan yang dipilih: {selected_post}")

    comments = []
    times    = []
    for u in selected_url:
        
        driver.get(u)
        time.sleep(3)

        while True:
            tombol_reply = driver.find_elements(
                By.XPATH,
                '//span[contains(text(),"View all") and contains(text(),"repl")]')

            if len(tombol_reply) == 0:
                break

            for tombol in tombol_reply:
                try:
                    driver.execute_script("arguments[0].click();", tombol)
                    time.sleep(1)
                except:
                    pass

        komentar_elemen = driver.find_elements(
            By.XPATH,
            '//div[@class="x78zum5 xdt5ytf x1iyjqo2"]'
            '//div[@class="html-div xdj266r x14z9mp xat24cr x1lziwak xexx8yu xyri2b x18d9i69 x1c1uobl x9f619 xjbqb8w x78zum5 x15mokao x1ga7v0g x16uus16 xbiv7yw x1uhb9sk x1plvlek xryxfnj x1c4vz4f x2lah0s xdt5ytf xqjyukv x1cy8zhl x1oa3qoh x1nhvcw1"]'
            '//span[@class="x1lliihq x1plvlek xryxfnj x1n2onr6 xyejjpt x15dsfln x193iq5w xeuugli x1fj9vlw x13faqbe x1vvkbs x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x x1i0vuye xvs91rp xo1l8bm x5n08af"]'
        )

        waktu_komentar  = driver.find_elements(By.TAG_NAME, "time")

        for komentar in komentar_elemen:
            text = komentar.text
            if text:
                comments.append(text)

        temp_times = []
        for waktu in waktu_komentar:
            val_waktu = waktu.get_attribute('title')
            if val_waktu:
                temp_times.append(val_waktu)

        if len(temp_times) > 2:
            times.extend(temp_times[1:-1])
        elif len(temp_times) == 2:
            pass

    print(len(times))
    print(len(comments))
    return comments, times, jml_all_post, selected_post

