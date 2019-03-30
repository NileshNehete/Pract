####This is a Inheritance example with child class does have parameteres.
####Hence pass is is mentioned.
##
##When you add the __init__() funcion, the child class will no longer inherit the parent's __init__() function.
##The child's __init__() function overrides the inheritance of the parent's __init__() function.


class person:
    def __init__(person,fname,lname):
        person.fname = fname
        person.lname = lname

    def printname(self):

        print("Hello! "+self.fname+" "+self.lname)

class student(person):
    def __init__(stud,fname,lname,roll_no):
        person.__init__(stud,fname,lname)
        stud.roll_number = roll_no

    def display_info(stud):
        print("Welcome %s %s has roll number as %d" %(stud.fname,stud.lname,stud.roll_number))
           

def funCall():
    p1 = person('Nilesh','Nehete')
    p2 = student('Yushan','Nehete',32)
    p1.printname()
    p2.printname()
    p2.display_info()

if __name__ == '__main__':
    funCall()
