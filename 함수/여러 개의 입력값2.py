# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
a = input().split(" ")

x = int(a[0]); op = a[1]; y = int(a[2])

def cal(x, op, y) :
	if op == "+" : print(f'{x} {op} {y} = {x+y}')
	elif op == "-" : print(f'{x} {op} {y} = {x-y}')
	elif op == "*" : print(f'{x} {op} {y} = {x*y}')
	elif op == "/" : print(f'{x} {op} {y} = {x/y}')
	
cal(x, op, y)