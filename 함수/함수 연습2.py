# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
#두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# 함수 호출 예 : print_arithmetic_operation(3, 4)

def print_arithmetic_operation(a, b) :
	print(f'{a} + {b} = {a+b}')
	print(f'{a} - {b} = {a-b}')
	print(f'{a} * {b} = {a*b}')
	print(f'{a} / {b} = {a/b}')
	
print_arithmetic_operation(3, 4)
