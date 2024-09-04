myDict = {
    "spam1" : "make a lot of money",
    "spam2" : "buy now",
    "spam3" : "subscribe this",
    "spam4" : "click this"
}
print(myDict.values())
a = raw_input("Enter the comment: ")
if(a==myDict["spam1"] or myDict["spam2"] or myDict["spam3"] or myDict["spam4"]):
    print("SPAM......")
    