from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


binary = FirefoxBinary('C:\\Program Files\\Mozilla Firefox\\firefox.exe')
kw = input("Provide the keyword to search through google : ")



# creates firefox session
driver = webdriver.Firefox(firefox_binary=binary, executable_path="C:\\geckodriver.exe")
driver.implicitly_wait(30)



# navigate to google
driver.get("http://www.google.com")



#get the search textfield
search_field = driver.find_element_by_id("lst-ib")
search_field.clear()



#enter search kw and submit
search_field.send_keys(kw)
search_field.submit()



lists = driver.find_elements_by_class_name("_Rm")
print ("Elements found : {}".format(len(lists)))



i=0
print("Here are the links : ")
for listitem in lists:
    print(listitem.get_attribute("innerHTML"))
    i=i+1
    if(i>10):
        break



driver.quit()