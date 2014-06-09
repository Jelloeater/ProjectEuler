__author__ = 'Jesse'
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#
# What is the 10001st prime number?

import math
def is_prime(n):
	if n % 2 == 0 and n > 2:
		return False

	for i in range(3, int(math.sqrt(n)) + 1):
		if n % i == 0:
			return False
	return True

def prime(x):
	if str(x / 2).split(".")[1] != "0":  # Odd Number

		for numToCheck in range(3, int(math.sqrt(x))+1):  # Tests to square root rounded up
			if str(x / numToCheck).split(".")[1] == "0":
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
ansList = generateList(10001)
print(ansList[-1])

