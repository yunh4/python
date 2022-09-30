# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

in_str = input("입력해주세요.\n")
print(in_str.upper()+" World!")

age = input("나이를 입력해주세요.\n")
print("당신의 나이는", age, "살 입니다.")

print(type(age)) #문자열 타입

print(10+int(age))

lan = input("국어 성적을 입력해주세요.\n")
math = input("수학 성적을 입력해주세요.\n")
eng = input("영어 성적을 입력해주세요.\n")
print("세 성적의 평균은", (int(lan)+int(math)+int(eng))/3, "입니다.")