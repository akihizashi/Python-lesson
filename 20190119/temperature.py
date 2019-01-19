from sklearn.linear_model import LinearRegression
import  pandas,numpy
import matplotlib.pyplot as plt

temperature = pandas.read_csv('./csv/temperature.csv', encoding="utf-8")
# print(temperature)

target_year = 2014
train_year = temperature[temperature.year != target_year]
# print(train_year)
test_year = temperature[temperature.year == target_year]

interval = 6
def make_data(data):
    x = []
    y = []
    temps = list(data['temperature'])
    # print(temps)
    # exit()
    for i in range(len(temps)):
        if i < interval:
            continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p -interval
            #６個結果group
            xa.append(temps[d])
        # 6個のgroup->xの中にまとめ
        # print(xa)
        # exit()
        x.append(xa)
    #print(x)
    #print(y)
    #print(x)
    #print(y)
    return (x,y)

train_data, train_label = make_data(train_year)
test_data, test_label = make_data(test_year)

lr = LinearRegression(normalize=True)
#学習させる
lr.fit(train_data, train_label)
#予想させる
predict_label = lr.predict(test_data)
#graphの見た目設定
plt.figure(figsize=(10,6), dpi=100)
#実際のデータのLine
plt.plot(test_label, c='r')
#予想のデータのLine
plt.plot(predict_label, c='b')

plt.show()
