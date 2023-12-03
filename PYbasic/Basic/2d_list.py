list = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]] #colum value

# print(list[2][1])#[row]#[col]
# print(len(list[1])) #row count

print("")

for i in range(5):
    for j in range(5):
        print(i,j)

print("")

for row in range(len(list)): #row = 0;1;
    col_size = len(list[row]) # col size =3
    for col in range(col_size): 
        print(list[row][col])

print("")

for row in list:
    print(row)
    for col in row:
        print(col) 