class calculator:
    def __init__(self,num):
        self.number = num
        self.square = num **2
        self.cube = num **3
        self.squareroot = num **0.5
    def display(self):
        print("square of "+str(self.number)+" = "+str(self.square)+"\nsquareroot of"+str(self.number)+" = "+str(self.squareroot)+"\ncube of "+str(self.number)+" = "+str(self.cube)+" ")
    @staticmethod
    def greet():
        print("Thank you")
num = int(raw_input("Enter the number:"))
a = calculator(num)
a.display()
a.greet()