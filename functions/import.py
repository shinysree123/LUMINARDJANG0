import functions.mathoperation
from functions.mathoperation import *
# add=functions.mathoperation.addition(3,4)#by using from we dont need to call again for each functions
print(addition(3,4))
# sub=functions.mathoperation.subtraction(4,3)
print(subtraction(4,3))
# mul=functions.mathoperation.mul(4,3)
print(mul(4,3))
# div=functions.mathoperation.div(4,3)
print(div(4,3))



import functions.mathoperation as fun
# from functions.mathoperation import *
add=fun.addition(3,4)#by using from we dont need to call again for each functions
# print(addition(3,4))
print(add)
