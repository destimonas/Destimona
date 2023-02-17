class myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print("sum:",self.y+self.x)
        print("substraction:",self.x-self.y)
        print("Division:",self.x/self.y)
        print("multiplication:",self.x*self.y)
p=myclass(9,8)
print(myclass)
p.show()