a=int(input("Enter the limit:"))
for i in range(a):
    for j in range(i):
        print ('*',end=" ")
    print('')
for i in range(a,0,-1):
    for j in range(i):
        print('*',end=" ")
    print('')