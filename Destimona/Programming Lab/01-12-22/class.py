#single inheritance
"""class animal:
    def speak(self):
        print("Animal speak")
class dog(animal):
    def bark(self):
        print("Dog Barks")
d=dog()
d.speak()
d.bark()

# multiple inheritance
class Mother:
    mothername=""
    def mother(self):
        print(self.mothername)

class Father:
    fathername=""
    def father(self):
        print(self.fathername)

class daughter(Mother,Father):
    def parents(self):
        print("Mother:",self.mothername)
        print("Father:",self.fathername)
d=daughter()
d.mothername="suma"
d.fathername="David"
d.parents()

#multilevel inheritance

class grandfather:
    def __init__(self,gfname):
        self.gfname=gfname

class father(grandfather):
    def __init__(self,fname,gfname):
        self.fname=fname
        grandfather.__init__(self,gfname)
class daughter(father):
    def __init__(self,dname,fname,gfname):
        self.dname=dname
        father.__init__(self,fname,gfname)
    def show(self):
        print("Grand Father Name:",self.gfname)
        print("Father Name:",self.fname)
        print("Daughter Name:",self.dname)

d=daughter("Tesa tijo","Tijo","Titus")
d.show()

#hierarchical
class Mother:
    def mname(self):
        print("Suma")
class daughter1(Mother):
    def dname(self):
        print("I love Mom")
class daughter2(Mother):
    def daname(self):
        print("Miss u mom")
d=daughter1()
d.mname()
d.dname()
d.daname()

#hybrid

class college:
    def study(self):
        print("Amal Jyothi college of Engineering")

class student1(college):
    def sname(self):
        print("Batch A,In MCA")
class student2(college):
    def stname(self):
        print("Batch A,In MCA")

class student3(college):
    def suname(self):
        print("Batch A,In MCA")
o=mca()
o.study()
o.sname()
o.stname()
o.suname()
"""

class animal:
    def sound(self):
        print("Animal makes sound")
class dog(animal):
    def sound(self):
        print("Dog Barks")
o=dog()
o.sound()