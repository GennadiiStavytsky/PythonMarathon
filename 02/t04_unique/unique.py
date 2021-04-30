def make_unique(dic):
	for it in dic:
		#print(it)
		dic[it] =sorted(list(set(dic[it])))
	
	return dic
