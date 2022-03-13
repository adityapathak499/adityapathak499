s1=int(input("Enter the first subject marks :"))
s2=int(input("Enter the second subject marks :"))
s3=int(input("Enter the third subject marks :"))
if (s1<33 and s2<33 and s3<33):
    print("you are failed coz all subject marks are not greater than 33")
elif (s1+s2+s3)/3 <40:
    print("you are failed!")
else:
    print("You are Passed")