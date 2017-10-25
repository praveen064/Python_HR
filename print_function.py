##@Print Function##
Q)Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.

Input Format 
The first line contains an integer .

Output Format 
Output the answer as explained in the task.

Sample Input
3
Sample Output
123

Sol-0:

print(*range(1, int(input()) + 1), sep="")

#Using the map() and the print _function, we can solve this in one line.
#list(map(lambda x:print(x + 1, end=''), range(int(input()))))


Sol-1:

from __future__ import print_function
n = int(input())

#for i in range(1, n+1):print(i, end="")
#print(*range(1, n+1), sep='')
[print(i, end='') for i in range(1,n+1)]
