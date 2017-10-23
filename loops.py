##@Loops##	
=======
Notes:
=======
There are two kinds of loops in Python.
A for loop:
for i in range(0, 5):
    print i
And a while loop:
i = 0
while i < 5:
    print i
    i += 1
	
Q)Task 
Read an integer N. For all non-negative integers i<N, print i^2. See the sample for details.(Constraints 1<=N<=20)
Input Format

The first and only line contains the integer, .

Output Format
Print  lines, one corresponding to each .

Sample Input
5
Sample Output
0
1
4
9
16

Sol:

if __name__ == '__main__':
    n = int(input())

    
print(*[num**2 for num in range(n)], sep='\n')  #https://docs.python.org/3/tutorial/controlflow.html#arbitrary-argument-lists

#[print(i**2) for i in range(n) if n in range(1, 21)]
    
""""
for i in range(0, 20):
    i = 0
while i < 5:
    print (i**2)
    i += 1
"""