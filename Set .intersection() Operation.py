#@Set .intersection() Operation:

Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. Your task is to find the total number of students who have subscribed to both newspapers.

Input Format

The first line contains n, the number of students who have subscribed to the English newspaper. 
The second line contains n space separated roll numbers of those students.
The third line contains b, the number of students who have subscribed to the French newspaper. 
The fourth line contains b space separated roll numbers of those students.

Output Format

Output the total number of students who have subscriptions to both English and French newspapers.

Sample Input
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
5

Explanation:
The roll numbers of students who have both subscriptions:
1,2,3,6, and 8.
Hence, the total is 5 students.

Sol-0:

Approach is:
STEP 1: Store the space separated input of roll numbers as sets in variables English and French.
STEP 2: Print the length of the intersection of sets English and French.

E = int(input())
English = set(input().split())

F = int(input())
French = set(input().split())

print (len(English & French))

Sol-1:

num1, st1, num2, st2 = (set(input().split()) for i in range(4))
print (len(st1.intersection(st2)))

