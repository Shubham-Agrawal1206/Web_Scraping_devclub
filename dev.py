import requests 
from bs4 import BeautifulSoup 
import os

def cont_rev(inte):
    if(inte == 1):
        return "january"
    elif(inte == 2):
        return "february"
    elif(inte == 3):
        return "march"
    elif(inte == 4):
        return "april"
    elif(inte == 5):
        return "may"
    elif(inte == 6):
        return "june"
    elif(inte == 7):
        return "july"
    elif(inte == 8):
        return "august"
    elif(inte == 9):
        return "september"
    elif(inte == 10):
        return "october"
    elif(inte == 11):
        return "november"
    elif(inte == 12):
        return "december"
    else:
        return "error!"

def img_save(img_s,dat):
    if(img_s.startswith("/")):
        image_url = "https:%s"%(img_s)
    else:
        image_url = "%s"%(img_s)
    r = requests.get(image_url) 
    img_m= "%s-%s.png"%(dat,author)
    with open(img_m,'wb') as f: 
        f.write(r.content)

def scan(year,month):
    os.mkdir(cont_rev(month))
    os.chdir(cont_rev(month))
    if (month>=10):
        URL1= "http://explosm.net/comics/archive/%d/%d/%s"%(year,month,author)
    else:
        URL1= "http://explosm.net/comics/archive/%d/0%d/%s"%(year,month,author)
    r=requests.get(URL1)
    print(URL1)
    soup = BeautifulSoup(r.content, 'html5lib')
    for row in soup.findAll('div',attrs={'class':'small-3 medium-3 large-3 columns'}):
        URL2="http://explosm.net" + row.a['href']
        r2 = requests.get(URL2)
        soup2 = BeautifulSoup(r2.content, 'html5lib')
        row2 = soup2.find('section',attrs={'id':'comic-area'})
        img_p = row2.find('div',attrs={'id':'comic-wrap'}) 
        img_src= img_p.img['src']
        date=row2.find('div',attrs={'id':'comic-info'}).find('div',attrs={'id':'comic-info-text'}).div.text[1:11]
        print(date)
        print(img_src)
        img_save(img_src,date)
    os.chdir("../")

def cont(str):
    if(str.lower() == "january"):
        return "01"
    elif(str.lower() == "february"):
        return "02"
    elif(str.lower() == "march"):
        return "03"
    elif(str.lower() == "april"):
        return "04"
    elif(str.lower() == "may"):
        return "05"
    elif(str.lower() == "june"):
        return "06"
    elif(str.lower() == "july"):
        return "07"
    elif(str.lower() == "august"):
        return "08"
    elif(str.lower() == "september"):
        return "09"
    elif(str.lower() == "october"):
        return "10"
    elif(str.lower() == "november"):
        return "11"
    elif(str.lower() == "december"):
        return "12"
    else:
        return "error!"
   
re = open("input.txt","r")
str1 = re.readline()
str2 = re.readline()
author = re.readline().lower()
print(author)

x= str1.index(" ")
mi= str1[:x]
yi= int(str1[x+1:])
y= str2.index(" ")
mf= str2[:y]
yf= int(str2[y+1:])
mip=cont(mi)
mfp=cont(mf)

for z in range(yi,yf+1):
    os.mkdir(str(z))
    os.chdir(str(z))
    if(z==yi):
        for w in range(int(mip),13):
            scan(z,w)
    elif(z==yf):
        for w in range(1,int(mfp)+1):
            scan(z,w)
    else:
        for w in range(1,13):
            scan(z,w)
    os.chdir("../")