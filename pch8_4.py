
def sum(n):
    if(n>=1):
        return n + sum(n-1)
    else:
        return n


n = int(raw_input("Enter the number of natural numbers"))
print("The sum of "+str(n)+" is "+str(sum(n)))