#@Triangle Quest:
You are given a positive integer N. Print a numerical triangle of height N-1 like the one below:

1
22
333
4444
55555
......
Can you do it using only arithmetic operations, a single for loop and print statement?

Use no more than two lines. The first line (the for statement) is already written for you. You have to complete the print statement.

Note: Using anything related to strings will give a score of 0.

Input Format 
A single line containing integer, N.

Constraints 

Output Format 
Print N-1 lines as explained above.

Sample Input

5
Sample Output

1
22
333
4444

Sol-0:
For integers greater than 0 and less than 10, examine below: 
	
(10^1 / 9) * 1 = 1 
(10^2 / 9) * 2 = 22
(10^3 / 9) * 3 = 333
(10^4 / 9) * 4 = 4444
(10^5 / 9) * 5 = 55555
(10^6 / 9) * 6 = 666666
(10^7 / 9) * 7 = 7777777
(10^8 / 9) * 8 = 88888888
(10^9 / 9) * 9 = 999999999

for i in range(1,input()): 
    print  i * 10**i / 9

Sol-1:

for i in range(1,int(input())):
    print([0, 1, 22, 333, 4444, 55555, 666666, 7777777, 88888888, 999999999][i])