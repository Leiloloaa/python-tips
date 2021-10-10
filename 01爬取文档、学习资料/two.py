from bs4 import BeautifulSoup

# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象


def create_doc_from_filename(filename):
    fo = open(filename, "r", encoding='utf-8')
    html_content = fo.read()
    fo.close()
    doc = BeautifulSoup(html_content)
    return doc


doc = create_doc_from_filename("tips1.html")
post_list = doc.find_all("div", class_="post-info")
for post in post_list:
    link = post.find_all("a")[1]
    print(link.text.strip())
    print(link["href"])
