#変数について
#・アルファベット、数字、アンダースコアを用いて作るのが基本
#例 pythonSchool(キャメルケース) or python_school(スネークケース)のように表記する
#pythonでは一般的にスネークケースで表記する方が一般的。
#
#・冒頭は数字ではなくアルファベットで。
#変数名の開始に、数字は使えないので、先頭の文字は必ずアルファベットに。

#一般的な出力
print ('本日は晴天なり')

#変数クオートかダブルクオートでくくる
var1 = "山田太郎"
print (var1)

#文字列切り出し
var2 = "20180922"
print (var2[0:4])
print (var2[4:6])
print (var2[6:8])

#わかりやすい文字
score = 80
#下記はエラー
#print ("今年のテストは"+ home_run+"点とりたい")
#文字列型にすればOK
print ("今度のテストは"+str(score)+"点とりたい")

num = 5
#0うめ５桁 sprintfのような使い方
print("num: %05d" % num)

#条件分岐はインデントがないと動かない
if score >= 80:
    print ("頑張りましたね")
elif score >= 60:
    print("もう一歩です")
elif score >= 40:
    print("頑張りましょう")
else:
    print("ダメダメです")


var_a = 10;
var_c = 7;

# AND 両方とも
# OR  片方満たせばOK
if (var_a == 10 and var_c == 8):
    print("OK");
else:
    print("NG");

#リスト
arr =["りんご", "かき", "みかん"]
arr2 =["犬", "猫", "うさぎ"]

print('------リストのデバッグ------')
#これだけでデバッグできる
print (arr)

print('------通常のループ------')
for sample_number in range(1,10):
    #1から9まで
    print (sample_number)

for sample_number in range(10):
    #0から9まで
    print (sample_number)

print('------リストのループ------')
#通常のリストのループ
for v in arr:
    print(v)

#長さ
print (len(arr))
#それぞれの要素
print (arr[1])
#リストの結合
arr3 = arr+arr2
print (arr3)

#リストの存在判定 in_array
print('------存在判定------')
print ("りんご" in arr)
print ("りんご" in arr2)

#リストに追加
arr.append("パイナップル")
print(arr)

#タプル
#リストと近いが、要素の変更ができない
print('------タプルのデバッグ------')
tupple_arr = ("Python", "PHP", "Java")
print(tupple_arr)


#文字列の分割・結合
day_str='2011/03/11'
day_arr = day_str.split('/')
print(day_arr)
day_str2 = '-'.join(day_arr)
print(day_str2)

print('------セットのデバッグ------')

#セット(重複を許さないリスト)
arr4 = [1,1,2,2,3]
afterSet = set(arr4)
print(afterSet)

print('------集合に関して------')
#集合はsetでないと扱えない

arr = [1,2,3,4]
arr2 = [3,4,5]
set1 = set(arr)
set2 = set(arr2)

#重複を覗く
print('------集合の合成------')

print(set1|set2)

print('------共通集合------')
#セットの共通
common = set1 & set2
print(common)

print('------共通部分以外の片方に所属している集合------')

#片方のみ
single = set1 ^ set2
print(single)

print('------ 辞書型 ------')

#辞書(dictoionary)
dict1 = {"name":"山田太郎","age":"33"}
dict2 = {"name":"鈴木次郎","age":"44"}
#普通にデバッグできる
dict1
dict2
#keyのみ
print(dict1.keys())
#valueのみ
print(dict1.values())

print('------ ループの出力 ------')
#ループ
for k2,v2 in dict1.items():
    print (k2 +" : "+ v2)

print('------ ループへの追加 ------')
#辞書型リスト
dict_list=[]
dict_list.append(dict1)
dict_list.append(dict2)
dict_list

#ループ+条件分岐
for dict_data in dict_list:
    if int(dict_data["age"]) > 40:
        print("40才以上のメンバーです。")
        dict_data

print("------- メソッド -------")
#メソッド
def hello():
    print('本日は晴天なり')

#メソッドは呼び出し前に定義しておかないと呼べない
hello()

def animalcry(name, bow="wanwan"):
  print("%sの鳴き声は%s" % (name, bow))

animalcry("猫","ニャーニャー")

animalcry("犬")

def animalcry2(name, bow="wanwan"):
  str = "%sの鳴き声は%s" % (name, bow)
  return str

str = animalcry2("猫","ニャーニャー")
print(str)
