import itertools

def add_decomp(summa, numterms):
	count = 0
	for combinations in itertools.combinations_with_replacement(range(1, summa),numterms):
		# print(combinations)
		# print(type(combinations)
		if summa == sum(list(combinations)):
			count += 1
	return count

def number_constraints(sum, numterms):
	acceptable = False
	if sum >= 1 and sum <= 30 and numterms >= 1 and numterms <= 10:
		acceptable = True
	return acceptable

test_cases = int(input("Enter the number of test cases: "))
test_cases_output = []
print(add_decomp(6,2))
if (test_cases <= 1000):
	for i in range(test_cases):
		num1, num2 = map(int, input().split())
		if number_constraints(num1, num2):
			test_cases_output.append(f"{num1} MAYBE REPRESENTED AS THE SUM OF {num2} INTEGERS IN {add_decomp(num1, num2)} WAYS")
else:
	print("Number of test cases must be less than or equal to 1000")


for i in test_cases_output:
	print(i)