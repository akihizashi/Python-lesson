import mysql.connector


#passwordは下記サイトで記号まで含めて８文字以上
#http://www.luft.co.jp/cgi/randam.php
#


#GRANT ALL PRIVILEGES ON person_db.* TO person_user@localhost IDENTIFIED BY 'JYVVHr9)/B5c' WITH GRANT OPTION;
#insert into person(name,age,language) values
#('yamada',19,'PHP'),
#('suzuki',22,'Java'),
#('tanaka',18,'Ruby'),
#('watanabe',25,'C'),
#('satou',33,'Perl');


#チュートリアル
#https://algorithm.joho.info/programming/python/mysql-connector-python-install/
#コマンドラインで下記を実行
#pip install mysql-connector-python

#実際のソース
#https://algorithm.joho.info/programming/python/mysql-connector-get-data/
#


cnt = mysql.connector.connect(
    host='localhost',
    port='3306',
    db='person_db',
    user='person_user',
    password='JYVVHr9)/B5c',
    charset='utf8'
)

# カーソル取得
db = cnt.cursor(dictionary=True, buffered=True)

sql = 'SELECT id,name,age,language FROM person';
db.execute(sql)

#問1
# 表示
results = db.fetchall()
data = []
for row in results:
    print(str(row['id']) + ":" + row['name'] + ":" + str(row['age']) + ":" + row['language'])

#問2
sql2 = " insert into person (name, age, language) values ('katou', 27, 'Python')";
db.execute(sql2)
cnt.commit()

#問3
sql3 = " update person set age = 25 where id = 2";
db.execute(sql3)
cnt.commit()

#問4
#回答1
sql4_1 = 'SELECT id,name,age,language FROM person';
db.execute(sql4_1)
results4 = db.fetchall()

loop_cnt = 0
age_sum = 0
for row4 in results4:
    loop_cnt += 1
    age_sum += row4['age']

print(round(age_sum/loop_cnt, 1))

#回答2
sql4_2 = " select AVG(age) AS age_average from person";
db.execute(sql4_2)
person = db.fetchone()
print(person['age_average'])

#問5
sql5 = " delete from person where age >= 20";
db.execute(sql5)
cnt.commit()


# カーソル終了
db.close()
# MySQL切断
cnt.close()
