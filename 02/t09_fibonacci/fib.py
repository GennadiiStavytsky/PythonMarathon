def fib(n):
	fib1 = 0
	fib2 = 1
	i = 0
	while i < n:
		res = fib1 + fib2
		fib1 = fib2 
		fib2 = res
		i += 1
	return fib1

def fib_generator(na):
	n1, n2 = 0, 1
	count = 0

	if na == 1:
		yield n1
	else:
		while count < na:
			yield n1
			nth = n1 + n2
			n1 = n2
			n2 = nth
			count += 1