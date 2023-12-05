list = [2,4,4,4,5,5,7,9]
sum = 0

for  i in list:
    sum = sum+i


def custom_len(x):
    count = 0
    for j in x:
        count = count+1
    return count


mean_avr = sum/custom_len(list)

sum1 = 0 
for k in list:
    list_sum = (k - mean_avr)**2
    sum1 = sum1+list_sum




o = (sum1/(custom_len(list)-1))**(1/2)

print(o)