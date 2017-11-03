Input Format

The first line contains a single integer T, the number of test cases. 
For each test case, there are 2 lines. 
The first line of each test case contains N, the number of cubes. 
The second line contains N space separated integers, denoting the sideLengths of each cube in that order.

Output Format
For each test case, output a single line containing either "Yes" or "No" without the quotes.

Sample Input
2
6
4 3 2 1 3 4
3
1 3 2

Sample Output
Yes
No

Explanation
In the first test case, pick in this order: left - 4, right - 4, left - 3, right - 3, left - 2, right - 1. 
In the second test case, no order gives an appropriate arrangement of vertical cubes. 3 will always come after either 1 or 2.

Sol-0:
In this problem we'll use a greedy approach and deque (Note that you can also use 2 pointers)
Keep a current variable then compare the largest element of both left and right of the main array and see if it's smaller than the current. This way you'll continue to add element in new array. See code below for implementation.

from collections import deque 
import sys
for _ in range(input()):
    n = input()
    arr = map(int,raw_input().split())
    for i in arr:
        assert i<=2**31 - 1
    lst = deque(arr)

    curr = 9999999999999999
    flag = 0
    if (len(lst)<=2):
        print "Yes"
        continue
    left = lst.popleft()
    right = lst.pop()
    latest = -1
    while (len(lst)>0):
        flag = 0
        if (left >= right and left <= curr):
            curr = left
            left = lst.popleft()
            latest = left
            flag = 1
        elif (right> left and right <= curr):
            curr = right
            right = lst.pop()
            latest = right
            flag = 1
        if flag == 0:
            break
    if len(lst)>0 or latest > curr:
        print "No"
    else:
        print "Yes"

Sol-1:

for t in range(input()):
    input()
    lst = map(int, raw_input().split())
    l = len(lst)
    i = 0
    while i < l - 1 and lst[i] >= lst[i+1]:
        i += 1
    while i < l - 1 and lst[i] <= lst[i+1]:
        i += 1
    print "Yes" if i == l - 1 else "No"