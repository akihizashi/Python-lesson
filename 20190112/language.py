from sklearn import svm, metrics
import glob, os.path, re, json

def check_freq(fname):
    name = os.path.basename(fname)
    # print(name)
    # exit()
    #ファイル名の頭2文字を取得
    #print(name)
    #groupで取り出し
    lang = re.match(r'^[a-z]{2,}', name).group()
    #print(lang)
    #exit()
    #文章を出力
    with open(fname, "r", encoding="utf-8") as f:
        text = f.read()
    #小文字に統一
    text = text.lower()
    #print(text)
    #exit()
    cnt = []
    for n in range(0,26):
        cnt.append(0)
    # cnt 26個分の配列を作成[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #print(cnt)
    #exit()
    #https://python.civic-apps.com/char-ord/
    code_a = ord("a") #97 ユニコードポイント#アッシュ―キ
    code_z = ord("z") #122
    #print(code_a)
    #print(code_z)
    #exit()
    for ch in text:
        #文字を１文字ずつ区切りユニコードポイントに痴漢
        #print(ch)
        n = ord(ch)
        #print(n)
        if code_a <= n <= code_z:
            #a〜zが１回出現するごとに+1する
            #ex b=98 98-97=1
            cnt[n - code_a] += 1
    total = sum(cnt)
    freq = list(map(lambda n :n / total, cnt ))
    #アルファベットごとの頻度を分数で出す
    #print(freq)
    #exit()

    return (freq, lang)

def load_files(path):
    freqs = []
    labels = []
    #ファイルリストの出力
    file_list = glob.glob(path)
    # print(file_list)
    # exit()
    for fname in file_list:
        # print(fname)
        # exit()
        #言語ごとの頻度分布を出力
        r = check_freq(fname)
        # print(r)
        # exit()
        freqs.append(r[0])
        #en:英語, fr:フランス語、id インドネシア語、tl タガログ語、
        labels.append(r[1])
    return {"freqs":freqs, "labels": labels}

data = load_files("lang/train/*.txt")
# print(data)
# exit()
test = load_files("lang/test/*.txt")
# print(test)
# exit()
clf = svm.SVC()
# print(clf.fit())

clf.fit(data["freqs"], data["labels"])
exit()
predict = clf.predict(test["freqs"])

ac_score = metrics.accuracy_score(test["labels"], predict)

print("正解率=", ac_score)
