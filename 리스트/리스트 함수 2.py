evennumbers = [2, 4, 6, 8]
oddnumbers = [1, 3, 5, 7]
evennumbers.append(10)
print(evennumbers)

evennumbers.insert(0, 0) #맨 앞에 있는 0을 삽입
print(evennumbers)

evennumbers.extend(oddnumbers) #리스트끼리 합하는 것
print(evennumbers)
print(len(evennumbers))

evennumbers.sort()
print(evennumbers)