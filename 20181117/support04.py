print("大問4")

class SampleUser:
    # コンストラクタ
    # 起動時に呼び出される関数
    def __init__(self, name):
        self.name = name

    def setAddress(self, address):
        self.address = address

    def setTel(self, tel):
        self.tel = tel

    def showProfile(self):
        print("私の名前は " + self.name + "で、住所は " + self.address +", 電話番号は " + self.tel + "です。")

sampleUser = SampleUser('山田太郎')
sampleUser.setAddress("東京都")
sampleUser.setTel('0123-456-789')
sampleUser.showProfile()
