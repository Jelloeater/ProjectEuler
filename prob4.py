__author__ = 'Jesse'
import json

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.

def writeList():
	numRange = range(100, 1000)

	num1 = []
	num2 = []
	ans = []
	for i in numRange:
		for i2 in numRange:
				x = i * i2
				num1.append(i)
				num2.append(i2)
				ans.append(x)


	jsonStr = json.dumps(list(zip(num1, num2, ans)),indent=2)
	fileHandle2 = open("data.json", "w")
	fileHandle2.write(jsonStr)
	fileHandle2.close()

def searchList():
	numList = json.load(open('data.json'))

	def palindromeTest(x):
		return True


	palTestList = []

	for i in numList:
		palTestList.append(palindromeTest(i[2]))

	print()

# writeList()
searchList()