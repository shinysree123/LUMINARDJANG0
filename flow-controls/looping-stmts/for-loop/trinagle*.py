for row in range(1,5):
    for column in range(1,8):
        if(row==4 or row+column==5 or column-row==3):
            print("*",end="\t")
        else:
            print(end="\t")
    print()