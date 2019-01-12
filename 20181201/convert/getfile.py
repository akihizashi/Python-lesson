from bs4 import BeautifulSoup
from utillib.webscraping import WebScraping
import re
import math

#
# ファイルの取得とスクレイピング処理全般
#
class GetFile():

    def __init__(self,url):
        self.url = url
    #
    # １ページ目のコンテンツの取得
    # @type string url ダウンロードURL
    #
    def getContents(self):
        ws = WebScraping;
        res = ws.downloadHTML(self.url)
        soup = BeautifulSoup(res,'html.parser')
        recruit_list = self.getPageData(soup)
        return recruit_list

    #
    # 1ページあたりのコンテンツデータの取得する
    # @type object soup パースされたHTML
    # @return arr 求人リスト
    #
    def getPageData(self, soup):
        #求人の一覧
        element_list = soup.select(".c-job_offer-box")
        #１求人あたりのデータ
        recruit_list =[]
        for element in element_list:
            recruit = self.getSingleRecruitData(element)
            recruit_list.append(recruit)
        return recruit_list

    #
    # 1求人あたりのデータを取得する
    # @type object singleRecuritObj 1求人
    # @return hash 求人情報
    #
    def getSingleRecruitData(self, singleRecuritObj):
        recuit_info = {}
        recruit_id_tmp = singleRecuritObj.select_one(".c-job_offer-box__header__title__link").attrs["href"]
        #print(recruit_id_tmp)
        recruit_id = recruit_id_tmp.split("/")[3]
        company_name = singleRecuritObj.select_one(".c-job_offer-recruiter__name a").text
        salary_text = singleRecuritObj.select_one(".c-job_offer-detail__salary").text
        salary_tmp = salary_text.split("〜")
        low_salary  = int(salary_tmp[0].replace("万", "").replace(',','').strip())
        high_salary = int(salary_tmp[1].replace("万円", "").replace(',','').strip())
        skill_arr = self.getSkillData(singleRecuritObj)

        recuit_info = {
            'id':recruit_id,
            'name':company_name,
            'low_salary':low_salary,
            'high_salary':high_salary,
            'skill':skill_arr
        }
        return recuit_info


    #
    # 技術の取得
    # @type object getSingleRecruitData 求人情報
    # @return arr 言語情報
    #
    def getSkillData(self, singleRecuritObj):
        skillele = singleRecuritObj.select(".c-job_offer-detail__description .lang_tag a")
        skill_arr = []
        skill_str = ''
        for skill in skillele:
            skill = skill.text
            if skill is not None and skill != "":
                skill_arr.append(skill)
        skill_str = ' '.join(skill_arr)
        return skill_str
