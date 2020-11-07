#Number Guessing Game:

from random import randint


guess = int(input("Enter a Number Between 1 to 50:"))
n = randint(1,50)
while n!=guess:
    if guess<n:
        print("Guess is low")
        guess = int(input("Enter a Number Between 1 to 50:"))
    elif guess>n:
        print("Guess is high")
        guess = int(input("Enter a Number Between 1 to 50:"))
else:
    print("Hurray...You won!! Your guess is correct")

        
