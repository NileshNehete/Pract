# Setting up the sys.path where all Modules are written for import
import sys
sys.path.append("C:\Python_Pro\Modules")
#print sys.path
from calmodule_print import *
inNum1= input("Input first number: ")
inNum2= input("Input second number: ")

while (ITERATOR == 0):
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division \n5. Exit")
    choice = input("Enter Operatration: ")
    if( choice == 1 ):
        add(inNum1,inNum2)
    elif( choice == 2 ):
        sub(inNum1,inNum2)
    elif( choice == 3 ):
        mult(inNum1,inNum2)
    elif( choice == 4 ):
        divi(inNum1,inNum2)
    else:
        print ("Opps!! Wrong choice. Bye.....")
        break
    #ITERATOR = ITERATOR + 1
    

