import datetime
import sys

input = sys.stdin.readline
answer = ["MON","TUE","WED","THU","FRI","SAT","SUN"]

month,day = map(int,input().split())

print( answer[datetime.date(2007,month,day).weekday()] )
