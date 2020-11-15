n=input()
l=len(n)
sum=0
for i in range(l):
    sum+=pow(2,l-i-1)*int(n[i])
print(sum)