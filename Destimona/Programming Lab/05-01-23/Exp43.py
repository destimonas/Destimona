import csv
c_col=['ID','Name','Age']
dict_data=[{'ID':1,'Name':'Dickson','Age':22},
            {'ID':2,'Name':'Anu','Age':25},
            {'ID':3,'Name':'Aparna','Age':22},
            {'ID':4,'Name':'Ajanya','Age':18},
            {'ID':5,'Name':'linju','Age':19},
            {'ID':6,'Name':'Minnu','Age':15},
            {'ID':7,'Name':'Tiffy','Age':14},
            {'ID':8,'Name':'Cathu','Age':9},
            {'ID':9,'Name':'Sona','Age':21},
            {'ID':10,'Name':'Tijo','Age':22},]
try:
    with open("name.csv","w") as f:
        write=csv.DictWriter(f,fieldnames=c_col)
        write.writeheader()
        for i in dict_data:
            write.writerow(i)
except IOError:
    print("Input/Output Error")
d=csv.DictReader(open("name.csv"))
print("CSV file output is:")
for i in d:
    print(i)
