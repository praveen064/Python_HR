@#Validating Roman Numerals##

Q)You are given a string, and you have to validate whether it's a valid Roman numeral. If it is valid, print True. Otherwise, print False. Try to create a regular expression for a valid Roman numeral.

Input Format

A single line of input containing a string of Roman characters.

Output Format

Output a single line containing True or False according to the instructions above.

Constraints

The number will be between  and  (both included).

Sample Input

CDXXI
Sample Output

True

Sol-0:
We can use the regular expression: ^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$.

import re
print bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$",raw_input()))

Sol-1:
import re
thousand = 'M{0,3}'
hundred = '(C[MD]|D?C{0,3})'
ten = '(X[CL]|L?X{0,3})'
digit = '(I[VX]|V?I{0,3})'
print (bool(re.match(thousand + hundred+ten+digit +'$', input())))

Sol-2:
import re
m = re.match(r'M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$', input())
print (bool(m))

Sol-3:
import roman
x=input()
try:
    if (roman.fromRoman(x)>0 and roman.fromRoman(x)<4000):
        print("True")
    else:
        print("False")
except:
    print("False")
	
	
	
#https://stackoverflow.com/questions/267399/how-do-you-match-only-valid-roman-numerals-with-a-regular-expression