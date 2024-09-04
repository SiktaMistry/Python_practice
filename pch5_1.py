myDict = {
    "Pankha": "Fan",
    "Dabba": "Box",
    "Vastu": "Item"
}
print("The options are",myDict.keys())
a = raw_input("Enter the Hindi Word\n")
print("The English Translation of your Word is: ",myDict.get(a))