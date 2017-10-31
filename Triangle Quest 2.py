#@Triangle Quest 2:
You are given a positive integer N. 
Your task is to print a palindromic triangle of size N.

For example, a palindromic triangle of size 5 is:

1
121
12321
1234321
123454321
You can't take more than two lines. The first line (a for-statement) is already written for you. 
You have to complete the code using exactly one print statement.

Note: 
Using anything related to strings will give a score of 0. 
Using more than one for-statement will give a score of 0.

Input Format

A single line of input containing the integerN.

Constraints

Output Format

Print the palindromic triangle of size N as explained above.

Sample Input

5
Sample Output

1
121
12321
1234321
123454321

Sol-0:

It is interesting to note that for integers greater than 0 and less than 10.

(10^1 / 9) = 1 
(10^2 / 9) = 11
(10^3 / 9) = 111 
(10^4 / 9) = 1111 
(10^5 / 9) = 11111 
(10^6 / 9) = 111111 
(10^7 / 9) = 1111111 
(10^8 / 9) = 11111111 
(10^9 / 9) = 111111111

and
1 * 1 = 1 
11 * 11 = 121
111 * 111 = 12321
1111 * 1111 =  1234321
11111 * 11111 = 123454321
111111 * 111111 = 12345654321
1111111 * 1111111 = 1234567654321

Sol:
for i in xrange(1,int(raw_input())+1):
    print (10**i/9)**2
	
Another Method 01:
for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print  reduce(lambda x, y: x + (10 ** (y - 1)), range(1, i + 1))**2
	
Another Method 02:
for i in range(1,int(raw_input())+1): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print [1, 121, 12321, 1234321, 123454321, 12345654321,1234567654321, 123456787654321, 12345678987654321][i-1]
	
Sol-1:
for x in range(1,int(input())+1):
    print(((10**x - 1)//9)**2)
	