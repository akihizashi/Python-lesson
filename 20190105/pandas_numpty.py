import pandas as pd
import numpy as np
import copy

print('------行列型のデータ------')

a = pd.DataFrame([
    [10,20,30],
    [40,50,60],
    [70,80,90]
])

print(a)

print('------ベクトル型のデータ------')

b = pd.Series([1.0,3.0,5.0,7.0])

print(b)

print('------辞書型+配列------')

wtbl = pd.DataFrame({
    "weight":[80.0, 70.4, 65.5, 45.9, 51.2],
    "height":[170, 180, 155, 143, 154],
    "type":["f", "n", "n", "t", "t"]
})

print(wtbl);

print(wtbl['weight']);

print(wtbl[['height',"weight"]]);

print("----比較　通常のdict+arr------")
sampleData = {
    "weight":[80.0, 70.4, 65.5, 45.9, 51.2],
    "height":[170, 180, 155, 143, 154],
    "type":["f", "n", "n", "t", "t"]
}
print(sampleData)

print("----0から数えて1以上4未満まで------")
print(wtbl[1:4])

print("----0から数えて3以上4全て------")
print(wtbl[3:])

print("----height 170以上------")
print(wtbl[wtbl.height >=170])

print("----type n------")
print(wtbl[wtbl.type =="n"])

print("----heightでsort------")
wtbl2 = wtbl.sort_values(by="height")
print(wtbl2)

print("----まとめて割り算------")
wtbl3 = copy.copy(wtbl)
wtbl3["height"] = wtbl["height"]/200
print(wtbl3)

print("----最大値------")
max_height = wtbl["height"].max()
print(max_height)

print("----連番で数字を作成------")
v = np.arange(10, dtype=np.uint64)
print(v)

print("----一律に3倍------")
v = v * 3
print(v)

print("----平均値------")
print(v.mean())
