__author__ = 'Jesse'

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?


def prime(x):
	if str(x / 2).split(".")[1] != "0":  # Odd Number
		divList = []

		for i in range(x):
			# print(str(x) + " / " + str((i+1)))
			# print(x / (i+1))
			if str(x / (i+1)).split(".")[1] != "0":
				divList.append(False)
			else:
				divList.append(True)


		# print(divList)
		# print(divList[1:-1])

		# print()
		# print(divList[0])  # Beginning of list
		# print(divList[-1:][0])  # End of list

		if divList[0] == True and divList[-1:][0] == True:
			for i in divList[1:-1]:
				if i:
					# print(i)
					return False
				# 	return False
				# else:
				# 	return True


def testPrime(x):
	if prime(x) is None:
		return True
	else:
		return False

print(testPrime(13))
print(testPrime(17))
print(testPrime(33))
print(testPrime(39))
print(testPrime(13))
