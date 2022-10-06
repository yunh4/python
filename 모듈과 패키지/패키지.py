class ThilandPackage:
    def detail(self):
        print("[태국 패키티 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원");
				
class VietnamPackage:
    def detail(self):
        print("[베트남 패키티 3박 5일] 방콕, 다닝 효도 여행 60만원");
				
__all__ = ["Vietnam", "Thailand"]

import Travel.Thailand

trip_to = Travel.Thailand.ThailandPackage()
trip_to.datail()

import Travel.Vietnam

trip_to = Travel.Vietnam.VietnamPackage()
trip_to.datail()

from Travel import *
trip_to = Vietnam.VietnamPackage()
trip_to.datail()