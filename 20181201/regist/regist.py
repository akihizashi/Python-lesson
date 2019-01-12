import utillib.dbutil as dbutil

class Regist():

    def __init__(self,db):
        self.db = db

    #
    # データの登録
    # @type arr recruits 求人データ
    #
    def registData(self, recruits):
        self.db.bulk_insert('recruit', recruits)
        self.db.close()
