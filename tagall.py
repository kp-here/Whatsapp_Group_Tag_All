from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

#hello
# grp_name = input("\nEnter Group Name :\n")
grp_name="kozhikoood"

#importing contact names


#loading web driver
driver = webdriver.Chrome(executable_path=r'T:\Whatsapp Automation\chromedriver.exe')
wait = WebDriverWait(driver, 20)
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
group_title = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//div[@class='_13NKt copyable-text selectable-text']")))
group_title.click()

#type in group name and select it
group_title.send_keys(grp_name + Keys.ENTER) 

#clicked on group name header
head_title= findbyxpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[4]/div[1]/header[1]/div[2]/div[1]/div[1]/span[1]")


#view all
try:
    view_all= WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[3]/span[1]/div[1]/span[1]/div[1]/div[1]/section[1]/div[6]/div[2]/button[1]/div[2]")))
except:
    print("error occured")
else:
    view_all.click()
finally:
    time.sleep(2)
    page_s=driver.page_source
    soup = bs( page_s , 'html.parser')

    l=set()

    for i in soup.find_all(class_="_3Bc7H KPJpj"):
        for j in i.find_all(class_="emoji-texttt _ccCW FqYAR i0jNr"): 
            l.add(j.text)
    
    l.remove("You")
    k=list(l)

    with open('a.txt','w',encoding="utf-8") as f:
        for i in k:
            f.write(i+"\n")
    f.close()


    try:
        #cross button
        cross_button=WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH,"/html[1]/body[1]/div[1]/div[1]/span[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/header[1]/div[1]/div[1]/button[1]")))
        
    except:
        print("error occured")
    else:
        cross_button.click()
        
    finally:
        #messagebox
        type_box=findbyxpath("//div[@class='_1UWac _1LbR4']//div[@class='_13NKt copyable-text selectable-text']")
        for i in k:
            type_box.send_keys("@"+ i + Keys.ENTER)
        type_box.send_keys(Keys.ENTER) 

