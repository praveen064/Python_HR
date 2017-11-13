Input Format

The first line contains N and M separated by a space. 
The next N lines each contain M elements. 
The last line contains K.

Output Format

Print the N lines of the sorted table. Each line should contain the space separated elements. Check the sample below for clarity.

Sample Input

5 3
10 2 5
7 1 0
9 9 9
1 23 12
6 5 9
1
Sample Output

7 1 0
10 2 5
6 5 9
9 9 9
1 23 12
Explanation

The table is sorted on the second attribute shown as K = 1 because it's 0-indexed.

Sol-0:
Use the sorted() function with key = lambda x: x[k]



Sol-1:

N, M = map(int, input().split())
rows = [input() for _ in range(N)]
K = int(input())

for row in sorted(rows, key=lambda row: int(row.split()[K])):
    print(row)

