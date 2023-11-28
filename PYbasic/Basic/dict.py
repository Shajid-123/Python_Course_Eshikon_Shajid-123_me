cars = {"car1":{"model":"porshe gt3 rs","price":"$100K"},"car2":{"model":"supra mk4","price":"$80k"}}

for i,j in cars.items():
    for k in j.items():
        for l in k:
            print(i,l)
