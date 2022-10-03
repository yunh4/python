# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n = int(input())

for i in range(1, n+1) :
	print("*"*i+" "*2*(n-i)+"*"*i)
for j in range(1, n) :
	print("*"*(n-j)+" "*2*j+"*"*(n-j))
