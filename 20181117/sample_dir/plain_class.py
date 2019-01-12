#読み込まれる側のクラス
#これをモジュールと定義
class SampleUser:
    # コンストラクタ
    # 起動時に呼び出される関数
    def __init__(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age

    def setLanguage(self, language):
        self.language = language

    def showProfile(self):
        print("my name is " + self.name + " " + str(self.age) +" years old")
        print("my language is " + self.language)
