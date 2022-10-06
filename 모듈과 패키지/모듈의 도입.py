#일반 가격
def price(people) :
	print("{0} 명 가격은 {1} 원 입니다".format(people, people*10000))

#조조할인 가격
def price_morning(people) :
	print("{0} 명 조조할인 가격은 {1} 원 입니다".format(people, people*6000))
	
#군인 할인 가격
def soldier(people) :
	print("{0} 명 군인 할인 가격은 {1} 원 입니다".format(people, people*4000))
	
import theater_module as tm
# theater_module.price(3)
# theater_module.price_morning(4)
# theater_module.soldier(5)

tm.price(3)
tm.price_morning(4)
tm.soldier(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price_soldier as price
# price(5)