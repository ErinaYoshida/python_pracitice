# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 21:35:37 2021

@author: erina
"""

from bs4 import BeautifulSoup
import requests
#yahooのニュースサイトのurl
url = "https://news.yahoo.co.jp/"
#requestsによりHTMLを取得
r = requests.get(url)
#日本語文字化けを防止
r.encoding = r.apparent_encoding
#BeautifulSoupによりデータを取り出しやすい形に変換
soup = BeautifulSoup(r.content, "html.parser")
#トピックニュースの塊を指定
topic = soup.find("div", class_="sc-dXLFzO pyViR")
#トピックニュースの塊からそれぞれのニュースを抽出
rows = topic.findAll("a")
news = []
for row in rows:
    news.append(row.get_text())
print(news)