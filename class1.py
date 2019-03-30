class myClass():
    def method1(self):
        print ("Base Class Method 1.")

class childClass(myClass):
    def method1(self):
        myClass.method1(self) #You can access a method of the parent class using the syntax
        print ("Child Class Method 1.")

    def method2(self):
        print("Child class method 2.")

def main():

    c2 = childClass()
    c2.method1()
    c2.method2()

if __name__ == '__main__':
    main()
