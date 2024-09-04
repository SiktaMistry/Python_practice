def convert(a):
    b = (a*1.8) +32
    return b
    
cel = int(raw_input("Enter the celsius temperature: "))
print("The fahrenheit temperature is:"+str(convert(cel)))