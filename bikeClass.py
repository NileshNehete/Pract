class Bike:
    def __init__(bike, model, make, company):

        bike.model = model
        bike.make = make
        bike.company = company


    def display(bike):
        #print ("You like bike "+bike.model+" made in "+str(bike.make)+" by company "+bike.company+" .")
        print( bike.model)
        print( bike.make)
        print( bike.company)

'''
class Bike_Price(Bike):
    def __init__(price,model):
        price.model = model

    def displayPrice(price, model):
        if(price.model == bike.model):
            print ("Price of "+bike.model+" is Rs 70000")
        elif( bike.model == 'Splendor'):
            print ("Price of "+bike.model+" is Rs 50000")
        else:
            print ("Price is not in catalogue")

'''

def bikeCall():

    myBike = Bike('Discover',2004,'Bajaj')
    myBike.display() 

if __name__ == '__main__':
    bikeCall()

    
