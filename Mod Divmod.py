#@Mod Divmod:
One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b first and then the remainder a.

For example:

>>> print divmod(177,10)
(17, 7)
Here, the integer division is 177/10 => 17 and the modulo operator is 177%10 => 7.

Task 
Read in two integers, a and b, and print three lines. 
The first line is the integer division a//b (While using Python2 remember to import division from __future__). 
The second line is the result of the modulo operator: a%b. 
The third line prints the divmod of a and b.

Input Format 
The first line contains the first integer, a, and the second line contains the second integer, b.

Output Format 
Print the result as described above.

Sample Input

177
10
Sample Output

17
7
(17, 7)

Sol-0:
The operator divmod takes two (non-complex) numbers as arguments and returns a pair of numbers consisting of their quotient and remainder when using long division.

a = int(input())
b = int(input())
print (a/b)
print (a%b)
print (divmod(a,b))

Sol-1:

print('{0}\n{1}\n({0}, {1})'.format(*divmod(int(input()), int(input()))))

Explination:

FJSevilla is using the string format method.
The things in the curly braces (i.e. {}), are references to the items in the format() method parentheses. The '\n' means line break. The * means unpack.
The first int(input()) will take the 177 (using the first example), and the second one will take the 10. Those numbers will go into the divmod function. The divmod function will produce a tuple that looks like (17, 7).
When that's unpacked you get a 17 and then a 7 and these are printed with a line break separating them.

