Q)Task 
Given an integer,n , and n  space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format
The first line contains an integer, , denoting the number of elements in the tuple. 
The second line contains  space-separated integers describing the elements in tuple .

Output Format
Print the result of hash(t).

Sample Input
2
1 2

Sample Output
3713081631934410656

Sol:
if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
	t = tuple(integer_list)
print the result
print hash(t)