# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import random
luckyNum = random.sample(range(1, 45), 6)
luckyNum.sort()

while True :
	bonus = random.sample(range(1, 45), 1)
	if bonus not in luckyNum :
		print(f'행운 번호 {luckyNum} 보너스 번호 {bonus}')
		import sys
		sys.exit()