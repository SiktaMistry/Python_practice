num1 = int(raw_input("Enter the number 1 :"))
num2 = int(raw_input("Enter the number 2 :"))
num3 = int(raw_input("Enter the number 3 :"))
num4 = int(raw_input("Enter the number 4 :"))

if(num1>num4):
    f1 = num1
else:
    f1 = num4
if(num2>num3):
    f2 = num2
else:
    f2 = num3
if(f1>f2):               
    print(f1,"is the greatest number")
else:
    print(f2,"is the greatest number")    