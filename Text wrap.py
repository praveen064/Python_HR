#@Textwrap:

Task

You are given a string S and width w. 
Your task is to wrap the string into a paragraph of width w.

Input Format

The first line contains a string, S. 
The second line contains the width, w.

Constraints
0 < len(S) < 1000 
0 < w < len(S)
 

Output Format

Print the text wrapped paragraph.

Sample Input

ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
Sample Output

ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ  


Sol-0:
This can be solved using the function textwrap.fill().

import textwrap
S = input()
w = input()
print (textwrap.fill(S,w))

Sol-1:
without using textwrap

s=input().strip()
w=int(input())
for i in range(0,len(s),w):
    print(s[i:w+i])
