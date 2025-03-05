import random
target =random.randint (1,100)

while True:
    userchoice =int(input("guess the target:"))
    if (userchoice == target):
        print("success:your guess is correct")
    elif (userchoice < target):
        print("your no was to small take a bigger guess")
    else:
        print("your no is to big . take a smaller guess...")
        print("-------GAME OVER-------------")