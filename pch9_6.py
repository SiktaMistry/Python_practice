f = open("log1.txt","r")
text = f.read()
if("python" in text.lower()):
    print("python is present")
else:
    print("python is not present")