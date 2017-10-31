#@Calendar Module:

The calendar module allows you to output calendars and provides additional useful functions for them.

class calendar.TextCalendar([firstweekday])

This class can be used to generate plain text calendars.

Sample Code

>>> import calendar
>>> 
>>> print calendar.TextCalendar(firstweekday=6).formatyear(2015)


Task

You are given a date. Your task is to find what the day is on that date.

Input Format

A single line of input containing the space separated month, day and year, respectively, in MM|DD|YYYY  format.

Output Format

Output the correct day in capital letters.

Sample Input

08 05 2015

Sample Output

WEDNESDAY

Explanation
The day on August 5th 2015 was WEDNESDAY.

Sol-0:
calendar.weekday(year, month, day)
This tool returns the day of the week (0 is Monday) for year (1970–...), month (1-12), day (1-31). 

Learn more about calendars here: https://docs.python.org/2/library/calendar.html


import calendar

day = {0:'MONDAY', 1:'TUESDAY', 2:'WEDNESDAY', 3:'THURSDAY', 4:'FRIDAY', 5:'SATURDAY', 6:'SUNDAY'}

m,d,y = map(int,input().split())
print (day[calendar.weekday(y,m,d)])


Sol-1:

import calendar
#calendar.Calendar(calendar.SUNDAY)
user_input = input().split()
month = int(user_input[0])
day = int(user_input[1])
year = int(user_input[2])
c = calendar.weekday(year, month, day)

if c == 0:
    print("MONDAY")
elif c == 1:
    print("TUESDAY")
elif c == 2:
    print("WEDNESDAY")
elif c==3:
    print("THURSDAY")
elif c==4:
    print("FRIDAY")
elif c== 5:
    print("SATURDAY")
elif c==6:
    print("SUNDAY")