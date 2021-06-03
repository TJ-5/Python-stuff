import datetime
import time
from selenium import webdriver

browser = webdriver.Firefox(executable_path=r'C:\Users\tomjo\Documents\geckodriver.exe')
browser.get("https://www.wetter.com/schweiz/zermatt/CH0CH4465.html")
time.sleep(15)
browser.find_element_by_xpath('//*[@id="cmp-btn-accept"]').click()
time.sleep(10)

content = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[1]/span[1]').text
print("")
print("Morgens:")
print("Höchste Temperatur: ", content)
content2 = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[6]/div[4]/div/table/tbody[1]/tr[4]/td[1]/span[2]').text
edited = content2.replace("/", "")
print("Niedrigste Temperatur:", edited)
regen1 = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[6]/td[1]/div/div[2]/span').text
print("Die Regenwahrscheinlichkeit liegt bei ", regen1)
print("")

mittags = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[2]/span[1]').text
print("Mittags:")
print("Höchste Temperatur: ", mittags)
mittags2= browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[2]/span[2]').text
editedmittags2 = mittags2.replace("/", "")
print("Niedrigste Temperatur:", editedmittags2)
regen2 = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[6]/td[2]/div/div[2]/span').text
print("Die Regenwahrscheinlichkeit liegt bei ", regen2)
print("")

Abends = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[3]/span[1]').text
print("Abends:")
print("Höchste Temperatur: ", Abends)
Abends2 = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[3]/span[2]').text
editedAbends = content2.replace("/", "")
print("Niedrigste Temperatur:", editedAbends)
regen3 = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[6]/td[3]/div/div[2]/span').text
print("Die Regenwahrscheinlichkeit liegt bei ", regen3)
print("")

nachts = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[4]/span[1]').text
print("Nachts:")
print("Höchste Temperatur: ", nachts)
nachts2= browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[4]/td[4]/span[2]').text
editednachts2 = mittags2.replace("/", "")
print("Niedrigste Temperatur:", editednachts2)
regen4 = browser.find_element_by_xpath('//*[@id="cnt-with-location-attributes"]/div/table/tbody[1]/tr[6]/td[4]/div/div[2]/span').text
print("Die Regenwahrscheinlichkeit liegt bei ", regen4)
print("")

browser.quit()
print(datetime.datetime.now().strftime("%H:%M:%S - %d.%m.%Y "))
