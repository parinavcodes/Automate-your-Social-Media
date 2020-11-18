import pandas as pd
from datetime import datetime
import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import *
import autoit

chrome_path=''
fb_page_url=""
fb_username= ""
fb_password= ""
insta_username= ""
insta_password= ""
linkedin_url=""
linkedin_username= ""
linkedin_password= ""

def facebook_post(desc,img_path):
    driver=webdriver.Chrome(executable_path=chrome_path)
    driver.get(fb_page_url)
    t_out = 10
    #log in tab
    try:
        element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("Timed out waiting for login page to load")
        return

    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[1]/input").send_keys(fb_username)
    time.sleep(0.3)
    driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[2]/input").send_keys(fb_password)
    driver.implicitly_wait(3000)
    button = driver.find_element_by_xpath("/html/body/div[1]/div[2]/div/div/div/div/div[2]/form/table/tbody/tr[2]/td[3]/label/input")
    driver.execute_script("arguments[0].click();", button)

    #post tab
    try:
        element_pres = EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("Timed out waiting for page to load")
    time.sleep(8)
    if desc!='no desc.':
        split=desc.split()
        txt=driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea")
        time.sleep(5)
        driver.execute_script("""
                    var elm = arguments[0], text = arguments[1];
                    if (!('value' in elm))
                      throw new Error('Expected an <input> or <textarea>');
                    elm.focus();
                    elm.value = text;
                    elm.dispatchEvent(new Event('change'));
                    """,txt,desc)
    else:
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div/div/div/form/div[1]/div/div[2]/textarea").click()
    time.sleep(4)
    try:
        element_pres = EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/div/span/a/div[2]/input'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("Timed out waiting for text box to load")

    if img_path!="0":
        driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/div/table/tbody/tr[1]/td[2]/div/div/span/a/div[2]/input").send_keys(img_path)
        try:
            element_pres = EC.presence_of_element_located((By.XPATH,'/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/span/button'))
            WebDriverWait(driver, t_out).until(element_pres)
        except TimeoutException:
            print("Timed out waiting for image to load")
        time.sleep(2)
        button = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[1]/div[2]/div[3]/div[2]/div[2]/div/span/button/span")
        driver.implicitly_wait(3000)
        driver.execute_script("arguments[0].click();", button)

    else:
        button = driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[2]/div[2]/div/div[3]/div[2]/div/div[1]/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div[3]/div[2]/div[2]/div/button/span")
        driver.implicitly_wait(3000)
        driver.execute_script("arguments[0].click();", button)

    time.sleep(10)
    driver.close()


