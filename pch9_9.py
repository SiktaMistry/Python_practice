f1 = open("match1.txt","r")
f2 = open("match2.txt","r")
text1 = f1.read()
text2 = f2.read()
if(text1==text2):
    print("The two files are identical")
else:
    print("The two files are unidentical")
    f1.close()
    f2.close()