with open("poems.dat") as infile :

	for n , line in enumerate(infile) :

		line = line.strip()

		if line == "" : continue

		ws = sorted( [ c for c in line if c not in "。，" ] )

		if n == 0 :
			# 交集字串列
			cwords = []
			for w in ws :
				if w not in cwords : cwords += [w]    # 避免儲存重複字
		else :
			# 新的交集字串列
			new_cwords = []

			for w in ws :
				if w in cwords : new_cwords += [w]    # 找新交集字 

			# 更新交集字
			cwords = new_cwords[:]

# 列印交集字
print( " ".join(cwords) )
