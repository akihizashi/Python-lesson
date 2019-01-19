from sklearn.linear_model import LinearRegression
import  pandas,numpy
import matplotlib.pyplot as plt

temperature = pandas.read_csv('./csv/temperature.csv', encoding="utf-8")
print(temperature)

target_year = 2014
train_year = temperature[temperature.year != target_year]
print(train_year)
test_year = temperature[temperature.year == target_year]

interval = 6
def make_data(data):
    x = []
    y = []
    temps = list(data['temperature'])
    for i in range(len(temps)):
        if i <= interval:
            continue
        y.append(temps[i])
        xa = []
        for p in range(interval):
            d = i + p -interval
            xa.append(temps[d])
        x.append(xa)
    #print(x)
    #print(y)
    #print(x)
    #print(y)
    return (x,y)

train_data, train_label = make_data(train_year)
test_data, test_label = make_data(test_year)

lr = LinearRegression(normalize=True)
lr.fit(train_data, train_label)

predict_label = lr.predict(test_data)

plt.figure(figsize=(10,6), dpi=100)
plt.plot(test_label, c='r')
plt.plot(predict_label, c='b')

plt.show()
