p = "春眠不覺曉處處聞啼鳥夜來風雨聲花落知多少"

while True :

    # 讀入詩句列數
    h = int(input("> "))

    # 計算詩句行數
    w = len(p)//h + ( 1 if len(p)%h else 0 )

    for i in range(h) :
        for j in range(w-1,-1,-1) :

            k = j*h+i
            print( p[k] if k < len(p) else "  " , end=" ")

        print()

    print()
