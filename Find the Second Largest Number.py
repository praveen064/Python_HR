#@Find the Second Largest Number
You are given n numbers. Store them in a list and find the second largest number.

Input Format

The first line contains n. The second line contains an array A[] of n integers each separated by a space.

Output Format

Print the value of the second largest number.

Sample Input 0

5
2 3 6 6 5
Sample Output 0

5
Explanation 0

Given list is [2,3,6,6,5]. The maximum number is 6, second maximum is 5. Hence, we print 5 as our answer.

Sol-1:

n = int(input())

nums = map(int, input().split())	
print (sorted(list(set(nums)))[-2])

Sol-2:
Transform the list to a set and then list again, removing all the duplicates. Then sort the list and print the second last element.

from collections import Counter
if __name__ == '__main__':
    n = int(input())
    arr = list(set(map(int, input().split())))
    arr.sort()
    print (arr[-2])