@#Group(), Groups() & Groupdict()

Q)Task

You are given a string . 
Your task is to find the first occurrence of an alphanumeric character in  (read from left to right) that has consecutive repetitions.

Input Format

A single line of input containing the string .

Constraints

0 < len(S) < 100
Output Format

Print the first occurrence of the repeating character. If there are no repeating characters, print -1.

Sample Input
..12345678910111213141516171820212223
Sample Output
1

Hint:
[A-Za-z0-9])\1+ can be used to solve this problem. 
The expression ([A-Za-z0-9]) will match an alphanumeric character and store it in group . 
The expression \1 matches the exact same text that was matched by the first capturing group.

Sol-0:
import re
m = re.search(r'([A-Za-z0-9])\1+',input())
if m:
    print (m.group(1))
else:
    print (-1)


Sol-1: import re
m = re.search(r'([a-zA-Z0-9])\1+', input().strip())
print(m.group(1) if m else -1)

so if I wanted to match the second appearing alphanumeric, which appears more than one time, how would I do it?

m = re.findall(r"([A-Za-z0-9])\1+",input())
print(m[1])


Sol-2:
import re
m = re.search(r'([a-zA-Z0-9])\1', input())
if m:
    print (m.group(1))
else:
    print (-1)