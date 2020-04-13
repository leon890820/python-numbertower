poem=("寒泉漱玉清音好好處深居近翠巒巒秀聳岩飛澗水水邊松竹檜宜寒寒窗淨室親邀客客待閒吟恣取歡歡宴聚陪終席喜喜來歸興酒闌殘")
n,r,c,d=7,5,1,0
dr,dc=[0,-1,0,1],[-1,0,1,0]
h=0
p=[["  "]*n for i in range(n)]
for i,ch in enumerate(poem):
    if i>0 and i%n==0: continue
    p[r][c]=ch
    r+=dr[d]
    c+=dc[d]
    if (r==c or (r==5 and c==0) or (r<c and r+c==n-1)or (r>c and r+c==n)):
        d+=1
        if d==4:d=0
for i in range(n):
    print(' '.join(p[i]))
