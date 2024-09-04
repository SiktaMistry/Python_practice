def pattern(n):
    for n in range(n,0,-1):
        print("*"*n)
        

n = int(raw_input("Enter the number of lines of pattern"))
pattern(n)