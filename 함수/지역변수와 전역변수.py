gun = 10

def checkpoint(soldier) : # 경계 근무
	global gun
	gun = gun - soldier
	print("[함수 내] 남은 총 : {0}" .format(gun))
	
print("전체 총 : {0}" .format(gun))
checkpoint(2) # 2명이 경게 근무 나감
print("남은 총 : {0}" .format(gun))