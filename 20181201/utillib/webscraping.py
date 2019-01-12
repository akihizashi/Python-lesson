import requests

class WebScraping:

    def __init__(self):
        super().__init__
    ##
    ## HTMLのダウンロード
    ##
    def downloadHTML(url):
        response = requests.get(url)
        #文字コードを設定
        response.encoding = response.apparent_encoding
        return response.text
