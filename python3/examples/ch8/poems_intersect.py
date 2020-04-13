with open("poems.dat") as infile :

    for n , line in enumerate(infile) :

        # 去除標點符號
        poem = set( filter( lambda c : c not in "。，" , line.strip() ) )

        if n == 0 : 
            words = poem.copy() 
        else :
            words.intersection_update(poem)
      
print( " ".join( words ) )
