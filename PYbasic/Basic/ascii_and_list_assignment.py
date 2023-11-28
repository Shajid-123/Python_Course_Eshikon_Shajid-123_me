list1 = ["ab","cd"]
list2 = []
for i in list1:
    sum =0
    for j in i:
        ascii = ord(j)
        sum = sum+ascii
    list2.append(ascii)
print(list2)
