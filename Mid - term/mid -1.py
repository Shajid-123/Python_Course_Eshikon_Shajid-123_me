list = [2,4,4,4,5,5,7,9]
sum = 0




def custom_len(x):
    count = 0
    for j in x:
        count = count+1
    return count


mean_avr = sum/custom_len(list)


for k in list:
    list_sum = k - mean_avr**2
    sum = sum+list_sum




o = (sum/(custom_len(list)-1))**(1/2)

print(o)