#####PARTE II: pasemos BD de empresa a CSV
#pip install xlsxwriter
#pip install xlrd
import pandas as pd
import os
import matplotlib.pyplot as plt
from facebook_scraper import get_posts

os.chdir(r'C:\Users\Andrés\OneDrive\Desktop\Experimentos')
posts = []

# Obtenemos la información de las publicaciones
for post in get_posts('INEIpaginaOficial', pages=5):
    print(post)
    posts.append(post)

# Pasamos a formato base de datos
fb_posts = pd.DataFrame(posts)
plt.plot(fb_posts['time'], fb_posts['likes'])
fb_posts.to_excel('fb_emp.xlsx',index=False)

#####PARTE II.5: entremos a nuestra cuenta y entremos al perfil de un amigo (no se olviden rellenar los txt y descargar los comprimidos)
#inspirado en https://github.com/harismuneer/Ultimate-Facebook-Scraper
#pip install selenium
from sys import exit
import calendar
import time
import os
os.chdir(r"C:\Users\Andrés\OneDrive\Desktop\Experimentos")
import platform
import sys
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def login(email, password):
    """ Logging into our own profile """

    try:
        global driver

        options = Options()

        #  Code to disable notifications pop up of Chrome Browser
        options.add_argument("--disable-notifications")
        options.add_argument("--disable-infobars")
        options.add_argument("--mute-audio")
        # options.add_argument("headless")

        try:
            driver = webdriver.Chrome(executable_path=r"C:\Users\Andrés\AppData\Local\Programs\Python\Python38\Lib\site-packages\selenium\chromedriver.exe", options=options)
            print("you logged in. Let's rock")
        except:
            print("you need web driver!")
            exit()

        driver.get("https://en-gb.facebook.com")
        driver.maximize_window()

        # filling the form
        driver.find_element_by_name('email').send_keys(email)
        driver.find_element_by_name('pass').send_keys(password)

        # clicking on login button
        driver.find_element_by_id('u_0_b').click()
        
    except:
        print("maybe something is wrong")

# -----------------------------------------------------------------------------
# -----------------------------------------------------------------------------

def main():
    with open('credentials.txt') as f:
        email = f.readline().split('"')[1]
        password = f.readline().split('"')[1]

        if email == "" or password == "":
            print("Your email or password is missing. Kindly write them in credentials.txt")
            exit()

    ids = ["https://en-gb.facebook.com/" + line.split("/")[-1] for line in open("input.txt", newline='\n')]

    if len(ids) > 0:
        print("\nStarting Scraping...")

        login(email, password)
        time.sleep(5)
        print(ids)
        driver.get(ids[0])
        #driver.close()
    else:
        print("Input file is empty.")


# -------------------------------------------------------------
# -------------------------------------------------------------
# -------------------------------------------------------------

if __name__ == '__main__':
    # Let's begin
    main()
