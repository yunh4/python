# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a = int(input())

for i in range(a-1):
	print(" "*(a-i-1)+"*"+" "*(i*2-1), end="")
	if i == 0:
		print("")
	else:
		print("*")
print("*"*(a*2-1))