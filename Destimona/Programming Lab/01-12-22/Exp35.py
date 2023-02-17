class bank:
    def __init__(self,accno,name,accty):
        self.accno=accno
        self.name=name
        self.accty=accty
        self.bal=0
    def showamt(self):
        print("Account Holder Name:",self.name)
        print("Account Number:",self.accno)
        print("Account Type:",self.accty)
        print(" Account Balance:",self.bal)
    def dep(self,d1):
        self.bal=self.bal+d1
        return self.bal
    def withd(self,w1):
        self.bal=self.bal-w1
        return self.w1
n=input("Enter Account Holder Name:")
a=int(input("Enter Account Number:"))
t=input("Enter Account Type:")
o=bank(a,n,t)
o.showamt()
d=0
while(True):
    print("Menu")
    print("\n1.Deposit\n2.Withdraw")
    c=int(input("Enter your choice:"))
    if(c==1):
        d=int(input("Enter the amount to deposit:"))
        print("Account Balance:",o.dep(d))
    elif(c==2):
        w=int(input("Enter the Amount to withdraw:"))
        if(w>d):
            print("Balance Amount is:",o.withd(w))
        else:
            print("Insufficient Balance")
    else:
        print("Invalid Choice")
