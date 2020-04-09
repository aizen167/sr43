d = 186
point = 1
x = input("please input the first number:")
while(point<152):
    flag = 0
    i = 2
    while(i<x):
        if x%i == 0:
            flag = 1
            break
        else:
            i+=1
    if flag==1:
        x+=d
        print"FALSE_", x
    elif flag==0:
        print point
        print x
        x+=d
        point+=1
