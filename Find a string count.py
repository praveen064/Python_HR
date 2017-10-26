#@Find a string count:

In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string. String traversal will take place from left to right, not from right to left.

NOTE: String letters are case-sensitive.

Input Format

The first line of input contains the original string. The next line contains the substring.

Constraints
Each character in the string is an ascii character.

Output Format
Output the integer number indicating the total number of occurrences of the substring in the original string.

Sample Input
ABCDCDC
CDC
Sample Output

2

Concept

Some string processing examples, such as these, might be useful. 
There are a couple of new concepts: 
In Python, the length of a string is found by the function len(s), where s is the string. 
To traverse through the length of a string, use a for loop:

for i in range(0, len(s)):
    print (s[i])
A range function is used to loop over some length:

range (0, 5)
Here, the range loops over 0 to 4. 5 is excluded.


Sol-0:
Approach 1 

Slice an x amount of string in each iteration of the loop. 

A = input().strip()
x = input().strip()

count = 0
for i in range(len(A) - len(x) + 1):
    if A[i:i+len(x)] == x:
        count += 1
print (count)

Approach 2 
This can be solved by using a regex.

import re
a = input()
b = input()
match = re.findall('(?='+b+')',a)
print (len(match))

Sol-1:

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)-len(sub_string)+1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count