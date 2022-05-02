# NOTA PARA QUE EL SCRIPT FUNCIONES SE DEBE TENER LAS IMÁGENES DE REACCIONES EN LA MISMA CARPETA DE OS.CHDIR
# ADEMÁS DE NO TENER NINGUNA NOTIFICACIÓN PENDIENTE DE LEER EN FACEBOOK
# Y TENER EL IDIOMA EL ESPAÑOL
from sys import exit
import pandas as pd
import re
import calendar
import time
import os
import platform
import sys
import time
from urllib.request import urlretrieve #pip install resumable-urlretrieve
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image

# Definir directorio
os.chdir(r"C:\Users\Andrés\OneDrive\Desktop\Experimentos\CEMI")

# Cargamos un diccionario de imágenes de reacciones para su reconocimiento
like = Image.open('0.png')
love = Image.open('1.png')
haha = Image.open('2.png')
wow = Image.open('3.png')
sad = Image.open('4.png')
hate = Image.open('5.png')
care = Image.open('6.png')

# Listas para guardar resultados
nombres = []
textos = []
likes = []
loves = []
hahas = []
wows = []
sads = []
hates = []
cares = []

# Iniciamos el Selenium
options = Options()
options.add_argument("--disable-notifications")
options.add_argument("--disable-infobars")
options.add_argument("--mute-audio")
options.add_argument("--start-maximized")
driver = webdriver.Chrome(executable_path=r"C:\Users\Andrés\AppData\Local\Programs\Python\Python38\Lib\site-packages\selenium\chromedriver.exe", options=options)
driver.get("https://web.facebook.com/")
time.sleep(5)

# Como necesitamos credenciales para ver mejor una página de un amigo, iniciaremos sesión
driver.find_element(By.XPATH,"//input[contains(@id,'email')]").send_keys("andycampa17@hotmail.com")
driver.find_element(By.XPATH,"//input[contains(@id,'pass')]").send_keys("")
driver.find_element(By.XPATH,"//button[contains(@name,'login')]").click()
time.sleep(10)

# Con las credenciales ya listas, entremos a un perfil
driver.get("https://web.facebook.com/beremiz.rojas")
time.sleep(7)
name = driver.find_element(By.XPATH,'//h1')
name = name.text

# Bucle para diferentes publicaciones
for publ in range(1,6):
    # Bajamos un poco la página
    nombres.append(name)
    time.sleep(3)
    bajar = 'window.scrollTo(0,' + str(250) + ')' # para que cargue un poco la página
    driver.execute_script(bajar)
    time.sleep(10)

    # Nos movemos a la publicación que deseamos scrapear
    pub_numero=publ
    element=driver.find_element(By.XPATH,"//div[contains(@data-pagelet,'ProfileTimeline')]/div["+str(pub_numero)+"]//span[contains(@dir,'auto')]/span") # ubicamos el driver en la fecha (puesto que ahí está el id del post, para analizar más fácil)
    driver.execute_script("arguments[0].scrollIntoView();", element)
    driver.execute_script("scrollBy(0,-200);") # subimos un poco la página puesto que está la ventana flotante de botones
    element.click()
    time.sleep(5)
    
    # Volvemos arriba para no malversar el scraping
    driver.execute_script("scroll(0, 0);")
    time.sleep(5)
    
    # Obtenemos el texto de la publicación
    texto=driver.find_element(By.XPATH,"//div[contains(@data-ad-preview,'message')]")
    texto=texto.text
    print(texto)
    textos.append(texto)
    
    try:
    
        # Damos click a las reacciones para ver reacción por reacción
        driver.find_element(By.XPATH,"//span[contains(@aria-label,'Consulta quién reaccionó a esto')]").click()
        time.sleep(5)
        
        # Encontramos el número de reacciones distintas
        reac_num=driver.find_elements(By.XPATH,"//div[contains(@aria-label,'Reacciones')]//div[contains(@role,'tab')]/div/div/img[contains(@src,'http')]")
        
        # Ahora sí, damos click reacción por reacción, vemos que imagen es y la comparamos con el diccionario, retorna que tipo de reacción es, y el scraping su cantidad
        for z in range(0,len(reac_num)):
            if len(reac_num)==1:
                reac=reac_num[z].get_attribute("src")
                reac_cant=driver.find_elements(By.XPATH,"//div[contains(@aria-label,'Reacciones')]//div[contains(@role,'tab')]/div/span/span")
                r=reac_cant[0].text
                urlretrieve(reac, 'comparar.png')
                reaccion = Image.open('comparar.png')
                if list(like.getdata()) == list(reaccion.getdata()):
                    print(r,"likes")
                    likes.append(r)
                if list(love.getdata()) == list(reaccion.getdata()):
                    print(r,"loves")
                    loves.append(r)
                if list(haha.getdata()) == list(reaccion.getdata()):
                    print(r,"hahas")
                    hahas.append(r)
                if list(wow.getdata()) == list(reaccion.getdata()):
                    print(r,"wows")
                    wows.append(r)
                if list(sad.getdata()) == list(reaccion.getdata()):
                    print(r,"sads")
                    sads.append(r)
                if list(hate.getdata()) == list(reaccion.getdata()):
                    print(r,"hates")
                    hates.append(r)
                if list(care.getdata()) == list(reaccion.getdata()):
                    print(r,"cares")
                    cares.append(r)
                    
            else:
                driver.find_element(By.XPATH,"//div[contains(@aria-label,'Reacciones')]//div[contains(@role,'tab')]["+str(z+2)+"]").click()
                reac=reac_num[z].get_attribute("src")
                reac_cant=driver.find_elements(By.XPATH,"//div[contains(@aria-label,'Reacciones')]//div[contains(@role,'tab')]/div/span/span")
                r=reac_cant[0].text
                urlretrieve(reac, 'comparar.png')
                reaccion = Image.open('comparar.png')
                if list(like.getdata()) == list(reaccion.getdata()):
                    print(r,"likes")
                    likes.append(r)
                if list(love.getdata()) == list(reaccion.getdata()):
                    print(r,"loves")
                    loves.append(r)
                if list(haha.getdata()) == list(reaccion.getdata()):
                    print(r,"hahas")
                    hahas.append(r)
                if list(wow.getdata()) == list(reaccion.getdata()):
                    print(r,"wows")
                    wows.append(r)
                if list(sad.getdata()) == list(reaccion.getdata()):
                    print(r,"sads")
                    sads.append(r)
                if list(hate.getdata()) == list(reaccion.getdata()):
                    print(r,"hates")
                    hates.append(r)
                if list(care.getdata()) == list(reaccion.getdata()):
                    print(r,"cares")
                    cares.append(r)
        
        if len(likes)!=publ:
            likes.append("0")
        if len(loves)!=publ:
            loves.append("0")
        if len(hahas)!=publ:
            hahas.append("0")
        if len(wows)!=publ:
            wows.append("0")
        if len(sads)!=publ:
            sads.append("0")
        if len(hates)!=publ:
            hates.append("0")
        if len(cares)!=publ:
            cares.append("0")
            
        driver.back()
        time.sleep(3)
        
    except:
        likes.append("0")
        loves.append("0")
        hahas.append("0")
        wows.append("0")
        sads.append("0")
        hates.append("0")
        cares.append("0")
        
    
fb = pd.DataFrame(data=[nombres,textos,likes,loves,hahas,wows,sads,hates,cares]).transpose()
fb.columns = ["Nombre en Facebook","Contenido","Likes","Loves","HAHAs","WOWs","Sads","Hates","Cares"]
fb.to_excel("aqui.xlsx",index=False)


