import mysql.connector

#
# データベースへの接続
#
class Dbutil():

    def __init__(self, host, user, dbname, passwd):
        self.host = host
        self.user = user
        self.dbname = dbname
        self.passwd = passwd


        self.cnt = mysql.connector.connect(
            host = self.host,
            port='3306',
            db= self.dbname,
            user= self.user,
            password= self.passwd,
            charset='utf8'
        )

        if self.cnt is not None:
            self.db = self.cnt.cursor(dictionary=True, buffered=True)

    #
    # dbを閉じる
    #
    def close(self):
        self.db.close()
        self.cnt.close()

    #
    # bulk_insert
    # @type string talbe テーブル名
    # @type dict dict 辞書型データ
    # @return int 影響された行数
    #
    def bulk_insert(self, table, dictlists):
        columns = []
        prepears = []

        single_dict = dictlists[0]
        columns = single_dict.keys()
        column_str = ','.join(columns)
        tmp_prepears = []
        bind_vals =[]

        for dicts in dictlists:
            tmp_val = dicts.values()
            bind_vals.extend(tmp_val)
            #配列初期化
            tmp_prepears = ["%s"] * len(tmp_val)
            tmp_prepears_str = ",".join(tmp_prepears)
            prepears.append("(" + tmp_prepears_str + ")")

        prepear_str = ",".join(prepears)
        sql  =" INSERT INTO %s (%s) VALUES %s " % (table, column_str, prepear_str)
        res = self.db.execute(sql, bind_vals)
        self.cnt.commit()
        return res
