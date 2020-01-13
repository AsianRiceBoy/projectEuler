#!/usr/bin/env python3

sum = 0
for i in range(1000):
	if (i % 3 == 0) or (i % 5 ==0):
		sum += i

print(sum)

#one line solution
print (sum(filter(lambda i:(i % 3 == 0) or (i % 5 == 0), [a for a in range(1000)])))