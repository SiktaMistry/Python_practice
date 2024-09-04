from math import factorial


num=int(raw_input("Enter the number:"))
fact = 1
if(num==0 or num==1):
    fact=1
else:  
    for i in range(1,num+1):
        fact *= i
print("The factorial of "+str(num)+" is "+str(fact))        