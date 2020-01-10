#!/usr/bin/env python3

'''
for n = 3 up, the numbers on the diagonal of the matrix for this problem
are given by the polynomials n^2, n^2 + (1 - n), n^2 + 2(1 - n), n^2 + 3(1 - n).
The sum of these polynomials is 4n^2 + 6(1 - n)
'''

result = 0
for n in range(3,1002,2):
	result += (4*(n**2) + 6*(1 - n))

result += 1 #add 1 to account for n = 1

print (result) 