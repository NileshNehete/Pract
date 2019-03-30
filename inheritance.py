##This is a Inheritance example with child class does not have parameteres.
##Hence pass is mentioned.

class person:
    def __init__(person,fname,lname):
        person.fname = fname
        person.lname = lname

    def printname(self):

        print("Hello! "+self.fname+" "+self.lname)

class student(person):
    pass

    


def funCall():
    p1 = person('Nilesh','Nehete')
    p2 = student('Yushan','Nehete')
    p1.printname()
    p2.printname()


if __name__ == '__main__':
    funCall()
