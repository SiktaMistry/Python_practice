def convert(a):
    return a*2.54
    
inch = int(raw_input("Enter the inch value: "))
print(inch," inch = " + str(convert(inch))+" cms")