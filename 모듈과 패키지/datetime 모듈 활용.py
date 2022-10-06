import datetime as dt

print('오늘 =', dt.datetime.now())
hundred = dt.timedelta(days = 100)
plus100day = dt.datetime.now() + hundred
print('100일 후 =', plus100day)

minus100day = dt.datetime.now() - hundred
print('100일 전 =', minus100day)

week = dt.timedelta(weeks = 1)
nextweek = dt.datetime.now()+week
print('1주일 후 =', nextweek)