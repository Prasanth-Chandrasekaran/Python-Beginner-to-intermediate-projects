
#Dice Script


from random import randint

roll = input("Do you want to roll dices(y/n):")

if roll=="y":
    while roll=="y":
        print("Rolling the dices")
        dice1=randint(1,6)
        dice2=randint(1,6)
        print(dice1,dice2)
        roll=input("Do you want to Roll again(y/n)\n")
        if roll =="y":
            continue
        else:
            print("Thanks for playing")
else:
    print("Thanks for playing")
