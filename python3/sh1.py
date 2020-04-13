five=[127,8,8,62,10,18,36,255]
for i in range(len(five)):
    for j in range(7,-1,-1):
        if (five[i]>>j)%2==1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
