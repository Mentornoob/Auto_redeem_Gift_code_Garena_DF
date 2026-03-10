import random
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pickle
import time
import json

# thêm thư viện popup
from tkinter import Tk
from tkinter.filedialog import askopenfilename


# hàm chọn file
def choose_file(title, filetype):
    root = Tk()
    root.withdraw()
    return askopenfilename(title=title, filetypes=filetype)


# popup chọn cookie
cookie_file = choose_file("Chọn file cookies", [("JSON", "*.json")])

# popup chọn file code
code_file = choose_file("Chọn file gift code", [("Text file", "*.txt")])


driver = webdriver.Chrome()

# mở đúng domain trước
driver.get("https://redeem.df.garena.sg")

time.sleep(2)

# đọc file cookie
with open(cookie_file, "r", encoding="utf-8") as f:
    data = json.load(f)

cookies = data["cookies"]

# thêm cookie vào selenium
for c in cookies:
    cookie = {
        "name": c["name"],
        "value": c["value"],
        "domain": c["domain"],
        "path": c["path"],
    }

    driver.add_cookie(cookie)

# reload trang
driver.refresh()
print("Login bằng cookie thành công")

# đọc file code
with open(code_file, "r", encoding="utf-8") as f:
    codes = [line.strip() for line in f if line.strip()]

for code in codes:

    print("Redeem:", code)

    input_box = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/input"))
    )

    input_box.clear()
    input_box.send_keys(code)

    # đóng popup nếu có
    try:
        close_button = WebDriverWait(driver, 0.5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/a"))
        )
        close_button.click()
    except:
        pass

    redeem_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[2]/a"))
    )

    redeem_button.click()

    time.sleep(0.1)

print("Hoàn thành")
