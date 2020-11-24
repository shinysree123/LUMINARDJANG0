lower=int(input("enter the lower limit"))#1
upper=int(input("enter the upper limit"))#10
for num in range(lower,upper+1):#num(1,10)
    if(num>1):
        for i in range(2,num):#2,1
            if(num%i==0):
                break
        print(num)

