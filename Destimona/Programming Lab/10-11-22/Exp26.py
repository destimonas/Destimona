a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
gcd=1
for i in range(1,max(a,b)):
    if a%i==0 and b%i==0:
        gcd=i
print("GCD of two number is:",gcd)

