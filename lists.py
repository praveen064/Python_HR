Q) Task:
Input Format

The first line contains an integer, , denoting the number of commands. 
Each line  of the  subsequent lines contains one of the commands described above.

Output Format
For each command of type print, print the list on a new line.

Sample Input
12
insert 0 5
insert 1 10
insert 0 6
print 
remove 6
append 9
append 1
sort 
print
pop
reverse
print
Sample Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]

Sol: 
if __name__ == '__main__':
    T = int(input().strip())
L = []
for t in range(T):
    args = input().strip().split(" ")
    if args[0] == "print":
        print (L)
    elif len(args) == 3:
        getattr(L, args[0])(int(args[1]), int(args[2]))
    elif len(args) == 2:
        getattr(L, args[0])(int(args[1]))
    else:
        getattr(L, args[0])()