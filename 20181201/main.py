from regist.regist import Regist
from utillib.dbutil import Dbutil
from convert.getfile import GetFile
#import convert.getfile as getfile

#求人データの登録
url = "https://paiza.jp/career/job_offers"

getfileObj = GetFile(url)
recruits = getfileObj.getContents()
#DBデータの登録
db = Dbutil('localhost', 'root', 'python_sample', 'password')
reg = Regist(db)
reg.registData(recruits)
