import mysql.connector
import time

class Database:

    connect = mysql.connector.connect(
        host='localhost',
        port='3306',
        db='python',
        user='root',
        password='',
        # charset='utf8'
    )

    def __init__(self):
        # print('ok')
        # exit()
        self.db = self.connect.cursor(dictionary=True, buffered=True)


    def insertLog(self, sql, data):
        # sql = 'insert into chat_logs(theme, log) values (%s, %s)',(theme, log)
        # print(sql)
        # exit()
        try:
            self.db.execute(sql, data)
            self.connect.commit()
            time.sleep(2)
            print('I saved this conversation to data')
        except mysql.connector.Error as error :
            self.connect.rollback()
            print('Sorry, I can\'t save conversation')
            # print("Failed to insert into MySQL table {}".format(error))
        # finally:
        # #closing database connection.
        #     if (self.connect.is_connected()):
        #         self.db.close()
        #         self.connect.close()
                # print("MySQL connection is closed")
            
    
    def selectLog(self, sql):
        self.db.execute(sql)
        return self.db.fetchall()

# database = Database()

# print(database.insertLog('1', '2'))
# exit()
# theme = 'test theme'
# log = 'test log'
# sql = 'select * from chat_logs'
# sql2 = """ INSERT INTO `chat_logs`
#                           (`theme`, `log`) VALUES (%s,%s)"""
# data = (theme, log)
# data = database.selectLog(sql)
# print(data)
# exit()
# database.insertLog(sql2, data)



    

