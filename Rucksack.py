import datetime
import time
import re
from selenium import webdriver

class browserinformation:
    browser = webdriver.Firefox(executable_path='F:\Py\geckodriver.exe')
    browser.get("https://www.recon-company.com/")
    time.sleep(3)
    browser.find_element_by_xpath('/html/body/div[2]/div/header/div[2]/div[1]/nav/ul/li[3]/a/i').click()
    time.sleep(2)

    browser.find_element_by_xpath('//*[@id="email"]').send_keys('katrin.joeres@freenet.de')
    browser.find_element_by_xpath('//*[@id="passwort"]').send_keys('Tom28032005.')
    time.sleep(0.5)
    browser.find_element_by_xpath('/html/body/div[2]/div/section/div/div[2]/div[2]/div/div/form/div[5]/button').click()
    browser.find_element_by_xpath('/html/body/div[2]/div/section/div/div[2]/div/div[2]/div[5]/a[1]').click()
    
    global Eigenschaft 
    Eigenschaft = browser.find_element_by_xpath('/html/body/div[2]/div/section/div/div[2]/div/div[2]/div[1]/div[2]/div[4]/div[2]').text
    
    browser.quit()
    

class printinforamtion:
    file = open("Rucksack Bestellung.txt", "w")
    file.write(datetime.datetime.now().strftime("%H:%M:%S - %d.%m.%Y ") )
    re.sub(r"^\s+", "", Eigenschaft)
    file.write("\n" + Eigenschaft)
