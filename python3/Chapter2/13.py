n=int(input()) 
import math 
for i in range(2*n): 
    if i<n: 
        print(' '*2*n,end='') 
    else: 
        print(' '*(2*n-i-1)+'/'+"--"*(i-n)+"\\" + " "*(2*n-i-1),end="") 
    print(' '*(2*n-i-1)+'/'+"--"*i+"\\"+' '*(2*n-i-1),end="") 
    if i<= (n/2)-1: 
        print("") 
    else: 
        print(' '*(2*n-i-1)+'/'+"--"*(i-math.floor(n/2))+"\\")
