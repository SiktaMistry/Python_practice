class train:
    def __init__(self,name,seats,fare):
        self.name = name
        self.seats = seats
        self.fare = fare
    def ticket(self):
        if(self.seats>0):
            print("Your ticket have been booked! Your seat number is "+str(self.seats)+" ")
        else:
            print("Sorry this train is full")
    def status(self):
        print("The name of the train is "+self.name+" ")
        print("The number of seats is "+str(self.seats)+" ")
    def fareinfo(self):
        print("The fare of the train is Rs "+str(self.fare)+" ")

a = train("CKP Express: 14031", 90, 300)
a.status()
a.fareinfo()
a.ticket()
