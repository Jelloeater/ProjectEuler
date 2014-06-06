__author__ = 'Jesse'

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def printOnlyAnswers(list):
	answers = []
	for i in list:
		answers.append(i[2])
	answers.sort()
	print(answers)
	return answers


def listPals(start=100, stop=200):
	numRange = range(start, stop)

	num1 = []
	num2 = []
	ans = []

	def inAnsList(num):
		for i in ans:
			if i == num:
				return True
			else:
				return False

	for i in numRange:
		for i2 in numRange:
			x = i * i2
			num = str(x)
			if num[0] == num[-1] and num[1] == num[-2]:
				# FIXME
				# # TODO Check x against answers in ans
				num1.append(i)
				num2.append(i2)
				ans.append(x)


	listOutput = list(zip(num1, num2, ans))

	answers = printOnlyAnswers(listOutput)

	for item in listOutput:
		if item[1] != [answers in answers]:
			print("DOUBLE")


	listOutput = list(set(listOutput))

	# print(listOutput)


if __name__ == "__main__":  # Runs Script
	listPals(5, 55)
