f1 = open("Hiscore.txt","r")
previous_Highscore = f1.read()
print(previous_Highscore)
new_Highscore = raw_input("Enter the new highscore")
f2 = open("Hiscore.txt","w")
f2.write(new_Highscore)
f1.close()
f2.close()