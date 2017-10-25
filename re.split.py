--> re.split()

The re.split() expression splits the string by occurrence of a pattern.

Code

>>> import re
>>> re.split("-","+91-011-2711-1111")
['+91', '011', '2711', '1111']

Q)Task 
You are given a string , containing , and/or . and 0-9 digits. 
Your task is to re.split() all of the , and . symbols.

Input Format

A single line of input containing the string .

Output Format

Print the numbers obtained after splitting the string on separate lines.

Sample Input

100,000,000.000
Sample Output

100
000
000
000

Sol-0:
The expression, [.,], matches the . or , symbol in the string .
import re

for i in re.split(r'[.,]',raw_input()):
    if i.isdigit():
        print i

Sol-1:
import re
print(*filter(any, re.split(r'[.,]+', input())), sep='\n')
#print(*re.split(r'[.,]+', input().strip('., ')), sep='\n')
#print("\n".join(i for i in re.split('[,.]*', input())).strip())

* takes a list and "unpacks" it into separate arguments.
list = [1,2,3]
print(*list, sep=",")
is equivalent to
print(1,2,3, sep=",")

