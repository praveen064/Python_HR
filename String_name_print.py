#@What's Your Name:

You are given the firstname and lastname of a person on two different lines. Your task is to read them and print the following:

Hello firstname lastname! You just delved into python.
Input Format

The first line contains the first name, and the second line contains the last name.

Constraints

The length of the first and last name ≤ .

Output Format

Print the output as mentioned above.

Sample Input

Guido
Rossum
Sample Output

Hello Guido Rossum! You just delved into python.
Explanation

The input read by the program is stored as a string data type. A string is a collection of characters.

Sol-0:

a = input()
b = input()
print("Hello %s %s! You just delved into python." % (a,b))
'''
a = input()
b = input()
print ("Hello " + a + " " + b + "! You just delved into python.")
'''

Sol-1:

print ("Hello {0} {1}! You just delved into python.".format(input(), input()))