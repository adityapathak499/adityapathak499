tup=(98,98,78,56,987,"Aditya","Pathak")
#print(type(tup), tup)
#print(tup[0::2])
#print(len(tup))
'''if 98 in tup:
    print("yes available")
else:
    print("not availbale")'''
'''x=list(tup)
x[-1]=786
y=tuple(x)
print(y)'''
y=("Aditya", "Rai")
y += tup
print(y)