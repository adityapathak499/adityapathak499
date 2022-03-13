a = int(input("Enter a number to print a table of given number: "))

for i in range(10, 0, -1):
     print(str(a) + " X " + str(i) + "=" + str(i*a))
    #print(f"{a} X {i} = {i * a}")  # print's as same as above one

"""l1=["Subham","Shivam","Aadi"]
for name in l1:
    if name.startswith("S"):
        print("Hello "+ name)
    else:
        print("not found")"""

"""a = int(input("Enter a number to print a table of given number: "))

count = 1
print("The tabe of given number is", a)

while count <= 10:
    a = a * 1
    print(a, " X ", count, "=", a * count)
    count += 1"""

"""a=8
for a in range(8):
    print(" * " * (a*1))"""
