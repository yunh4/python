s1 = {3, 2, 5, 1, 8, 4, 3} #집합으로 바로 선언 및 초기화
print(s1, type(s1))


str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str) 
print(s0, type(s0))

l = ['a', 'a', 'c', "goorm", "hello", 10, 30, 30]
print(l, type(l))

s1 = set(l) 
print(s1, type(s1))

d = {"Anna":25, "Bob": 23}
print(d, type(d))

s2 = set(d)
print(s2, type(s2))

t = (190,)
print(t, type(t))

s3 = set(t)
print(s3, type(s3))


str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str) 
print(s0, type(s0))

newstr = tuple(s0)
print(newstr, newstr[4], newstr[5:], type(newstr)) #인덱싱, 슬라이싱 가능

l = [1,2,3,4,5,6,7,8]
print(l, type(l))

s1 = set(l)
print(s1, type(s1))

newlist = list(s1)
print(newlist, newlist[4], newlist[:-5], type(newlist))


str = "Hello goorm!!!"
print(str, type(str))

s0 = set(str) 
print(s0, type(s0))

newstr = tuple(s0)
print(newstr, newstr[4], newstr[5:], type(newstr)) #인덱싱, 슬라이싱 가능

l = [1,2,3,4,5,6,7,8]
print(l, type(l))

s1 = set(l)
print(s1, type(s1))

newlist = list(s1)
print(newlist, newlist[4], newlist[:-5], type(newlist))