#@Check Subset:

You are given two sets, A and B. 
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

Input Format

The first line will contain the number of test cases, T. 
The first line of each test case contains the number of elements in set A.
The second line of each test case contains the space separated elements of set A.
The third line of each test case contains the number of elements in set B.
The fourth line of each test case contains the space separated elements of set B.

Output Format

Output True or False for each test case on separate lines.

Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
Explanation

Test Case 01 Explanation

Set  A= {1 2 3 5 6} 
Set  B= {9 8 5 6 3 2 1 4 7} 
All the elements of set A are elements of set B. 
Hence, set A is a subset of set B.

Sol-0:
.issubset() or <=

These tools return whether the set is a subset of the set of elements in an iterable. 

For example:
print set([2, 9, 7, 1]).issubset(set([1, 7])) #Output: False
print set([2, 9, 7, 1]).issubset(set([1, 2, 3, 4, 5, 6, 7, 8, 9])) #Output: True


Complexity analysis of issubset() can be found here:
http://stackoverflow.com/questions/27674289/the-complextiy-of-python-issubset


for i in range(int(input())): #More than 4 lines will result in 0 score. Blank lines won't be counted.  
    a = int(input()); A = set(input().split())
    b = int(input()); B = set(input().split())
    print (A <= B)

