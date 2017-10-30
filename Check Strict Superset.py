#@Check Strict Superset:

You are given a set A and n other sets. 
Your job is to find whether set A is a strict superset of each of the N sets.

Print True, if A is a strict superset of each of the N sets. Otherwise, print False.

A strict superset has at least one element that does not exist in its subset.

Example 
Set([1,3,5]) is a strict superset of set([1,3]). 
Set is not a strict superset of set. 
Set is not a strict superset of set.

Input Format

The first line contains the space separated elements of set A. 
The second line contains integer n, the number of other sets. 
The next n lines contains the space separated elements of the other sets.

Constraints

Output Format

Print True if set  is a strict superset of all other  sets. Otherwise, print False.

Sample Input 0

1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
Sample Output 0

False
Explanation 0

Set A is the strict superset of the set([1,2,3,4,5]) but not of the set([100,11,12]) because 100 is not in set A. 
Hence, the output is False.

Sol-0:
set > otherSet

This tool tests whether the set is a proper(strict) superset of the other set like this: set >= otherSet and set != otherSet.

For Example:
print set([2, 9, 7, 1]) > set([1, 7]) #Output: True 
print set([2, 9, 7, 1]) > set([1, 2, 7, 9]) #Output: False

A = set(input().split());
print (all(map(lambda x: (A > x), [set(input().split()) for i in range(int(input()))])))

Sol-1:
a = set(input().split())
print(all(a > set(input().split()) for _ in range(int(input()))))

