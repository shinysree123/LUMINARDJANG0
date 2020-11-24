num1=int(input("enter the number :"))
num2=int(input("enter the number :"))
num3=int(input("enter the number :"))

if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print(num2,"2nd largest")
    else:
        print(num3, "2nd largest")
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print(num1, "2nd largest")
    else:
        print(num3, "2nd largest")
elif((num3>num1)&(num3>num2)):
    if (num1 > num2):
        print(num1, "2nd largest")
    else:
        print(num2, "2nd largest")



