__author__ = 'Jesse'

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def listPals(start = 100, stop = 200):
	numRange = range(start, stop)

	num1 = []
	num2 = []
	ans = []
	for i in numRange:
		for i2 in numRange:
			x = i * i2
			num = str(x)
			if num[0] == num[-1] and num[1] == num[-2]:
				if True: # FIXME
					## TODO Check x against answers in ans
					num1.append(i)
					num2.append(i2)
					ans.append(x)
	listOutput = list(zip(num1,num2,ans))


	answers = []
	for i in listOutput:
		answers.append(i[2])

	answers.sort()
	print(answers)


	listOutput = list(set(listOutput))

	# print(listOutput)


if __name__ == "__main__":  # Runs Script
	listPals(5,55)
