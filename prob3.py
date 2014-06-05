import multiprocessing
import math

__author__ = 'Jesse'

# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

# from multiprocessing.pool import ThreadPool
#
# def computation(args):
# 	length, startPosition, npoints = args
# 	print(args)
#
# length = 100000000009191981950
# np=4
# p = ThreadPool(processes=np)
# p.map(computation, [(startPosition,startPosition+length, length//np) for startPosition in  range(0, length, length//np)])


from multiprocessing.pool import ThreadPool


def prime(x):
	if str(x / 2).split(".")[1] != "0":  # Odd Number
		divList = []

		for i in range(x):
			# print(str((i/x)*100).split(".")[0])
			if str(x / (i + 1)).split(".")[1] != "0":
				divList.append(False)
			else:
				divList.append(True)

		if divList[0] is True and divList[-1:][0] is True:  # First and last should be divisible by themselves
			for i in divList[1:-1]:  # Checks list to make sure all are False
				if i:  # If they are divisible, let us know they are not prime
					return False


def testPrime(x):
	if prime(x) is None:
		return True
	else:
		return False



pool = ThreadPool(processes=2)              # start 4 worker processes
objList = ["n","g","ssgf"]
results = pool.map(f,objList)         # prints "[0, 1, 4,..., 81]"

print(results)
pool.close()
pool.join()
print(results)


# print(testPrime(13))
# print(testPrime(17))
# print(testPrime(33))
# print(testPrime(991))
# print(testPrime(13))

# print(testPrime(600851475143))


# import threading
# import time
#
# exitFlag = 0
#
# class myThread (threading.Thread):
# 	def __init__(self, threadID, name, counter):
# 		threading.Thread.__init__(self)
# 		self.threadID = threadID
# 		self.name = name
# 		self.counter = counter
# 	def run(self):
# 		print "Starting " + self.name
# 		print_time(self.name, self.counter, 5)
# 		print "Exiting " + self.name
#
# def print_time(threadName, delay, counter):
# 	while counter:
# 		if exitFlag:
# 			thread.exit()
# 		time.sleep(delay)
# 		print "%s: %s" % (threadName, time.ctime(time.time()))
# 		counter -= 1
#
# # Create new threads
# thread1 = myThread(1, "Thread-1", 1)
# thread2 = myThread(2, "Thread-2", 2)
#
# # Start new Threads
# thread1.start()
# thread2.start()
#
# print "Exiting Main Thread"