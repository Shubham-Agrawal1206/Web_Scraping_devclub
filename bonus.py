import requests 
from bs4 import BeautifulSoup 
import os

def img_save(img_s,i):
    if(img_s.startswith("/")):
        image_url = "https:%s"%(img_s)
    else:
        image_url = "%s"%(img_s)
    r = requests.get(image_url) 
    img_m= "frame%d.png"%(i)
    with open(img_m,'wb') as f: 
        f.write(r.content)

def img_save_2(img_s,date,author):
    if(img_s.startswith("/")):
        image_url = "https:%s"%(img_s)
    else:
        image_url = "%s"%(img_s)
    r = requests.get(image_url) 
    img_m= "%s-%s.png"%(date,author)
    with open(img_m,'wb') as f: 
        f.write(r.content)

def func1():
    r=requests.get("http://explosm.net/rcg")
    soup = BeautifulSoup(r.content, 'html5lib')
    i=1
    img_span = soup.find('div',attrs={'class':'rcg-panels'})
    for img_src in img_span.findAll('img'):
        img_save(img_src['src'],i)
        i+=1

def func2():
    r=requests.get(req)
    soup = BeautifulSoup(r.content, 'html5lib')
    row = soup.find('section',attrs={'id':'comic-area'})
    src = row.find('div',attrs={'id':'comic-wrap'}).img['src']
    row2= row.find('div',attrs={'id':'comic-author'})
    date = row2.text[1:11]
    author= row2.text[15:-1]
    img_save_2(src,date,author)
    prev_src = row.find('a',attrs={'class':'nav-previous'})['href']
    return "http://explosm.net%s"%(prev_src)

re = open("input_bonus.txt","r")
str1 = re.readline()

if(str1.lower()=="random"):
    os.mkdir("random")
    os.chdir("random")
    func1()
else:
    os.mkdir("latest")
    os.chdir("latest")
    x= str1.index(" ")
    initial= str1[:x]
    count= int(str1[x+1:])
    req="http://explosm.net"
    for z in range(count):
        abc=func2()
        req=abc