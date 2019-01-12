
#文字の出力
print ("No.1")

print ("Hello  world!")

#変数の代入+文字の結合
print ("No.2")

a = "College"
b = "Business"
c = "Communication"

print (a + " " + b + " " + c)

#変数の代入+足し算
print ("No.3")

a = 10
b = a + 5

print (b)

#変数の代入+足し算
print ("No.3")

a = 10
b = a + 5

print (b)

#掛け算 + 整数型
print ("No.4")

TAX = 1.08
original_price = 2000

print (int(original_price * TAX))
#参考
#print (original_price * TAX)
#print (float(original_price * TAX))

#if
print ("No.5")

score = 70
if score >= 80:
    print("congratulation")
elif score >= 60:
    print("OK")
else:
    print("Don't mind")

#ifの空白
print ("No.6")

sample_id = ""
sample_name = ""
if sample_id != "" and sample_name!= "":
    print("OKです。")
else:
    print("未入力があります。")

#リストの定義
print ("No.7")

arr = ['aaa','bbb','ccc']
print(arr[1])

#for文
print ("No.8")

val = 0
for v in range(10):
    val += 1
print(val)

#date
print ("No.9")

import datetime
print(datetime.datetime.today().strftime("%Y年%m月%d日%H時%M分"))
#https://qiita.com/motoki1990/items/8275dbe02d5fd5fa6d2d

#文字分割
print ("No.10")

str = "apple,orange,peach"
sample_list = str.split(",")
print(sample_list)

#正規表現
print ("No.11")
import re

if re.compile("\d7").search("1234567"):
    print("OK")
else:
    print("NG")

#for+if
print ("No.12")
for v in range(1,11):
    print(v)
    if v %3 == 0:
        print("3の倍数です。")

#全結合
print ("No.13")
val = 0
for v in range(1,101):
    val += v
print(val)
