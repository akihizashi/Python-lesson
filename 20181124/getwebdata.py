
from webscraping import WebScraping
from bs4 import BeautifulSoup

webscraping = WebScraping
#htmlのダウンロード
html_data = webscraping.downloadHTML('https://www.cbc.ac.jp/sitemap.html')
#htmlデータの出力
# print(html_data)

#タイトルタグ
soup = BeautifulSoup(html_data,'html.parser')
# title = soup.title.string
# print(title)

#データの取得
#貿易コースの取得
extract_html_data = soup.select(".sitemap .bold")
# print(extract_html_data)

# #全コースの取得
# course_data_html = soup.select(".coursebox li")
# print(course_data_html)

for each_course in extract_html_data:
    print("---------------------------")
    print(each_course)
    # print("---------------------------")
    # print(each_course.select('a'))
