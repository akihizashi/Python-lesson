print("大問2")

import csv

csv_file = open("support02_data.csv", "r", encoding="utf-8")
totalList = []
counter = 0

fruit_count = 0
drink_count = 0
fruit_sum = 0
drink_sum = 0
for row in csv.reader(csv_file):
    counter += 1
    if counter > 1:
        if row[1] == '果物':
            fruit_count += 1
            fruit_sum   += int(row[2])
        elif row[1] == '飲料':
            drink_count += 1
            drink_sum   += int(row[2])
csv_file.close()

print ("果物" + str(fruit_count) + "個  " + str(fruit_sum) + "円")
print ("飲料" + str(drink_count) + "個  " + str(drink_sum) + "円")
