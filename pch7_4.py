num = int(raw_input("Enter a number: "))
temp = 0
if(num==0 or num==1):
    temp = 1
for i in range(2,int((num/2)+1)):
    if(num%i==0):
        temp = 1
if(temp==1):
    print("The number is not a Prime Number")
else:
    print("The number is a Prime Number")            
