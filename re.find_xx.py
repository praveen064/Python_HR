##@Re.findall() & Re.finditer()##

Q)Task 
You are given a string . It consists of alphanumeric characters, spaces and symbols(+,-). 
Your task is to find all the substrings of  that contains  or more vowels. 
Also, these substrings must lie in between  consonants and should contain vowels only.

Note : 
Vowels are defined as: AEIOU and aeiou. 
Consonants are defined as: QWRTYPSDFGHJKLZXCVBNM and qwrtypsdfghjklzxcvbnm.

Input Format

A single line of input containing string .

Constraints


Output Format

Print the matched substrings in their order of occurrence on separate lines. 
If no match is found, print -1.

Sample Input

rabcdeefgyYhFjkIoomnpOeorteeeeet
Sample Output

ee
Ioo
Oeo
eeeee

Explanation

ee is located between consonant d and .f 
Ioo is located between consonant k  and m. 
Oeo is located between consonant p and r. 
eeeee is located between consonant t and t.


Sol-0:
import re
consonants = 'qwrtypsdfghjklzxcvbnm'
vowels = 'aeiou'
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',input(),flags = re.I)
if match:
    for i in match:
        print (i)
else:
    print (-1)

Sol-1:
The regexes I saw can be shortened using either a positive lookbehind or a positive lookahed. I don't think it can be solved without them because you have to avoid consuming the input somewhere (before or after).
Using the positive lookbehind:

import re
v = "aeiou"
c = "qwrtypsdfghjklzxcvbnm"
m = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (c, v, c), input(), flags = re.I)
print('\n'.join(m or ['-1']))

Using the positive lookahead, same as above with the regex:
[%s]([%s]{2,})(?=[%s])


Sol-2:
import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))


Sol-3:
import re

s = input()
match = re.findall(r'[^aeiou]([aeiou]{2,})(?=[^aeiou])', s, re.I)
print(*match or [-1], sep = '\n')

Sol-4:
import re
m = re.findall(r'([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})+([QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])',input())
for i in m:
    print i[1]

