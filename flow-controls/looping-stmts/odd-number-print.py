lower_limit=int(input("enter the lower limit"))
upper_limit=int(input("enter the upper limit"))
sum=0
if(lower_limit>upper_limit):
    print("error")
while(lower_limit<=upper_limit):
    if(lower_limit%2!=0):
        sum+=lower_limit
    lower_limit+=1
print(sum)