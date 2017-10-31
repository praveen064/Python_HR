You are given 2 timestamps in the format given below:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.

Input Format

The first line contains T, the number of testcases. 
Each testcase contains 2 lines, representing time t1 and time t2 .

Output Format

Print the absolute difference (t1-t2) in seconds.

Sample Input 0

2
Sun 10 May 2015 13:54:36 -0700
Sun 10 May 2015 13:54:36 -0000
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000
Sample Output 0

25200
88200
Explanation 0

In the first query, when we compare the time in UTC for both the time stamps, we see a difference of 7 hours. which is 7 * 3600 seconds or 25200 seconds.

Similarly, in the second query, time difference is 5 hours and 30 minutes for time zone adjusting for that we have a difference of 1 day and 30 minutes. Or 24 * 3600 + 30 * 60 = 88200


Sol-0:				   
In this challenge, our goal is the first convert the time stamp to UNIX time stamps that are independent of timezones. After that we simply subtract and print the difference.
To solve this in python you can use the python package called datetime and it has a function called strptime. Using which we can get a time object.
Refer : datetime.strptime 
This tool returns a date time corresponding to a date string, parsed according to format.


from datetime import datetime

for i in range(int(input())):
    t1 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    t2 = datetime.strptime(input(), '%a %d %b %Y %H:%M:%S %z')
    print(abs(int((t1-t2).total_seconds())))
	
	
Sol-1:
from datetime import datetime as dt


fmt = '%a %d %b %Y %H:%M:%S %z'
for i in range(int(input())):
    print(int(abs((dt.strptime(input(), fmt) - 
                   dt.strptime(input(), fmt)).total_seconds())))