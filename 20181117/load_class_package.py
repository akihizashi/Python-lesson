#パッケージ内を呼び出す
from sample_dir.plain_class import SampleUser

sampleUser = SampleUser("山田太郎")
sampleUser.setAge(32)
sampleUser.setLanguage('Python')
sampleUser.showProfile()
