name = "Shajid yt gaming 12345678990"
phone = "0"
email = "s"

if (len(name)==0 or len(phone)==0 or len(email) == 0 ): 
    print("failed")


else:
    if(len(name)<2 or len(name)>20):
        print("The name lenght must be beetween 2 and 20 charecters")
    elif(len(phone)!=11):
        print("Phone size must be equal to 11")
    else:
        print("Success")