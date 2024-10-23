from random import randint

n = randint(1 , 100)

a  = -1

gusse = 0

while(a!=n):
    gusse = gusse + 1
    a = int ( input("Enter the nummber between 1 to 100: "))

    if (a>n):
        print ("ENTER LOWER NUMBER ")
    else:
        print   ("ENTER HIGHER NUMBER ")  

print (f"YOU GUSSE THE NUMBER {n} CORRECTLY IN {gusse} ATTEMPTS.")        
