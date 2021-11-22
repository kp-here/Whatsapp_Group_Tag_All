from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#okayy

# grp_name = input("\nEnter Group Name :\n")
grp_name="Kozhikoood"

#importing contact names


#loading web driver
driver = webdriver.Chrome(executable_path=r'T:\Whatsapp Automation\chromedriver.exe')
wait = WebDriverWait(driver, 5)
driver.maximize_window()
driver.get('https://web.whatsapp.com/')


#selenium functions to select and click elements
def findbyxpath(x):
    a= wait.until(EC.presence_of_element_located((By.XPATH, x)))
    a.click()
    return a

def findbyxpath_noclick(x):
    return wait.until(EC.presence_of_element_located((By.XPATH, x)))

#click search box
group_title = WebDriverWait(driver, 600).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")))
group_title.click()

#type in group name and select it
group_title.send_keys(grp_name + Keys.ENTER) 

#clicked on group name header
head_title= findbyxpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]")

