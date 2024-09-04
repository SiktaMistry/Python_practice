f = open("poem.txt","r")
text = f.read()
print(text.find("Twinkle"))
f.close()