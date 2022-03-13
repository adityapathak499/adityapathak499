import random

cnumber = random.randrange(1, 100)
Userinput = int(input("Enter your number--->"))
if Userinput > cnumber:
    print("Computer generated number is--->", cnumber)
    print("Your number is too high")
elif cnumber > Userinput:
    print("Computer generated number is--->", cnumber)
    print("Your number is too low")
else:
    print("Computer generated number is--->", cnumber)
    print("Number is equal..!")
