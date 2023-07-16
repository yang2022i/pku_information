#!/bin/python
import requests
import re
from bs4 import BeautifulSoup
import os
import csv


def function(url,c):   #传入网址和文件名
    
    #新建文件夹
    save_dir = "/mnt/d/projectB/py/outcome/" + str(c) + "/"
    if os.path.exists(save_dir):
        pass
    else:
        os.mkdir(save_dir)

    #获取并格式化
    r = requests.get(url)
    r.encoding = 'utf-8'
    html_doc = r.text

    #文字获取部分
    s = BeautifulSoup(html_doc,features='lxml')
    doc = s.find_all("p")

    for item in doc:
        ptxt = re.sub('\s',' ',item.get_text())
        with open(save_dir+"0.txt",'a',encoding = 'utf-8') as f:
            f.write(ptxt + '\n')

    print("find doc ok!!")

    #图片获取部分
    s2 = BeautifulSoup(html_doc,"html.parser") 
    img = s2.find_all("img")

    i = 0
    for item in img:
        src=''
        print ('')
        print ('.........img begin .......')
        try:
            src = item["src"]
        except:
            try:
                src = item["data-src"]
            except:
                src = item["id"]
                
        if "https" not in src:
            continue
        
        print (src)
        print ('.........img end .......')

        resp_img = requests.get(src)
        with open(save_dir+"path{}.jpg".format(i), "wb") as f:
            f.write(resp_img.content)
            i = i + 1


def main():

    c = 0
    
    with open("/mnt/d/projectB/py/stdin.csv", 'r' ,encoding = 'utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row[0])
            url = row[0]
            function(url,c)
            c = c + 1
            
            if c==5:    #临时加的终止条件
                break
    
main()

