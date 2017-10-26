#@Capitalize:

You are given a string S. Your task is to capitalize each word of S.

Input Format

A single line of input containing the string, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

hello world
Sample Output

Hello World

Sol-1:
import string 
print(string.capwords(input(), ' '))

Sol-2: print(input().title()) will not work because the question is asking to capitalise firse letter of each word keeping in mind that "if it is a letter". Title and Capitalise are different in function as:
'abcd'.title()
results in 'Abcd' but 
'12abcd'.title()
results in '12Abcd'. This is not what we want. 

We just want to capitalise first letter of each word, not the first occuring letter of a word. 
Instead, use this: 
s = input()
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)


Sol-0-x:
This can be solved using split, join and capitalize.

print (' '.join(word.capitalize() for word in input().split(' ')))

  

