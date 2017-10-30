Task
You have a non-empty set , and you have to execute  commands given in  lines.

The commands will be pop, remove and discard.

Input Format

The first line contains integer n , the number of elements in the set s. 
The second line contains n space separated elements of set s. All of the elements are non-negative integers, less than or equal to 9. 
The third line contains integer N, the number of commands.
The next N lines contains either pop, remove and/or discard commands followed by their associated value.

Output Format

Print the sum of the elements of set s on a single line.

Sample Input

9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5
Sample Output

4
Explanation

After completing these 10 operations on the set, we get set([4]). Hence, the sum is 4.

Note: Convert the elements of set s to integers while you are assigning them. To ensure the proper input of the set, we have added the first two lines of code to the editor.


Sol-0:

The approach is:
Step 1: Store the space separated input of elements in set s.
Step 2: Run a loop N times and store the commands in variable a.
Step 3: Using conditionals, execute the appropriate commands on set s.
Step 4: Print the sum of set s.


n = int(input())
s = set([int(x) for x in input().strip().split()]) 
for _ in range(int(input())):

    a = list(input().strip().split())

    if a[0] == 'pop':
        s.pop()
    elif a[0] == 'discard':
        s.discard(int(a[1]))
    else:
        s.remove(int(a[1]))

print (sum(s))
   

Sol-1:
n = int(input())
s = set(map(int, input().split())) 
for i in range(int(input())):
    eval('s.{0}({1})'.format(*input().split()+['']))

print(sum(s))