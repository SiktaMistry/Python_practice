letter ='''Dear <|NAME|>,
You are selected!
 
Date: <|DATE|>
'''
name=raw_input("Enter your name\n")
date=raw_input("Enter the date\n")
letter=letter.replace("<|NAME|>",name)
letter=letter.replace("<|DATE|>",date)
print(letter)