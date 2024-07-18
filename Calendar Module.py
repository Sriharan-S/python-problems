# www.hackerrank.com/challenges/calendar-module/

import calendar
a = str(input())
a = a.split(" ")
print((calendar.day_name[calendar.weekday(int(a[2]), int(a[0]), int(a[1]))]).upper())
