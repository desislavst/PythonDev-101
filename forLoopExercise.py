for i in range(1,21):
    if i == 4 or i == 13:
        print(str(i) + " is unlucky!")
    elif (i % 2) == 0:
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")