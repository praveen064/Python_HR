#@Power - Mod Power:

Task 
You are given three integers: a, b, and m, respectively. Print two lines. 
The first line should print the result of pow(a,b). The second line should print the result of pow(a,b,m).

Input Format 
The first line contains a, the second line contains b, and the third line contains m.

Sample Input

3
4
5
Sample Output

81
1

Sol-0:
The operator pow(x, y, z) returns x to the power y, modulo z.

a = int(input())
b = int(input())
m = int(input())
print (a**b)
print (pow(a,b,m))

Sol-1:

a,b,m = [int(input()) for _ in '123']
print(pow(a,b),pow(a,b,m),sep='\n')