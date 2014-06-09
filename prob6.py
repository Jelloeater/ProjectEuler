__author__ = 'Jesse'
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10 001st prime number?


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

		if divList[0] is True and divList[-1:][0] is True:  # First and last should be divisible by themselves
			for numToCheck in divList[1:-1]:  # Checks list to make sure all are False
				if numToCheck:  # If they are divisible, let us know they are not prime
					return False
		return True


def generateList(countTo=1000):
	primeList = []
	num = 1
	while len(primeList) < countTo:
		if prime(num):
			primeList.append(num)
			print(str(len(primeList)) + " - " + str(num))
		num += 1

	return primeList

print("Answer")
ansList = generateList(100)
print(ansList[-1])