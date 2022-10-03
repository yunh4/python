# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
print(dic1)
print(type(dic1))
print(dic1["apple"])

dic2 = dict(apple = "사과", bird = "새", bug = "벌레")
print(dic2)

dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
print(dic1)

del dic1["bug"]
print(dic1)

dic = {"num":3}
dic["num"] = 4

#dic[[1]] = True -> 리스트는 key로 저장할 수 없음
dic[False] = 0

#value는 어느 값이든 저장 가능
dic[True] = [1, 10, 100] 
dic["nums"] = {"one":1, "two":2}
print(dic)