words = ['dog', 'cow', 'donkey', 'shit']
f1 = open('lists_bad.txt','r')
text = f1.read()
for word in words:
    text = text.replace(word,"******")
    f2 = open("lists_bad.txt","w")
    f2.write(text)
f1.close()
f2.close()
