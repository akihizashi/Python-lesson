import csv

def showData(str)
    csv_file = open("str", "r", encoding="utf-8")
    for row in csv.reader(csv_file):
        print(row)
    csv_file.close()

showData("data.csv")
