import time
from selenium import  webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\tomjo\Documents\geckodriver.exe')
browser.get("https://www.zermatt.ch/Schneebericht")
time.sleep(5)
Schneeberg = browser.find_element_by_xpath('//*[@id="overview"]/div[2]/div[1]/div/span').text
print("Schnee auf dem Berg in cm: ", Schneeberg)

Schneeort = browser.find_element_by_xpath('//*[@id="overview"]/div[2]/div[2]/div/span').text
print("SChnee im Ort in cm: ", Schneeort)

Pisten = browser.find_element_by_xpath('//*[@id="overview"]/div[2]/div[3]/div/span[2]').text
print("Es sind ", Pisten, "360 km Pisten befahrbar")

Anlagen = browser.find_element_by_xpath('//*[@id="overview"]/div[2]/div[4]/div/span[2]').text
print("Es sind ", Anlagen, "Anlagen offen")
browser.quit()
datei = open('Schnee_in_Zermatt.txt','a')
datei.write("Schnee auf dem Berg in cm:")
