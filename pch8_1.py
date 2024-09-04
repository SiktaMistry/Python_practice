def maximum(a, b, c):
    if(a>b):
        f=a
    else:
        f=b
    if(f>c):
        return f
    else:
        return c        
        
a = int(raw_input("Enter the number 1: "))
b = int(raw_input("Enter the number 2: "))
c = int(raw_input("Enter the number 3: "))
print(str(maximum(a,b,c))+"is the greatest number" )