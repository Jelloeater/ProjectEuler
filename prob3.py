__author__ = 'Jesse'

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

from multiprocessing.pool import ThreadPool


def prime(x):
	if str(x / 2).split(".")[1] != "0":  # Odd Number
		divList = []

		for numToCheck in range(x):
			if str(x / (numToCheck + 1)).split(".")[1] != "0":
				divList.append(False)
			else:
				divList.append(True)

		if divList[0] is True and divList[-1:][0] is True:  # First and last should be divisible by themselves
			for numToCheck in divList[1:-1]:  # Checks list to make sure all are False
				if numToCheck:  # If they are divisible, let us know they are not prime
					return False
		return True


numList = range(10000)

pool = ThreadPool(processes=8)  # start 4 worker processes

results = pool.map(prime, numList)  # prints "[0, 1, 4,..., 81]"
pool.close()
pool.join()

pairs = zip(numList, results)

answerList = []
for i in pairs:
	if i[1]:
		answerList.append(i[0])

answerList.pop(0)  # Remove 1

print(answerList)



