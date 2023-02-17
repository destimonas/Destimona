x=int(input("Enter the start  year:"))
y=int(input("Enter the End  year:"))
print("The following are the leap year:")
for i in range(x,y):
    if((i%400==0) or((i%100!=0) and (i%4==0))):
        print(i)


