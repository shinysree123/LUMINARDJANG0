lower=int(input("enter the lower limit"))
upper=int(input("enter the upper limit"))
evensum=0
oddsum=0
for i in range(lower,upper):
    if(i%2==0):
        evensum=evensum+i

    else:
        oddsum=oddsum+i
print(evensum,"sum of even numbers")
print(oddsum,"sum of odd numbers")