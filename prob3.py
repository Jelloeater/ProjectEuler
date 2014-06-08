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
		else:
			print(list(zip(factor, numeral)))







	# TODO MATH!!
	return "ANSWER LIST"


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
		print(pairList)

		if divList[0] is True and divList[-1:][0] is True:  # First and last should be divisible by themselves
			for numToCheck in divList[1:-1]:  # Checks list to make sure all are False
				if numToCheck:  # If they are divisible, let us know they are not prime
					return False
		return True


computeFactors(6552)
# TODO Figure out factors
# Factor 600851475143
# TODO Check if factors are prime
# Determine the largest factor that is also a prime




# Multi-thread example

# from multiprocessing.pool import ThreadPool

# pool = ThreadPool(processes=8)  # start 4 worker processes
# results = pool.map(prime, numList)  # prints "[0, 1, 4,..., 81]"
# pool.close()
# pool.join()
# pairs = zip(numList, results)




