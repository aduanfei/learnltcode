import requests
import docx
import xlrd
import os
from bs4 import BeautifulSoup
import time

import random

title="1"
ptml=r"http://money.fjsen.com/2022-04/08/content_31003271.htm"
content = requests.get(ptml)
cont = BeautifulSoup(content.text, "lxml")
messa = cont.find(id="new_message_id").findAll("p")
ps = title + "\n"
for p in messa:
    ps = ps + p.text + "\n"
rpath = r"C:\Users\之子言归\Desktop\2022上半年主动宣传\新闻稿"
rpath += "\\" + title + ".docx"
if os.path.exists(rpath):
    os.remove(rpath)
doc = docx.Document()
doc.add_paragraph(ps)
doc.save(rpath)
print(title + " saved!")