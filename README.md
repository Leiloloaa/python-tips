# Python_tips

**Python 日常帮手的最佳实践。**

比如： 

- 爬取文档，爬表格，爬学习资料；  
- 玩转图表，生成数据可视化；  
- 批量命名文件，实现自动化办公；  
- 批量搞图，加水印、调尺寸；

## 爬取文档、学习资料

首先，你得先确定你要爬的网站是什么？你要获取的目的是什么？比如，小明想爬青岩帮网站中的招考指南，所以他想搜集目前该网页的所有文章的标题和超链接，以方便后续浏览。（提示：需要先安装 Python 依赖：urllib3 bs4）

> 爬取网站的链接：https://zkaoy.com/sions/exam
> 目的：收集目前该网页的所有文章的标题和超链接

**代码修改**

- 替换为想要下载的网页地址
- 替换为网页保存的文件名

## 抓取表格，做数据分析

我们日常在上网的时候，往往都会看到一些有用的表格，都希望保存下来日后使用，但直接复制到 Excel 往往都很容易发生变形，或者乱码，或者格式错乱等种种问题，借助 Python 可以轻松实现网页中表格的保存。（提示：需要先安装依赖: urllib3, pandas）

执行之后，会在代码文件所在的目录生成 tips2.xlsx 的 excel 文件

**代码修改**

- 替换为想要抓取表格所在网页的网址；
- 替换为表格的序号，比如想要抓取网页中的第几个表格；
- 替换为最终想要保存的文件名。

## 批量下载图片

当我们看到一个网页上有很多喜欢的图片时，一张一张保存效率比较低。
通过 Python 我们也可以实现快速的图片下载。以堆糖网为例，我们看到了这个网页。

感觉很好看，希望能够把所有图片下载下来，方案大体和 1 是一样的。
我们首先下载网页，然后分析其中的 img 标签，然后把图片下载下载来。首先我们在工作目录建立一个文件夹 tips_3 用来放下载的图片。

**代码修改**

- 替换为想要下载网页的网址；
- 替换为想要保存的文件名（网页文件）；
- 替换为网页文件名，值应该和 2 一样；
- 替换为想要保存图片的文件夹，需要创建好文件夹。

另外，有的网站的图片是先显示网页之后才动态加载的，这类动态加载的内容的图片下载是不支持的喔。

## 玩转图表，实现数据可视化

除了使用 Python 编写爬虫来下载资料， Python 在数据分析和可视化方面也非常强大。往往我们在工作中需要经常使用 Excel 来从表格生成曲线图，但步骤往往比较繁琐，而用 Python 则可以轻松实现。


从 csv 或 excel 提取数据来画图
本节需要先安装 pandas 、matplotlib、seaborn
```
pip install pandas
pip install matplotlib
pip install seaborn
```

我们以刚才创建的 tips_2.xlsx 这个 excel 为例，来介绍我们如何把 Excel 表格中的数据画成图。
我们这次将 excel 中的卖出价一列，生成柱状图。

```py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# 使用 pandas 读取 excel， csv 文件的话换成 pd.read_csv 即可
df = pd.read_excel("tips2.xlsx")
# 因为第一行是中文表头，所以我们先过滤掉
df = df[df.index>0]
sns.set()
figure2 = plt.figure(figsize = (10, 5))
figure2.add_subplot(1,1,1)

# 设置轴的属性
plt.xlabel("",fontsize = 14)
plt.ylabel("卖出价", fontsize = 14)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.title("外汇情况", fontsize=14)

# 设置字体的属性
plt.rcParams["font.sans-serif"] = "Arial Unicode MS"
plt.rcParams["axes.unicode_minus"] = False

category = df[0]
index_category = np.arange(len(category))
# 将 卖出价 转换为数字
df[3] = pd.to_numeric(df[3])
plt.xticks(rotation = 90)
plt.bar(x=df[0], height=df[3].values, color=[1,0,1])
plt.show()
```

**代码修改**

- 替换要画图的 excel 文件夹名称
- Y 轴的标题
- 图的标题
- 横轴的数据（第几列做横轴）
- 纵轴的数据（第几列做纵轴）

## 从文本文件中生成词云

```
需要先安装 wordcloud，jieba
conda install -c conda-forge wordcloud
conda install -c conda-forge jieba
```

词云是最近数据分析报告中非常常见的数据表现形式了，它会从一段文字中抽取出高频的词汇并且以图片的形式将它们展示出来
如何用 Python 生成词云呢？为了做示范，我们首先解析第一步我们抓取的 tips_1.html 网页（考研网），将所有的新闻标题都存储到一个文本文档中。

