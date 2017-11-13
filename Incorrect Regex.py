#@Incorrect Regex:

You are given a string S. 
Your task is to find out whether S is a valid regex or not.

Input Format

The first line contains integer T, the number of test cases. 
The next T lines contains the string S.

Output Format

Print "True" or "False" for each test case without quotes.

Sample Input

2
.*\+
.*+
Sample Output

True
False
Explanation

.*\+ : Valid regex. 
.*+: Has the error multiple repeat. Hence, it is invalid.

Sol-0:
Inside the try statement, we can re.compile the input string. If the compilation of regex fails, then the except would handle the output.

import re
for i in range(int(input())):
    try:
        s = input()
        re.compile(s)
    except:
        print (False)
        continue
    print (True)
	
Sol-1:

import re
for _ in range(int(input())):
    ans = True
    try:
        reg = re.compile(input())
    except re.error:
        ans = False
    print(ans)