a = int(input("Enter the first number:- "))
b = int(input("Enter the second number:- "))
c = int(input("Enter the third number:- "))
d = int(input("Enter the third number:- "))

'''if (a > b) and (a > c) and (a > d):------->First Method
    largest = a
elif (b > a) and (b > c) and (b > d):
    largest = b
elif (c > a) and (c > b) and (c > d):
    largest = c
else:
    largest = d

print("The greatest number found....", largest)'''
if (a > d):#----->Second Method
    f1 = a
else:
    f1 = d
if (b > c):
    f2 = b
else:
    f2 = c
if (f1 > f2):
    print(str(f1) + "is largest number")
else:
    print(str(f2) + "is largest number")