```py
from bs4 import BeautifulSoup

# 输入参数为要分析的 html 文件名，返回值为对应的 BeautifulSoup 对象
def create_doc_from_filename(filename):
    fo = open(filename, "r", encoding='utf-8')
    html_content = fo.read()
    fo.close()
    doc = BeautifulSoup(html_content)
    return doc

doc = create_doc_from_filename("tips1.html")
post_list = doc.find_all("div",class_="post-info")

result = []
for post in post_list:
    link = post.find_all("a")[1]
    result.append(link.text.strip())

result_str="\n".join(result)
with open("news_title.txt", "w") as fo:
    fo.write(result_str)
```

接下来我们将 news_title.txt 这个文本文件中的汉字进行分词，并生成词云。代码如下：

```py
import jieba
import wordcloud
text = ""
with open ("news_title.txt", encoding="utf-8") as fo:
    text = fo.read()
split_list = jieba.lcut(text)
final_text = " ".join(split_list)

stopwords= ["的", "是", "了"]
# Windows 系统的 font_path 替换为'C:\Windows\Fonts\STZHONGS.ttf'
wc = wordcloud.WordCloud(font_path = "/System/Library/Fonts/PingFang.ttc", width=1000, height=700, background_color="white",max_words=100,stopwords = stopwords)
wc.generate(final_text)

import matplotlib.pyplot as plt
plt.imshow(wc)
plt.axis("off")
plt.show()
```

**代码修改**

如果你想生成自己的词云，首先你需要想清楚你的数据来源，一般是一个网页或者一个文本文件。
如果是网页的话可以首先保存到本地，提取文本，之后就可以进行代码替换来生成了。
如果是文本，直接复制在 text，再执行下文即可。

## 使用 Python 实现批量重命名文件

使用 Python 进行批量的文件重命名是比较简单的。比如我们要把一批图片导入到 PS 中编辑，或者导致一批视频文件到 PR 中操作，如果资源的文件名杂乱的话会严重影响效率。所以一般情况下我们都需要首先将相关的文件批量的按照某个规则重命名。

这里我们以前面爬虫示例的 3 小节中批量下载的图片文件夹为例，批量把该文件夹中的所有图片名字重命名为 “图片_0x.jpg ”的形式，其中 x 是图片的序号，逐一递增。

当你希望批量重命名一批文件时，可以首先将这些文件放到某个文件夹中，然后按照下述方法进行批量重命名。

**代码修改**

- 替换为希望批量重命名的文件夹；
- 文件的格式。其中{idx}部分需要保留，代码执行时会被替换为序号。

## 批量给照片加水印

```
需要首先安装 opencv、pillow
pip3 install opencv-python
pip3 install pillow
```

如果手中有非常多的图片，想保护自己版权，或者申明来源，我们可以在图片上加水印。那如何用 Python 给非常多的图片批量加上文字水印呢？
还是以我们在爬虫示例的 3 小节中批量下载的图片文件夹为例。
下述代码会给该文件夹下所有图片的(100,100) 这个坐标点加上“文字水印”这四个中文。坐标点是以图片左上角为基准的。如果图片的宽高小于 100，则不会打上水印。

代码执行完后，可以去 tips_3_watermark 这个文件夹中查看图片，可以看到这里的所有图片都已经被打上了文字水印。

**代码修改**

- 文字水印的位置，以图片左上角为原点；
- 文字水印的内容；
- 文字水印的颜色，RGB 值；
- 想要处理的图片文件夹的名称；
- 处理完成后保存结果的文件夹名称。

## 批量给照片调整饱和度

我们在生活中有经常需要给照片、图片调色的场景，虽然用 PS 可以很方便地完成，但是一张照片一张照片的处理还是比较麻烦。
使用 Python 我们可以非常方便的批量地对照片调整饱和度。
这一节我们还是以前面 03 节批量下载的图片目录为例，给所有照片的饱和度升高为 1.5 倍。
我们首先建立 tips_3_sa 文件夹，用来存放处理过的图片

执行完毕之后，可以看到所有的图片已经被处理后存储在 tips_3_sa 文件夹中了。我们可以对比其中的两幅，左图是处理前，右图是处理后，可以看到颜色饱满了很多。

**代码修改**

- 替换为要处理图片的目录；
- 替换为处理之后的图片存储的目录（需要事先创建好）；
- 替换为饱和度的倍数

## 批量调整照片尺寸

除了调整饱和度外，批量调整照片尺寸也是非常常见的需求。我们继续以 tips_3 文件夹中的图片为例，来批量将所有图片缩写为之前的1/2， 然后存储在 tips_3_resize 目录中。

首先需要在我们的工作目录中建立 tips_3_resize 目录

**代码修改**

- 替换为目标分辨率的高
- 替换为目标分辨率的宽
- 要处理的图片文件夹
- 处理完毕存储结果的文件夹（需要事先创建好

## 总结

技巧出自 https://kaiwu.lagou.com/course/courseInfo.htm?courseId=1236#/detail/pc?id=8704