from cmath import e
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

import urllib.request
import time
import os

print("What do you want to download?")
download = input()
site = 'https://www.google.com/search?tbm=isch&q='+download

print("How hoften should be scrolled?")
numberOfScrolls = int(input())

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(site)

i=0
while i<numberOfScrolls:
    driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    try:
        driver.find_element_by_xpath("/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[5]/input").click()
    except Exception as e:
        pass
    time.sleep(5)
    i+=1

soup = BeautifulSoup(driver.page_source, 'html.parser')

driver.close();

img_tags = soup.find_all("img", class_="rg_i")


count = 0
for i in img_tags:
    try:
        urllib.request.urlretrieve(i['src'], str(count)+".jpg")
        
        img = Image.open(str(count)+".jpg")

        width, height = img.size

        if(width <=height*6):
            img = img.resize((500,500),Image.LANCZOS)
            img.save(fp=str(count) + ".jpg")
            count+=1
        else:
            os.remove(str(count)+".jpg")
   

    except Exception as e:
        pass