#!/usr/bin/env python3

result = 0
for i in range (1,1001):
	result += (i**i % 10000000000)

print (result % 10000000000)