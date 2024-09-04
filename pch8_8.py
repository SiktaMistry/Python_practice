def table(n):
    for i in range(0,11):
        print(n," x "+str(i)+" = "+str(n*i))
        
n = int(raw_input("Enter the number: "))
table(n)