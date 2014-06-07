__author__ = 'Jesse'

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


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
			if num[0] == num[-1] and num[1] == num[-2] and num[2] == num[-3]:
				# FIXME
				# # TODO Check x against answers in ans
				num1.append(i)
				num2.append(i2)
				ans.append(x)

	listOutput = list(zip(num1, num2, ans))

	print(answerCountList(listOutput))
	print()

	# # answers = list(set(answers))


	# for listItem in listOutput:
	# 	for i in answers:
	# 			if listItem[2] == i:
	# 				try:
	# 					del listOutput[listOutput.index(listItem)]
	# 				except:
	# 					pass


	listOutput = list(set(listOutput))

	listOutput.sort(key=lambda listOutputIN: listOutputIN[2])

	print(listOutput)


if __name__ == "__main__":  # Runs Script
	listPals(700, 900)
