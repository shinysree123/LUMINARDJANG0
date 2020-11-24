# a=int(input())
# b=int(input())
# for row in range(a,b):
#     for col in range(0,row):
#         print("*",end="  ")
#     print()
#1
# 1 2
# 123
# 1234
for row in range(0,5):
    for col in range(1,row+1):
        print(col,end=" ")
    print()