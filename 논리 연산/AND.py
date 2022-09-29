# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

input_id = input("아이디를 입력해주세요.\n")
input_pwd = input("비밀번호를 입력해주세요.\n")
real_id = "egoing"
real_pwd = "11"

#if를 중첩해서 사용한 예제
"""
if real_id == input_id:
    if real_pwd == input_pwd:
        print("Hello!")
    else:
        print("잘못된 비밀번호입니다")
else:
    print("잘못된 아이디입니다")
"""


#and로 통합한 예제
if real_id == input_id and real_pwd == input_pwd:
    print("Hello!")
else:
    print("로그인에 실패했습니다")