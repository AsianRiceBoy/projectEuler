#!/usr/bin/env python3

import math

#this is just combinations without repetition
#you need to move a total of 40 times
#so just n choose r with n = 40 and r = 20

print(math.factorial(40)/(math.factorial(20)*math.factorial(20)))
