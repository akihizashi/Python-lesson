import csv

print ("1-1")
#読み込んで表示
csv_file = open("kadai_02_sample.csv", "r", encoding="utf-8")
for row in csv.reader(csv_file):
    print(row)
csv_file.close()


print ("1-2")
#読み込んで表示
csv_file2 = open("kadai_02_sample.csv", "r", encoding="utf-8")
totalList = []
counter = 0
for row in csv.reader(csv_file2):
    counter+=1
    if counter == 1:
        headList=[]
        #まずヘッダだけのリスト
        for i in range(len(row)):
            headList.append(row[i])
    else:
        dict1 = {}
        #ヘッダのリストを作る
        for i in range(len(row)):
            header = headList[i]
            val = row[i]
            dict1[header] = val
            totalList.append(dict1)
csv_file2.close()
print(totalList)

print ("1-3")
#読み込んで表示
csv_file3 = open("kadai_02_sample.csv", "r", encoding="utf-8")
counter3 = 0
for row in csv.reader(csv_file3):
    counter3 +=1
    if counter3 > 1:
        if int(row[1]) < 20:
             print(row[0] + "さんは未成年なのでまだお酒は飲めません。")
        else:
             print(row[0] + "さんは飲み過ぎには注意しましょう。")
csv_file3.close()


print ("1-4")
#読み込んで表示
csv_file4 = open("kadai_02_sample.csv", "r", encoding="utf-8")
counter4 = 0
man_cnt = 0
man_age = 0
woman_cnt = 0
woman_age = 0
for row in csv.reader(csv_file4):
    counter4 +=1
    if counter4 > 1:
        if row[2] == "男":
            man_cnt += 1
            man_age += int(row[1])
        else:
            woman_cnt += 1
            woman_age += int(row[1])
print("男性:" + str(man_cnt) + "人　平均" + str(round(man_age/man_cnt, 1)) + "才" )
print("女性:" + str(woman_cnt) + "人　平均" + str(round(woman_age/woman_cnt, 1)) + "才" )
csv_file4.close()
