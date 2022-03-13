'''a=10
b=10
print(id(b))'''
"""a=10
print(type(a))
b=05.56
print(type(b))"""

"""a = range(1, 100, 2)
for i in a:
    print(i)"""

"""b={10,20,30,40,40,40,'Aditya','Pathak'}
print(b)"""

"""dicta={1:'Aditya',2:'Abhishek',3:'Satish'}
print(dicta.get(3))"""

'''class Employee:
    def __init__(self, name, age, department, gender):
        self.name = name
        self.age = age
        self.department = department
        self.gender = gender

    def employee_details(self):
        print("Employee name is", self.name)
        print("Employee age is", self.age)
        print("Employee department is", self.department)
        print("Employee gender is", self.gender)


e1 = Employee("Aditya", 18, "NOC", "Male")
e1.employee_details()
print(e1)

e2 = Employee("Abhishek", 19, "SMS NOC", "Male")
e2.employee_details()
print(e2)

e3 = Employee("Avvi", 20, "SMS NOC", "Male")
e3.employee_details()
print(e3)'''

'''num=int(input("Enter the number to check that the number is even or odd: "))
if num % 2==0:
    print('Number is even', num)
else:
    print("Number is odd")'''

dicts = {"Name1": "Aditya", "Name2": "Abhishek", "Name3": "Mishra", "Name4": "Singh"}
inpu = input("Enter the Keys to check the value: ")
if inpu in dicts.keys():
    print(dicts.get(inpu))
else:
    print("None")
