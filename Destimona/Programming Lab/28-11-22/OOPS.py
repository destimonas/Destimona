class myclass:
    x=5
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def show(self):
        print(self.y+self.x)
p=myclass(9,8)
print(myclass)
p.show()

class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname

    def printname(self):
        print(self.fname,self.lname)

    class student(Person):
        pass

    x=student("sona","sona")
    x.printname()