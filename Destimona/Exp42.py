import csv
with open("dep.csv",newline='') as f:
    d=csv.DictReader(f)
    print("Magnitude Subject")
    for i in d:
        print(i['Magnitude'],i['Subject'])