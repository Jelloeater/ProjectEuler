__author__ = 'Jesse'
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

limit = 1000

list = []

for i in range(limit):
	if i*3 < limit:
		list.append(i * 3)
	if i*5 < limit:
		list.append(i * 5)
	# print(str(i) +" "+ str(list))
	if list.count(0) >=1:
		list.remove(0)
	list.sort()

print(list)