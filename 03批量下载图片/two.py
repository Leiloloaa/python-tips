from bs4 import BeautifulSoup

from urllib.request import urlretrieve


# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象

def create_doc_from_filename(filename):

    fo = open(filename, "r", encoding='utf-8')

    html_content = fo.read()

    fo.close()

    doc = BeautifulSoup(html_content)

    return doc


doc = create_doc_from_filename("tips3.html")

images = doc.find_all("img")

for i in images:

    src = i["src"]

    filename = src.split("/")[-1]

    # print(i["src"])

    urlretrieve(src, "tips_3/" + filename)
