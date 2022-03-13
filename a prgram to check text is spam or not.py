a = input("Enter the text\n ")

if ("click on" in a):
    spam = True
elif ("watch this" in a):
    spam = True
elif ("xxx" in a):
    spam = True
else:
    spam = False

if (spam):
    print("this text is spam")
else:
    print("this text is not spam")