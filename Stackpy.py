l=[]
while True:
    c=int(input("""
    1 Push elements
    2 Pop elements
    3 Peek element
    4 Display elements
    5 Exit
     
    """))
    if c==1:
        n=input("Enter the value :-");
        l.append(n)
        print(l)
    elif c==2:
            if len(l)==0:
                print("Empty list")
            else:
                p=l.pop()
                print(p)
                print(l)
    elif c==3:
        if len(l)==0:
            print("Empty list")
        else:
            print("last stack value",l[-1])
    elif c==4:
        print("Display the stack",l)
    elif c==5:
        break;
    else:
        print("Invalid option !")