##@Python: Division##
Q)
Read two integers and print two lines. The first line should contain integer division, a // b. The second line should contain float division, a / b.
You don't need to perform any rounding or formatting operations.

Input Format 
The first line contains the first integer, . The second line contains the second integer, .

Output Format 
Print the two lines as described above.

Sample Input
4
3
sample Output
1
1.3333333333333333

Sol-0:
a = int(input())
b = int(input())

print(a // b)
print(a / b)

Sol-1:

if __name__ == '__main__':
    a = int(input())
    b = int(input())
    print(str(a//b), str(a/b))
    #print("\n".join([str(a//b),str(a/b)]))
