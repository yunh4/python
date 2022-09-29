# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

sex = input("성별을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))

if sex == 'man' and age >= 13:
  print("남자화장실 출입이 가능합니다.")
else:
  print("남자화장실 출입이 불가능합니다.")