def instagram_post(desc, img_path):
    options = Options()
    mobile_emulation = {"deviceName": "Nexus 5"}
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
    options.add_argument("--disable-notifications")
    driver = webdriver.Chrome(executable_path=chrome_path, options=options)
    driver.get("https://www.instagram.com/accounts/login/?next=%2F&source=mobile_nav")

    time.sleep(3)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[4]/div/label/input").send_keys(insta_username)
    time.sleep(0.3)
    driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[5]/div/label/input").send_keys(insta_password)
    time.sleep(0.5)
    button = driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div/div/div/form/div[7]/button/div")
    driver.implicitly_wait(3000)
    driver.execute_script("arguments[0].click();", button)
    time.sleep(1)

    t_out = 5
    check = 0
    try:
        element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/section/main/div/div/div/button'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("no pop up")
        check = 1
    if check == 0:
        button = driver.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/button")
        driver.implicitly_wait(3000)
        driver.execute_script("arguments[0].click();", button)

    time.sleep(1)
    check = 0
    try:
        element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div/div[3]/button[2]'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("no pop up")
        check = 1
    if check == 0:
        button = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
        driver.implicitly_wait(3000)
        driver.execute_script("arguments[0].click();", button)
        check = 0

    time.sleep(1)

    try:
        element_pres = EC.presence_of_element_located(
            (By.XPATH, '//*[@id="react-root"]/section/nav[2]/div/div/div[2]/div/div/div[3]'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("button not found")
        check = 1

    time.sleep(2)

    if check == 0:
        driver.find_element_by_xpath("//div[@role='menuitem']").click()

    time.sleep(1.5)
    autoit.win_active("Open")  # open can change by your os language if not open change that
    time.sleep(2)
    autoit.control_send("Open", "Edit1", img_path)
    time.sleep(1.5)
    autoit.control_send("Open", "Edit1", "{ENTER}")
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
    time.sleep(1.5)
    if desc!="no desc.":
        split=desc.split()
        #driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea").send_keys(desc)
        for i in split:
             driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea").send_keys(i)
             time.sleep(0.01)
             driver.find_element_by_xpath("/html/body/div[1]/section/div[2]/section[1]/div[1]/textarea").send_keys(" ")
             time.sleep(0.01)
    time.sleep(2)
    driver.find_element_by_xpath("/html/body/div[1]/section/div[1]/header/div/div[2]/button").click()
    time.sleep(20)
    driver.close()


def linkedin_post(desc,img_path):
    driver = webdriver.Chrome(executable_path=chrome_path)
    driver.get(linkedin_url)
    t_out=5
    f=0
    try:
        element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/form/div[1]/input'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("1st type linkedin Page not loaded1")
        f=1
    time.sleep(2)
    if f==1:
        driver.find_element_by_xpath("/html/body/div/div/form[1]/section/p/a").click()
        try:
            element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div/div/form[2]/input[1]'))
            WebDriverWait(driver, t_out).until(element_pres)
        except TimeoutException:
            print("2nd type Page not loaded")
            return
        time.sleep(0.5)
        driver.find_element_by_xpath("/html/body/div/div/form[2]/input[1]").send_keys(linkedin_username)
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/div/form[2]/input[2]").send_keys(linkedin_password)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/div/form[2]/input[7]").click()
    else:
        driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[1]/input").send_keys(linkedin_username)
        time.sleep(0.3)
        driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[2]/input").send_keys(linkedin_password)
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div/main/div[2]/form/div[3]/button").click()
    t_out=10
    while 1:
        try:
            element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div[9]/div[4]/div/div/div/div/div[1]/div/div[1]/button[1]'))
            WebDriverWait(driver, t_out).until(element_pres)
            break
        except TimeoutException:
            print("Home Page not loaded")
    driver.find_element_by_xpath("/html/body/div[9]/div[4]/div/div/div/div/div[1]/div/div[1]/button[1]").click()
    time.sleep(1.5)
    try:
        element_pres = EC.presence_of_element_located((By.XPATH, '/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]'))
        WebDriverWait(driver, t_out).until(element_pres)
    except TimeoutException:
        print("text box not loaded")
    if desc!="no desc.":
        split=desc.split()
        #driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]").send_keys(desc)
        for i in split:
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]").send_keys(i)
            time.sleep(0.01)
            driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]").send_keys(" ")
            time.sleep(0.01)

    # driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]").send_keys(desc)
    time.sleep(7)
    if img_path!='0':
        driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[1]/button[1]').click()
        time.sleep(1.5)
        autoit.win_active("Open")
        time.sleep(2)
        autoit.control_send("Open", "Edit1", img_path)
        time.sleep(1.5)
        autoit.control_send("Open", "Edit1", "{ENTER}")
        time.sleep(1.5)
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div/div[2]/div/button[2]/span").click()
    else:
        driver.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/button/span").click()
    time.sleep(15)


""" 
cur_time=datetime.now().time()
print(cur_time)
df=pd.read_excel("postingxlsx.xlsx")
df.Image=df.Image.fillna(0)
df.Desc=df.Desc.fillna("no desc.")
print(df)
for i, row in df.iterrows():
    if cur_time>=row['Time']:
        if row['Platform'].lower() =="facebook":
             if row['Image']==0:
                   if row['Desc']=="no desc.":
                       print("No Description and Image")
                       continue
                   st=str(0)
                   facebook_post(str(row['Desc']),st)
                   instagram_post(str(row['Desc']),st)
             else:
                   facebook_post(str(row['Desc']),row['Image'])
                   instagram_post(str(row['Desc']),row['Image'])
        elif row['Platform'].lower() =="instagram":
              if row['Image']==0:
                 print("Image not found")
              else:
                 instagram_post(str(row['Desc']),row['Image'])
                 facebook_post(str(row['Desc']),row['Image'])
        elif row['Platform'].lower() == "linkedin":
            if row['Image']==0:
                if row['Desc'] == "no desc.":
                    print("No Description and Image")
                    continue
                st=str(0)
                linkedin_post(str(row['Desc']),st)
            else:
                linkedin_post(str(row['Desc']),row['Image'])
"""
