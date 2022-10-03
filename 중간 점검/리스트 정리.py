# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import random

numbers = [] #빈 리스트 생성
while len(numbers) < 7 :
	number = random.randint(1, 45) #35
	if number not in numbers :
		numbers.append(number) #35를 리스트에 확장
numbers.sort()
print(numbers)