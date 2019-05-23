import qrspy
import config
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from PIL import Image
from config import qrs
from config import host
import csv
import sys
import time
import os


#read args
arg = "\n".join(sys.argv[1:])

if len(arg) > 0:
    #Set up selenium
    options = Options()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome("./chromedriver.exe", chrome_options=options)

    #Get all sheet objects see if they match appId
    link = ''
    linkList = []
    appObj = qrs.get_appobject(opt=True)
    for i in range(len(appObj)):
        if appObj[i]["app"]["id"] == arg and appObj[i]["objectType"] == "sheet":
            sheetId = appObj[i]["engineObjectId"]
            sheetName = appObj[i]["name"]
            link = "https://" + host + "/sense/app/"+ arg + "/sheet/" + sheetId
            linkList.append(link)
            driver.get(link)
            time.sleep(25)
            sheet = driver.find_element_by_tag_name("body")
            driver.save_screenshot(sheetName + '.png')
            response = qrs.import_appcontent(arg, sheetName + '.png')
            os.remove(sheetName + '.png')
    if len(linkList) <= 0:
        print("Please specify a proper app id as an argument when running the script!")        
else:
    print("Please specify an app id as an argument when running the script!")       
driver.quit() 