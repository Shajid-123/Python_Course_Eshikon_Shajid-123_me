input1 = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12],
          [13,14,15,16]]

# output 1

output1_list1 = []   
output1_p1 = input1[:2]
output1_p3_1 = input1[0]
output1_p3_2 = input1[1][:2]

odd_or_even = []

for i in output1_p1:
    for j in i:
        output1_list1.append(j)
output1_p2 = output1_list1.insert(8, input1[2][0])

for char in output1_p3_1:
    output1_list1.append(char)

for char1 in output1_p3_2:
    output1_list1.append(char1)
output1_list1.insert(9, 0)

output1_list2 = []
output1_list2.append(output1_list1[:4])
output1_list2.append(output1_list1[4:8])
output1_list2.append(output1_list1[8:12])
output1_list2.append(output1_list1[12:16])

print("Output 1")
print("")
for char2 in output1_list2:
    print(char2)


# output 2

for l in input1:
    for k in l:
        if (k % 2) == 0:
            odd_or_even.append("Even")
        else:
            odd_or_even.append("Odd")

odd_or_even_2d_list = []
odd_or_even_2d_list.append(odd_or_even[:4])
odd_or_even_2d_list.append(odd_or_even[4:8])
odd_or_even_2d_list.append(odd_or_even[8:12])
odd_or_even_2d_list.append(odd_or_even[12:16])

print("")
print("Output 2")
print("")
for lists in odd_or_even_2d_list:
    print(lists)


#output 3


print("")
print("Output 3")
print("")

output3_list = [input1[2][1],input1[3][0]*2,input1[2][3],input1[2][0]*2]

print(output3_list)


#output 4


print("")
print("Output 4")
print("")
even = []

for odd_or_even_in_input1 in output3_list:
        if (odd_or_even_in_input1 % 2) == 0:
            even.append("Even")
        else:
            even.append("Odd")       

print(even)
