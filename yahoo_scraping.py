import requests
from bs4 import BeautifulSoup
yahoo_main_news_xml = requests.get("https://news.yahoo.co.jp/pickup/rss.xml")
soup = BeautifulSoup(yahoo_main_news_xml.text,"html.parser")
for news in soup.findAll("item"):
    print(news.title.string)
