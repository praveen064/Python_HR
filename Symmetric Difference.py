Task 
Given  sets of integers, M and N, print their symmetric difference in ascending order. The term symmetric difference indicates those values that exist in either M or N but do not exist in both.

Input Format

The first line of input contains an integer,M . 
The second line contains M space-separated integers. 
The third line contains an integer, N. 
The fourth line contains N space-separated integers.

Output Format

Output the symmetric difference integers in ascending order, one per line.

Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12

Sol-0:
^ symbol can also be used to compute the symmetric difference of two sets.

M = input();m = input().split()
N = input();n = input().split()

print ("\n".join(sorted(list(set(m) ^ set(n)),key=int)))

Sol-1:

a,b = [set(input().split()) for _ in range(4)][1::2]
print ('\n'.join(sorted(a^b, key=int)))

explination: 

let's take it few by few:
[set(raw_input().split()) for _ in range(4)][1::2]

this one starts by reading the 4th fisrt lines:
[set(raw_input().split()) for _ in range(4)]

With the [...], those 4 inputs are stored in a list, which one is then explored by:
list[1::2]

This means [start:stop:step], like we start at list[1], stop at list[None] (this means we don't stop till the end of the list) and the step of the exploration is 2, so we got list[1], list[3], etc.

In our case, the list has length 4, so by list[1::2], we got members 2 and 4. Finally, with:
a,b = [set(raw_input().split()) for _ in range(4)][1::2]
the 2 lines are stored in variables a and b.

Then the print part:
print '\n'.join(sorted(a^b, key=int))

Here, 1st step is to calculate symmetric diff with the operator ^ . It's similar to a.symmetric_difference(b).
The result is sorted with the key int, means it uses int values of a^b members to sort them.

Finally, the:
'\n'.join(...)
means that all members of the collection in parameter are joined in a unique string, using '\n' as separator. If you had writen
'-'.join
then the separator would have been '-'.

Hope this was helpful :)
