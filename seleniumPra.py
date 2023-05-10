from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("incognito")

#Login in Facebook with Selenium
driver = webdriver.Chrome(options = options)
driver.get("https://zh-tw.facebook.com/")
result1 = driver.find_element(By.NAME, "email")
result1.send_keys("sundial.chiu@gmail.com")
result2 = driver.find_element(By.NAME, "pass")
result2.send_keys("123456")
result3 = driver.find_element(By.NAME, "login")
result3.submit()
time.sleep(5)

#三立新聞粉絲頁
driver.get("https://www.facebook.com/setnews/?locale=zh_TW")
time.sleep(5)
#Scroll 
for i in range(1,3):
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    time.sleep(10)

#用BeautifulSoup爬資料
pages = driver.page_source
soup = BeautifulSoup(pages, "html.parser")
para1 = soup.findAll("div", class_="x1iorvi4 x1pi30zi x1swvt13 x1l90r2v")
print("Total: "+str(len(para1))+" articles.")
print("============================")
for obj in para1:
    post = obj.findAll("div", {"dir":"auto"})
    for obj2 in post:
        print(obj2.text)

