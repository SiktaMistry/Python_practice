print("Enter the value of n such that n=3*i+1 to see the pattern")
n = int(raw_input("Enter the value of n:"))

for j in range(1,n+1):
    if(j%2!=0):
        print("*"*3)
    else:
       print("* *")        
