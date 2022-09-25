from urllib import response
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import undetected_chromedriver as uc
import time
#https://selenium-python.readthedocs.io/locating-elements.html

def GetFarmList(monsterName):

    url = 'https://meso.kr/monster.php?n='+monsterName
    options = uc.ChromeOptions()
    #options.add_experimental_option("excludeSwitches", ["enable-logging"])
    options.headless=True
    #options.add_argument('--headless')

    driver = uc.Chrome(version_main=104,use_subprocess=True)
    driver.get(url)
    # driver = webdriver.Chrome('./chromedriver.exe',options=options)
    # driver.implicitly_wait(3)
    # driver.get(url)

    #response = requests.get(url)
    time.sleep(5)
    soup=driver.page_source
    if driver.title.find(monsterName)==0:
        tag = driver.find_elements(By.CLASS_NAME,"copybtn")
        subtag=[]
        for i in tag:
            subtag.append(i.get_attribute('dt-name'))
        driver.close()
        return subtag
    else : 
        print('')
    # if response.status_code == 200:
    #     html = response.text
    #     soup = BeautifulSoup(html, 'html.parser')
    #     tag = soup.find_all(attrs={'class': 'btn btn-primary btn-sm copybtn'})
    #     subtag=[]
    #     for i in tag:
    #         subtag.append(i['dt-name'])
    #     return subtag
    # else : 
    #     print(response.status_code)
