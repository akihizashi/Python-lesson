import numpy as np
import matplotlib.pyplot as plt
import os
import codecs

csv_dir = os.path.dirname(os.path.abspath(__name__))
csv_path = os.path.join(csv_dir, './csv/bmi_no_label.csv')
#学習データ
csv_path = os.path.join(csv_dir, './csv/bmi_no_label.csv')
filecp = codecs.open(csv_path ,encoding= "utf-8")
train = np.loadtxt(filecp, delimiter=",", skiprows=1)

#1列名を縦にとる
train_x = train[:,0]
#2列名を縦にとる
train_y = train[:,1]

#print(train_x)
#print(train_y)

plt.plot(train_x, train_y,'o')
#1次式で式のさくせい
res = np.polyfit(train_x, train_y, 1)
print("----- 係数の決定 ---")
print(res)
#[  1.01900816 103.45067088]
print("----- 関数式の決定 ---")
funcSample = np.poly1d(res)
print(funcSample)
#1.019 x + 103.5
print("----- 値の代入 ---")
print(funcSample(10))
#1.019 * 10  + 103.5 113.64075243357006
print("----- 配列の代入 ---")
print(funcSample([10,20]))
#[113.64075243 123.83083399]

plt.plot(train_x, funcSample(train_x), label ='d-1')
plt.show()
