n=int(input())
for i in range(2*n):
    if i<n:
        print('* '*n+'- '*2*n)
    else:
        print('+ '*n+"- "*2*n)
        
