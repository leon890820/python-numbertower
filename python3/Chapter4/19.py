n=int(input())
pp=[0x180,0x3c0,0x180,0xc0,0xf0,0xe8,0x164,0x264,0x70,0x50,0x8e,0x81,0x82,0x300]
s=len(pp)
for i in range(s):
 for k in range(n):
   for j in range(9,-1,-1):
     if (pp[i]>>j)%2:
       print('*',end='')
     else:
       print(' ',end='')
   print(' ',end='')   
 print()     
