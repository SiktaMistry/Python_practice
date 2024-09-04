markSub1 = int(raw_input("Enter the marks of subject 1: "))
markSub2 = int(raw_input("Enter the marks of subject 2: "))
markSub3 = int(raw_input("Enter the marks of subject 3: "))
totalmarks = (markSub1+markSub2+markSub3)/3
if(markSub1>=33 and markSub2>=33 and markSub3>=33 and totalmarks>=40):
    print("Student has Passed")
else:  
    print("The student have Failed")  