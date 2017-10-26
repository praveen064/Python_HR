#@Mutations:

Task 
Read a given string, change the character at a given index and then print the modified string.

Input Format 
The first line contains a string, . 
The next line contains an integer , denoting the index location and a character  separated by a space.

Output Format 
Using any of the methods explained above, replace the character at index  with character .

Sample Input

abracadabra
5 k
Sample Output

abrackdabra


Sol-0:
s = input()
i, k = input().split()
print (s[:int(i)] + k + s[int(i)+1:])