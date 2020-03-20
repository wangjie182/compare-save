import requests
from bs4 import BeautifulSoup
import re
import xlrd
import csv


url="http://top.100ppi.com/hs/detail-day---1.html"
try:
   kv = {"user-agent":"Mozilla/5.0"}
   r = requests.get(url,headers=kv)#更改访问浏览方式
   r.raise_for_status ()
   r.encoding = r.apparent_encoding#更改内容编码信息
   demo = r.text   
   soup = BeautifulSoup(demo,"html.parser")#用BeautifulSoup库进行解析
   #print(soup)
except:
   print("访问错误")

pat=soup.find_all("div","detail")
s = 0
for tr in pat:
   ltr = tr.find_all("tr")
   for tr in ltr:
       ltd = tr.find_all("td")
       data = [str(a.string) for a in ltd]
       #print("\t".join(data))
    #    print(data[0])
       filename = "E:\\生意社现货.csv"
       filename2 = "E:\\生意社现货2.csv"
       with open(filename2,"w+") as csvfile: 
        writer = csv.writer(csvfile)
        with open(filename) as f:
            u = csv.reader(f)
            for i in u:
                if data[0] == i[0]:
                    i.append(data[2])
                    i.append(data[3])
                writer.writerow(i)
                print(i)
                print("1")
        
