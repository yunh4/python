# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
def gugudan(a) :
	for i in range(1, 10) :
		print(f'{a} x {i} = {a*i}')
n=int(input("단입력 : "))
gugudan(n)