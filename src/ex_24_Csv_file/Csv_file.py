# CSV - Comma Separated File
import csv

with open("../ex_25_Pandas/TestData1.csv") as csvfile:
    reader = csv.reader(csvfile)
    # to print columns
    for col in reader:
        print(col[0], col[1], sep="|")
