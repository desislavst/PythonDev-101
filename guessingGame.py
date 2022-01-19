import random
random_number = random.randint(1,10)
playagain = "y"
myguess = int(input("Pick a number between 1 and 10?"))
# if myguess == random_number:
#     print("Well done! Do you want to play another one? (y/n)")
while playagain == "y":
    while myguess != random_number:
        if myguess < random_number:
            print("Try higher")

        else:
            print("Try lower")
        myguess = int(input("Your new guess?"))  
    playagain = str(input("Well done! Do you want to play again? (y/n)")) 
    if playagain == "n":
        break
    else:
        myguess = int(input("Pick a number between 1 and 10?"))
