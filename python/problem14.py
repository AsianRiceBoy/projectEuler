#!/usr/bin/env python3

def colLength(start):
	'''returns the length of the collatz sequence starting at the given number'''
	length = 1
	current = start
	while (current != 1):
		if (current % 2 == 0):
			current = current / 2
		else:
			current = 3*current + 1
		length += 1

	return length

currentLongest = 1
currentLongestStart = 1
for i in range(1,1000001):
	currentLength = colLength(i)
	if currentLength > currentLongest:
		currentLongest = currentLength
		currentLongestStart = i

print (currentLongestStart)
	