str=input("Enter the sting:")
dict={}
count=0
a=str.split()
for i in a:
    if i in dict:
         dict[i]+=1
    else:
        dict[i]=1
        print(a)
for k,v in dict.items():
    print(k,v)




