list1=[1,2,3,4,5,6]
list2=[7,8,9,1,2,3]
print(list1)
print(list2)
a=len(list1)
b=len(list2)
if a==b:
    print("Length of the list is same")
else:
    print("Length of the list is not same")
sum1=sum(list1)
sum2=sum(list2)
if(sum1==sum2):
    print("Sum of the list is equal")
else:
    print("sum of the list is not equal")
print("Common Elements:")
for i in list1:
    for j in list2:
        if(i==j):
            print(i)




