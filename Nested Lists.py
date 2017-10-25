#@Nested Lists

Given the names and grades for each student in a Physics class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, N, the number of students. 
The 2N subsequent lines describe each student over 2 lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.

Sample Input

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
Sample Output

Berry
Harry
Explanation

There are 5 students in this class whose names and grades are assembled to build the following list:

students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
The lowest grade of 37.2  belongs to Tina. The second lowest grade of 37.21 belongs to both Harry and Berry, so we order their names alphabetically and print each name on a new line.

Sol-0:
We can solve this challenge by using nested list.

a = [[input(), float(input())] for i in range(int(input()))]
s = sorted(set([x[1] for x in a]))
for name in sorted(x[0] for x in a if x[1] == s[1]):
    print (name)
	
Sol-1:
if __name__ == '__main__':
    final = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        final.append([score,name])
final.sort()
k = 0
for x in range(n):
    if final[x][0] > final[0][0]:
        k = x
        break
for x in range(n):
    if final[k][0] == final[x][0]:
        print(final[x][1])
		
		
