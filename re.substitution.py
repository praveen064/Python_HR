@#Regex Substitution##

Q)Task
You are given a text of  lines. The text contains && and || symbols. 
Your task is to modify those symbols to the following:

&& → and
|| → or
Both && and || should have a space " " on both sides.

Input Format

The first line contains the integer, N. 
The next N lines each contain a line of the text.

Constraints


Neither && nor || occur in the start or end of each line.

Output Format

Output the modified text.

Sample Input

11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
Sample Output

a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b)) 
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.    


Sol-0:
One can solve this challenge by using the re.sub() tool along with (?<= ) which is a positive lookbehind that makes sure that the pattern is preceded by a space. Also, by using (?= ) which is a positive lookahead that makes sure that the pattern is followed by a space.

import re

for line in range(int(input())):
    string = ''
    string = re.sub(r'(?<= )&&(?= )','and',input())
    string = re.sub(r'(?<= )\|\|(?= )','or',string)
    print (string)

Sol-1:
import re
N = int(input())
for _ in range(N):
    print(re.sub(r'(?<= )(\&\&|\|\|)(?= )', (lambda m: 'and' if m.group(1) == '&&' else 'or'), input()))

Sol-2:	
two pass solved overlapping problem
import re

for _ in range(int(input())):
    S=re.sub(' \|\| ', ' or ', re.sub(' && ', ' and ', input())) 
    print (re.sub(' \|\| ', ' or ', re.sub(' && ', ' and ', S)))
	
This is the overlapping problem:
Supose you are looking for the pattern #A# in this string: #A#A# r'#A#' will match the first #A#, but wont match the second, because the middle # was consumed in the first match (our pattern overlaps the two matches).
I solved it by making a first pass of substitutions, and later a second pass. another way of solving it would be using read ahead patterns, that wont consume the matched string, like this `r'#A(?=#)'
Test it in http://pythex.org/, its great to develop regex in python

Sol-3:
for _ in range(int(input())):
    line = input()
    
    while ' && ' in line or ' || ' in line:
        line = line.replace(" && ", " and ").replace(" || ", " or ")
    
    print(line)