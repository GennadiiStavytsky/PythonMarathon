def contains(str_arg, substr):
	res = []
	for it in substr:
		if it.lower() in str_arg.lower():
			res.append(it)
	return res