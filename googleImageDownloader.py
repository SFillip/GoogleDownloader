from cmath import e
from PIL import Image
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib.request
import time
import os
import sys

site = 'https://www.google.com/search?tbm=isch&q=%27+sys.argv[1]
numberOfScrolls = int(sys.argv[2])

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get(site)

i=0a
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
img_tags = soup.findall("img", class="rg_i")


count = 0
for i in img_tags:
    try:
        urllib.request.urlretrieve(i['src'], str(count)+".jpg")

        img = Image.open(str(count)+".jpg")

        width, height = img.size

        prefWidth=int(sys.argv[3])
        prefHeight=int(sys.argv[4])

        dataFormat=sys.argv[5]

        if(width <=height*6):
            img = img.resize((prefWidth,prefHeight),Image.LANCZOS)
            img.save(fp=str(count) + dataFormat)
            count+=1
        else:
            os.remove(str(count)+dataFormat)
    except Exception as e:
        pass