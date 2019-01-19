import numpy as np
import matplotlib.pyplot as plt
import os
import codecs 

#学習データ
#学習データ
csv_dir = os.path.dirname(os.path.abspath(__name__))
csv_path = os.path.join(csv_dir, './csv/bmi_no_label.csv')
filecp = codecs.open(csv_path ,encoding= "utf-8")
train = np.loadtxt(filecp, delimiter=",", skiprows=1)

train_x = train[:,0]
train_y = train[:,1]

#print(train_x)
#print(train_y)

plt.plot(train_x, train_y, 'o')
plt.show()
