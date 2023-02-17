class Base():
    def __init__(self):
        self.n1=int(input("Enter the Number 1:"))
class Base_A(Base):
    def _init_(self):
        Base.__init__(self)
        self.n2=int(input("Enter the Number 2:"))
class Base_B():
    def __init__(self):
        self.n3=int(input("Enter the Number 3:"))

class largestBase(Base_A,Base_B):
    def __init__(self):
        Base_A.__init__(self)
        Base_B.__init__(self)
        if self.n1 > self.n2 and self.n1 > self.n3:
            print("Greatest Element is in Class Base:",self.n1)
        elif self.n2 > self.n1 and self.n2 > self.n3:
            print("Greatest Element is in Class Base_A:",self.n2)
        else:
            print("Greatest Element is in Class Base_B:", self.n3)

obj01=largestBase()