#クラス　変数や配列と関数をまとめて扱えるデータ構造
def showProfile(name):
    print("こんにちは" + name + "さん")

#後にかく
showProfile("山田")

#初期値を設定する
def showProfile2(name = "田中"):
    print("こんにちは" + name + "さん")

showProfile2()

showProfile2("鈴木")

#複数の引数
def showProfile3(name, weather):
    print("こんにちは" + name + "さん")
    print("今日の天気は" + name + "ですね")

showProfile3("田中", "晴れ")

#戻り値
def calcIncTaxPrice(price):
    price2 = price * 1.08
    return price2

price = 1000
incprice = calcIncTaxPrice(price)
print(incprice)
#エラー
#print(price2)
