import csv
from user import SampleUser

csv_file = open("file_import_student.csv", "r", encoding="utf-8")
totalList = []
counter = 0

for row in csv.reader(csv_file):
    counter += 1
    if counter > 1:
        print("-------------------------------")
        user = SampleUser(row[0],row[1],row[2])
        user.showProfile()
csv_file.close()
