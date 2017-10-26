#@sWAP cASE: 
You are given a string . Your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

For Example:

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2

Input Format
A single line containing a string S.

Output Format
Print the modified string S.

Sample Input

HackerRank.com presents "Pythonist 2".
Sample Output

hACKERrANK.COM PRESENTS "pYTHONIST 2".

Sol-0:
Use the method string.swapcase(s) to swap lower case letters to upper case letters and vice versa.

To learn more, visit:
https://docs.python.org/2/library/string.html#string.swapcase

import string
print string.swapcase(input())

Sol-1:
def swap_case(s): 
	return s.swapcase()

Sol-2:	
def swap_case(s):
    result = ""
    for letter in s:
        if letter == letter.upper():
            result += letter.lower()
        else:
            result += letter.upper()
    return result