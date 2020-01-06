#!/usr/bin/env python3

def fib(limit):
	"""returns a list of numbers in the fibonacci sequence, starting at 1 up to the limit given"""
	nums = [1, 2]
	while (nums[-1] + nums[-2] < limit):
		nums.append(nums[-1] + nums[-2])
	
	return nums

def isEven(num):
	"""returns True if num is even"""
	return (num % 2 == 0)

sum = 0

for i in fib(4000000):
	if isEven(i): sum += i

print(sum)
