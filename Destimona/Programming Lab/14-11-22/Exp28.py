def factor(num):
    for i in range(1,num+1):
        if(num%i==0):
            print(i)
num=int(input("Enter the number:"))
print("Factor of the number is:")
factor(num)