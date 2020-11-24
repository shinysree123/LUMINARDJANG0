a=int(input("enter the num:"))
b=int(input("enter the num:"))
c=int(input("enter the num:"))
if((a>b)&(a>c)):
    if(b>c):
        print(a,b,c)
    else:
        print(a,c,b)
elif((b>c)&(b>a)):
    if(c>a):
        print(b,c,a)
    else:
        print(b,a,c)
elif((c>a)&(c>b)):
    if(a>b):
        print(c,a,b)
    else:
        print(c,b,a)
