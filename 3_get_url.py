from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import csv
import requests
import re
from bs4 import BeautifulSoup

def get_url(name):

    driver=webdriver.Chrome()
    driver.get("https://weixin.sogou.com/")
    driver.find_element(By.ID,'query').send_keys(name)
    driver.find_element(By.XPATH,'//input[@type="submit"]').click() 
    driver.find_element(By.CLASS_NAME,'swz2').click()
    driver.find_element(By.XPATH,"//a[@target='_blank' and contains(@uigs, 'account_article_0')]").click()

    all_window_handles = driver.window_handles

    # 遍历每个窗口句柄
    for window_handle in all_window_handles:
        # 切换到窗口
        driver.switch_to.window(window_handle)
        # 获取当前窗口的URL
        url = driver.current_url
        if 'url=' in url:
            print(requests.get(url))
            break

    driver.quit()
    
    

def main():
    with open("/mnt/d/projectB/py/txtin.csv", 'r' ,encoding = 'utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            name = row[0]
            get_url(name)
            
            
get_url("北大剧社")
