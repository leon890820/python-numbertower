lines=[]
aves=['']
srain=[0]*10
with open ("rain.txt") as infile:
    for i,line in enumerate(infile):
        if i<2:continue
        else:
            date,hr,*rain=line.split()
            rain=[int(x) for x in rain]
            
            for k,rf in enumerate(rain):
                srain[k]+=rf
        print(date,hr,end=' ')
        for k in range(10):
            print("{:>3}".format(rain[k]),end=' ')
        print()
    print(' '*14,end='')
    for i in range(10):
        print("{:>3}".format(srain[i]),end=' ')
        
   
                
            
       
   
        
