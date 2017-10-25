#@start() & end()

Q)Task:
Input Format

The first line contains the string . 
The second line contains the string .

Constraints

0 < len(S) < 100
0 < len(k) < len(S)

Output Format

Print the tuple in this format: (start _index, end _index). 
If no match is found, print (-1, -1).

Sample Input

aaadaa
aa
Sample Output

(0, 1)  
(1, 2)
(4, 5)


Sol-0:
We can solve this by using forward lookahead, together with start() and end().

import re
S = input()
k = input()
anymatch = 'No'
for m in re.finditer(r'(?=('+k+'))',S):
    anymatch = 'Yes'
    print((m.start(1),m.end(1)-1))
if anymatch == 'No':
    print((-1, -1))
	

Sol-1:
S = input()
k = input()
import re
pattern = re.compile(k)
r = pattern.search(S)
if not r: print ((-1, -1))
while r:
    print ("({0}, {1})".format(r.start(), r.end() - 1))
    r = pattern.search(S,r.start() + 1)
	
Sol-2:	
import re
s, k = input(), input()
matches = list(re.finditer(r'(?={})'.format(k), s))
if matches:
    print('\n'.join(str((match.start(),
          match.start() + len(k) - 1)) for match in matches))
else:
    print('(-1, -1)')
	

Sol-3:
Hello, you can use group in your lookahead assertion. 
Let's proceed by an example. We have input a_str = 'aaadaa' and substr='aa'. 
Parenthesis around substr at concatenation of the regex pattern p mean that we define group (aa) in pattern '(?=(aa))' for the Match object. 
group() is the Match object itself (empty string in this case), group(1) is the first group for this Match object, i.e. the lookahead. We define start and end of group(1) of the lookahead for every Match object returned by finditer().
	
import re

a_str = input()
substr = input()

p = re.compile(r"""
                    # zero-length match - empty string
(?=                 # positive lookahead assertion
(                   # group in lookahead to get start and end
"""+substr+"""      # concatenation to get pattern
)                   # closing parenthesis for lookahead group
)                   # closing parenthesis for lookahead assertion
""", re.VERBOSE)

if p.search(a_str):             # if there is any match
    for m in p.finditer(a_str): # for every Match object
        print((m.start(1), m.end(1)-1)) # start and end of group(1)
else:
    print((-1,-1))