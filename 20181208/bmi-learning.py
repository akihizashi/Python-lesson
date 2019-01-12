##
## 教師あり学習　ラベリング
##
##
from sklearn.model_selection import train_test_split
from sklearn import svm, metrics
import pandas as pd
import os;

csv_dir = os.path.dirname(os.path.abspath(__name__))
csv_path = os.path.join(csv_dir, 'csv/bmi_1000.csv')
tbl = pd.read_csv(csv_path)
label = tbl["label"]
w = tbl["weight"]/100
h = tbl["height"]/190

#横方向に結合する
wh = pd.concat([w,h], axis=1)

#print(label)
#print(w)
#print(h)
#print(wh)

data_train, data_test, label_train, label_test = train_test_split(wh,label)

#print(data_train)
#print(label_train)

#print(data_test)
#print(label_test)

clf = svm.SVC()
#学習!!
clf.fit(data_train,label_train)

#予測
predict = clf.predict(data_test)
#print(predict)

#答えあわせ
#数値のみ
score = metrics.accuracy_score(label_test, predict)
#詳細レポート

print(score)
