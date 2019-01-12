##
## 教師あり学習　ラベリング(学習とテストを自力で振り分け)
##
##
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import random,re,os

#独自読み込みからのデータ作成
csv = []
csv_dir = os.path.dirname(os.path.abspath(__name__))
csv_path = os.path.join(csv_dir, 'csv/bmi_1000.csv')
with open( csv_path ,'r', encoding='utf-8') as fp:
    for line in fp:
        line = line.strip()
        cols = line.split(',')
        #print(cols)
        fn = lambda n : float(n) if re.match(r'^[0-9\.]+$', n) else n
        cols = list(map(fn, cols))
        #print(cols)
        csv.append(cols)
del csv[0] 

#ランダムシャッフル
random.shuffle(csv)
#print(csv)
total_len = len(csv)
# print(total_len)
#全体の2/3を学習用に割り当てる
train_len = int(total_len * 2/3)
# print(train_len)
train_data = []
train_label = []
test_data = []
test_label = []
for i in range(total_len):
    data = csv[i][0:2]
    label = csv[i][2]
    if i < train_len:
        train_data.append(data)
        train_label.append(label)
    else:
        test_data.append(data)
        test_label.append(label)
#print(test_data)
#print(test_label)

#print(train_data)
#print(train_label)

#学習
clf = svm.SVC()
clf.fit(train_data,train_label)

#予測
predict = clf.predict(test_data)

#print(predict)

#答えあわせ
#数値のみ
ac_score = metrics.accuracy_score(test_label, predict)
print("正解率=", ac_score)
