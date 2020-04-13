for a in range(1,10):
    for b in range(10):
        if a==b:continue
        for c in range(10):
            if c in [a,b]:continue
            if a+b+c==10:
                print(a*100+b*10+c)
