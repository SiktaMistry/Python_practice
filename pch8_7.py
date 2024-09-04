def remove_strip(string, word):
    newstr = string.replace(word,"")
    return newstr.strip()
str1 = "hello how are you"
print(str1)
word = raw_input("Enter a word from the above : \n")
print(remove_strip(str1,word))