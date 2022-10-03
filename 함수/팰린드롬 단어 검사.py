# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

# def palindrome(string) :
# 	print(string == string[::-1])
# palindrome(input())

# is_palindrome = True

# word = input()
# for i in range(len(word) // 2):
# 	if word[i] != word[-1 - i]:
# 		is_palindrome = False
# 		break
# print(is_palindrome)

def pelin(str) :
	str2 = list(reversed(str))
	# print(type(str2))
	print(str == str2)

str = list(input())
pelin(str)