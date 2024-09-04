class C_2dvector:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __str__(self):
        return self.x,"i + "+str(self.y)+" j"

class C_3dvector(C_2dvector):
    def __init__(self, x, y, z):
        super(self,C_3dvector).__init__(x, y)
        self.z = z
    def __str__(self):
        return self.x,"i + "+str(self.y)+"j + "+str(self.z)+"k" 
v2d = C_2dvector(1,3)
v3d = C_3dvector(1,9,7)
print(v2d)
print(v3d)