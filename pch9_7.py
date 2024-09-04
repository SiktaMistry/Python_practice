content = True
f = open("log1.txt","r")
i = 1
while content:
    content = f.readline()
    if "python" in content.lower():
        print(content)
        print("Python is present on line number",i)
    i+=1