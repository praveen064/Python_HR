#@Validating phone numbers

Let's dive into the interesting topic of regular expressions! You are given some input, and you are required to check whether they are valid mobile numbers.

A valid mobile number is a ten digit number starting with a 7,8 or 9.

Concept:
A valid mobile number is a ten digit number starting with a 7,8 or 9.

Regular expressions are a key concept in any programming language. A quick explanation with Python examples is available here. You could also go through the link below to read more about regular expressions in Python.

https://developers.google.com/edu/python/regular-expressions

Input Format
The first line contains an integer N, the number of inputs.
 lines follow, each containing some string.


Output Format

For every string listed, print "YES" if it is a valid mobile number and "NO" if it is not on separate lines. Do not print the quotes.

Sample Input
2
9587456281
1252478965

Sample Output
YES
NO

Sol-0:
We can solve this using regex. 

[789] : match a single digit 7,8 or 9. 
\d{9} : match 9 digits.

import re
for i in range(int(input())):
    print ('YES' if re.search(r"^[789]\d{9}$",raw_input()) else 'NO')

Sol-1:
import re
N = int(input())

for i in range(N):
    print ('YES')  if re.match(r'^(7|8|9)[0-9]{9}$' , input()) else print('NO')
#print('YES' if bool(re.match(r'^[789]{1}[0-9]{9}$',input())) == True else 'NO')


