num=int(input("enter the number"))
result=0
while(num!=0):
    digit=num%10
    result=result+(digit**3)
    num=num//10
print(result)
