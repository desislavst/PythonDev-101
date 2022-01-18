age = int(input("How old are you?"))


if age >= 18 and age < 21:
    print("You can enter, but need a wristband")
elif age >= 21:
    print("You are good to enter and drink")
else: 
    print("Sorry, too young")