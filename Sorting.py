#@Sorting:


You are given a string S. 
S contains alphanumeric characters only. 

Your task is to sort the string S in the following manner:

All sorted lowercase letters are ahead of uppercase letters.
All sorted uppercase letters are ahead of digits.
All sorted odd digits are ahead of sorted even digits.

Input Format

A single line of input contains the string S.

Output Format

Output the sorted string S.

Sample Input

Sorting1234
Sample Output

ginortS1324
Note: 
a) Using join, for or while anywhere in your code, even as substrings, will result in a score of 0. 
b) You can only use one sorted function in your code. A 0 score will be awarded for using sorted more than once. 

Hint: Success is not the key, but key is success.


Sol-0:

Without using key:
from __future__ import print_function

upper = []
lower = []
even = []
odd = []

def separator(a):
    
    if a.isalpha():
        if a.isupper():
            upper.append(a)
        else:
            lower.append(a)
    else:
        if int(a)%2 == 0:
            even.append(a)
        else:
            odd.append(a)
    return 
    
map(separator,raw_input())       

upper.sort()
lower.sort()
even.sort()
odd.sort()

t = lower+upper+odd+even
map(lambda x: print(x,end=''),t)

Sol-1:

from __future__ import print_function

def func(x): 
    if x.isalpha():
        if x.isupper():
            return (ord(x)-ord('A'))
        else:
            return (ord(x)-ord('a'))-30
    else:
        if int(x) % 2 == 0:
            return 60+int(x)
        else:
            return 30+int(x)

s = input()        
map(lambda x: print(x,end=''),(sorted(s,key = func)))
