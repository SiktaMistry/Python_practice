class programmer():
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product
    def getInfo(self):
        print("The name of the "+self.company+" programmer is "+self.name+" and the product is "+self.product)

harry = programmer("Harry","Skype")
alka = programmer("alka","Github")
harry.getInfo()
alka.getInfo()
    
