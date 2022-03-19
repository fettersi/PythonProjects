import requests
from xml.etree import ElementTree
import bs4
import html5lib

# 不同网址输出不全会没法调整
res = requests.get("https://rcu.szshkj.net")
res.encoding="utf-8"
# print(res.text)

# html5lib执行兼容性更好
soup = bs4.BeautifulSoup(res.text, 'html5lib')
print(soup)

with open("input1.txt","w+") as fin:
    fin.write(res.text)

with open("input1.txt","r") as fr,open('input2.txt','w',encoding = 'utf-8') as fd:
    for text in fr.readlines():
        if text.split():
            # res.text = res.text.strip("\n")
            fd.write(text)
    print("写入成功")
fd.close()

# r = ElementTree.XML(res.text)
# print(r)
# print(res.status_code)