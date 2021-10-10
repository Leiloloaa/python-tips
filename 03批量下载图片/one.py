import urllib3


# 第一个函数，用来下载网页，返回网页内容

# 参数 url 代表所要下载的网页网址。

# 整体代码和之前类似

def download_content(url):

    http = urllib3.PoolManager()

    response = http.request("GET", url)

    response_data = response.data

    html_content = response_data.decode()

    return html_content

# 第二个函数，将字符串内容保存到文件中

# 第一个参数为所要保存的文件名，第二个参数为要保存的字符串内容的变量


def save_to_file(filename, content):

    fo = open(filename, "w", encoding="utf-8")

    fo.write(content)

    fo.close()


url = "https://www.duitang.com/search/?kw=ins%E9%A3%8E%E8%83%8C%E6%99%AF%E5%9B%BE&type=feed"

result = download_content(url)

save_to_file("tips3.html", result)
