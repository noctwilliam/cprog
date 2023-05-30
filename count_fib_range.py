def count_fibonacci_range(a,b):
	'''
	Returns the number of Fibonacci numbers in the range [a,b]
	'''
	fibs = [0,1]
	while fibs[-1] < b:
		fibs.append(fibs[-1]+fibs[-2])
	return len([x for x in fibs if x >= a and x <= b])
print(count_fibonacci_range(1234567890, 9876543210))