from random import *

n , total = 5 , 50000

counts = [ 0 for x in range(n+1) ]

for k in range(total) :

    # 起始落下的位置
    ball_pos = 2*randint(1,n) - 1

    # 第一層釘子
    move = 2*randint(0,1) - 1
    ball_pos += move 

    # 第二到第五層釘子
    for i in range(2) :
        
        move = 2*randint(0,1) - 1
        ball_pos += move 

        # 碰到兩側，提前離開
        if ball_pos < 0 or ball_pos > 2*n : break 

        move = 2*randint(0,1) - 1
        ball_pos += move 

    # 球數統計
    if ball_pos < 0 : 
        counts[0] += 1
    elif ball_pos > 2*n :
        counts[-1] += 1
    else :
        counts[ball_pos//2] += 1

# 列印
for no in counts :
    s = int(160*no/total+0.5)
    print(str(s)+"/160",end=" ")

print()        
