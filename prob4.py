__author__ = 'Jesse'

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

# Answer: 913 x 993 = 906609

def answerCountList(listIn):
	answers = []
	for i in listIn:
		answers.append(i[2])
	answers.sort()

	answerNumbers = list(set(answers))
	answerCount = []

	for i in answers:
		answerCount.append(answers.count(i))

	answersAndCount = list(zip(answerNumbers, answerCount))

	answersAndCount.sort(key=lambda answersAndCountIn: answersAndCountIn[0])
	return answersAndCount


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
			if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:  # Checks if palindrome
				if ans.count(x) < 1:  # Make sure there is only one of each answer
					num1.append(i)
					num2.append(i2)
					ans.append(x)

	listOutput = list(zip(num1, num2, ans))

	# print(answerCountList(listOutput))
	# print()

	# TODO Write code to clean list of duplicates

	listOutput.sort(key=lambda listOutputIN: listOutputIN[2])

	# print(listOutput)

	print("Answer")
	print(listOutput[-1])


if __name__ == "__main__":  # Runs Script
	listPals(100, 1000)
