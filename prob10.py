__author__ = 'Jesse'
# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# 142913828921

import math


def prime(x):
	if x % 2 == 1:  # Odd Number

		for numToCheck in range(2, int(math.sqrt(x))+1):  # Tests to square root rounded up
			if x % numToCheck == 0:
				return False
		return True


def generateList(limit):
	primeList = []
	num = 1
	while num < limit:
		if prime(num):
			primeList.append(num)
			print(str(len(primeList)) + " - " + str(num))
		num += 1
	return primeList


numberList = generateList(2000000)

x = 0
for i in numberList:
	x = i + x

print("Answer")
print(x)