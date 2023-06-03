year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('tian:\n'))
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 0 <= month <= 12:
    sun = months[month - 1]
else:
    print('data error')
sun += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sun += 1
print('今天是第', sun, '天')
