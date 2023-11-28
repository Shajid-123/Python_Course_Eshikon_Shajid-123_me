name = input("Name: ")
sum = 0
for char in name:
    print(char," - Ascii value is",ord(char))
    sum = sum + ord(char)


print("Total ASCII value of",name,"is",sum)                                      
