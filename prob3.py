__author__ = 'Jesse'

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def computeFactors(numberIn):
	divisor = 2

	factor = []
	numeral = []
	while True:
		answer = numberIn / divisor
		if str(answer).split(".")[1] == "0":
			numeral.append(int(answer))
			factor.append(divisor)
			numberIn = answer
		else:
			divisor += 1
		if answer < 1:
			break

	return list(zip(factor, numeral))


def prime(x):
	if str(x / 2).split(".")[1] != "0":  # Odd Number
		divList = []
		numList = []

		for numToCheck in range(x):
			if str(x / (numToCheck + 1)).split(".")[1] != "0":
				divList.append(False)
			else:
				divList.append(True)
			numList.append(numToCheck)

		pairList = list(zip(numList, divList))
		# print(pairList)

		if divList[0] is True and divList[-1:][0] is True:  # First and last should be divisible by themselves
			for numToCheck in divList[1:-1]:  # Checks list to make sure all are False
				if numToCheck:  # If they are divisible, let us know they are not prime
					return False
		return True


def primeFactorList(number):
	factorList = []
	primeCheckList = []
	for i in computeFactors(number):
		factorList.append(i)
		primeCheckList.append(prime(i[0]))

	return list(zip(factorList, primeCheckList))

print(600851475143)
ans = primeFactorList(600851475143)
print(ans)
print()
print('Answer')
print([x for x in ans if x[1] is True][0][0][1])
