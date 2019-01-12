
from webscraping import WebScraping
from bs4 import BeautifulSoup

webscraping = WebScraping
#htmlのダウンロード
html_data = webscraping.downloadHTML('https://www.cbc.ac.jp/sitemap.html')

#タイトルタグ
soup = BeautifulSoup(html_data,'html.parser')

#全コースの取得
course_data_html = soup.select(".sitemap .emp")

for each_course in course_data_html:
    print("---------------------------")
    print(each_course)
