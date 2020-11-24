def factorial(num):#4
    fact=1
    # for i in range(1,num+1):
    #     fact=fact*i
    while num>1:
            fact=fact*num
            num=num-1
    print(fact)

factorial(3)