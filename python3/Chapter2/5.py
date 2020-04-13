for i in range(1,10):
    for j in range(9):
        print(' '*2+str(i),end='  ')
    print()
    for j in range(1,10):
        print('x '+str(j),end='  ')
    print()
    for j in range(9):
        print('---',end='  ')
    print()    
    for j in range(1,10):
        print("{:>3}".format(i*j),end='  ')
    print()
    print()
