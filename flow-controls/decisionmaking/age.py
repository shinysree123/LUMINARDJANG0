bday=int(input("enter the birth day"))
byear=int(input("enter the birth year"))
bmonth=int(input("enter yhe birth month"))
cday=int(input("enter the current day"))
cyear=int(input("enter the current year"))
cmonth=int(input("enter the current month"))
if((bmonth==cmonth)&(bday==cday)):
    age=cyear-byear
    print(age)
elif(cmonth>bmonth):



