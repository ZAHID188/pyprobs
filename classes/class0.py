# Imagine its a flight booking overflow class
class Flight():
    #remember to put spaces in python . for examples- def __
    def __init__(self,capacit):
        self.capacitys=capacit
        self.passengers=[]

    def add_passenger(self,name):
        #if there're not any open seats
        if not self.open_seats():
            return  False 
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacitys - len(self.passengers)
flight= Flight(2)
people = ["Harry","Ron","Hermoine","zahid","raihan"]
for person in people:
    success= flight.add_passenger(person)
    if success:
        print(f"added {person} to flight succesfully")
    else :
        print(f"No available seats for {person}")