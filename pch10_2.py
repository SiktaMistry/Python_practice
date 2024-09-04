class calculator:
    def __init__(self,num):
        self.number = num
    def square(self):
        print("The value of "+str(self.number)+"square is ",self.number **2)
    def cube(self):
         print("The value of "+str(self.number)+"cube is ",self.number **3)
    def squareroot(self):
         print("The value of "+str(self.number)+"squareroot is ",self.number **0.5)

num = int(raw_input("Enter the number: "))
a = calculator(num)
a.square()
a.cube()
a.squareroot()

