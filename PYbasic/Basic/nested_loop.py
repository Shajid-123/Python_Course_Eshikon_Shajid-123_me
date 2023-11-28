for i in range(len(list)):
    for j in range(len(list)):
        print(i,j)


for row in range(len(list)): #row = 0;1;
    col_size = len(list[row]) # col size =3
    for col in range(col_size): 
        print(list[row][col]) 