n=int(input())
two=[31,1,31,16,31]
for l in range(len(two)):
    for i in range(len(two)):
        for k in range(4,-1,-1):
            for j in range(4,-1,-1):
                if (two[i]>>j)%2==1 and (two[l]>>k)%2==1:
                    print('2',end='')
                else:
                    print(' ',end='')
            print(' ',end='')
        print()
            
