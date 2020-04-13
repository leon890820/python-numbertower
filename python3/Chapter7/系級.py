rms=0
lines=[]
with open ("ss.txt") as infile:
    for i,line in enumerate(infile):
        rms=0
        if i==0 or i==2 or i==3:
            print(line.rstrip())
            continue
        elif i==1:
            pp=[int(x) for x in line[5:].split()]
            print(line.rstrip())
        else:
            name,ee,*ss=line.split()
            for k in range(4):
                rms +=int(ss[k])*int(pp[k])/100
            lines+=[[name,ee,ss,rms]]
srms=sorted(lines,key=lambda p:[-p[3]])
for i,p in enumerate(srms):
    print("{:>2}".format(i+1),p[0],p[1],end=' ')
    for j in range(4):
        print("{:>4}".format(p[2][j]),end=' ')
    print("{:>5.1f}".format(p[3]))



            
            
        
        
