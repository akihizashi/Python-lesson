print("大問1")

print("----------1----------")
print ("Hello Colleage of Business and Communication!")

print("----------2----------")
n = 10
print((n+5)*100)

print("----------3----------")

math = 90
english = 90
if math >= 80 and english >= 80:
    print("大変優秀です。")
elif (math >=80 and english < 80 ) or (math < 80 and english >= 80):
    print ("もう片方の教科も頑張りましょう。")
else:
    print("もう少し頑張りましょう。")
#下記の書き方でも可
if math >= 80 and english >= 80:
    print("大変優秀です。")
elif math >=80 or english >= 80:
    print ("もう片方の教科も頑張りましょう。")
else:
    print("もう少し頑張りましょう。")


print("----------4----------")
user_id = "hogehoge"
password = "sample_pass"
if user_id =="" and password == "":
    print("入力が不完全です。")
elif (user_id == "" and password != ""):
    print ("ユーザーIDが入力されていません。")
elif (user_id != "" and password == ""):
    print ("パスワードが入力されていません。")
else:
    print("問題ありません。")

#以下のコードでも可
if user_id =="" and password == "":
    print("入力が不完全です。")
elif user_id == "":
    print ("ユーザーIDが入力されていません。")
elif password == "":
    print ("パスワードが入力されていません。")
else:
    print("問題ありません。")


print("----------5----------")
for i in range(1, 21):
    print(i)
    if i % 5 == 0:
        print("5の倍数です。")

print("----------6----------")

str = "aaa,bbb,ccc"
tmp_list = str.split(",")
for s in tmp_list:
    print(s)

print("----------7----------")
import re
tel = "0123-456-789"
#tel = "0123456789"
#tel = "012345-78-9"
#tel = "０１２３４-456-789"
if re.compile("^[0-9]{1,5}-[0-9]{1,5}-[0-9]{1,5}$").search(tel):
    print("OK")
else:
    print("NG")
