#モジュール内のクラスを直接読み込む
from plain_class import SampleUser

sampleUser = SampleUser('山田太郎')
sampleUser.setAge(32)
sampleUser.setLanguage('Python')
sampleUser.showProfile()
