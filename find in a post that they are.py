a = input("Enter a Name to check whether is availabe or not in post:-")

name = "My name is Aditya Pathak.I am from Umila,Sant Kabir Nagar"


if a in name.lower():
    print("Yes your name is present in post")
elif a in name.upper():
    print("Yes your name is present in post")
else:
    print("No,Your name is not present in post")
