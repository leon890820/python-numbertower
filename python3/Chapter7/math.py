avg=[0]*12
lines=[]
with open("math.txt") as infile:
    for i,line in enumerate(infile):
        if i==0:continue
        n,name,*ss=line.split()
        for k in range(len(ss)):
            avg[i-1]+=int(ss[k])
        lines+=[[n,name,ss,int(avg[i-1])/10]]
slines=sorted(lines,key=lambda p:-p[3])
for p in slines:
    print("{:>2}".format(p[0]),p[1],end=' ')
    for l in p[2]:
        print("{:>3}".format(l),end=' ')
    print(p[3])
    
        
        
