##@Tuples##
Here is how I broke this down:
We need to read the first line of input to get it out of the way (it can be used to write a parser for the next line, but it isn't useful)
n = raw_input()
Read in the second line -- this is just a single string ex. '1 2 3 4'
input_line = raw_input()
Split the string by whitespace into a list
input_list = input_line.split()
Note: This is a list of strings ex. ['1', '2', '3', '4'] But we want a list of integers ex. [1, 2, 3, 4]
We need to convert the list elements from strings to ints
[Simple] Option 1 (since we know the number of elements, n):
    for i in xrange(n):
        input_list[i] = int(input_list[i])
[Simple] Option 2 (if we are ignoring the first input line for some reason):
    for i in xrange(len(input_list)):
        input_list[i] = int(input_list[i])
[More Advanced] Option 3:
    input_list = map(int, input_list)
[More Advanced] Option 4 (List composition):
    input_list = [int(x) for x in input_list]
Now input_list looks like this: [1, 2, 3, 4]
We need to convert our list of ints to a tuple of ints (as a list is not hashable, but a tuple is)
t = tuple(input_list)
print the result
print hash(t)
Other Optimizations (Not necessary for credit here):
If the first input line == '0' then bail, there isn't anything interesting to parse
Call strip() on the input to remove trailing and leading whitespace.
raw_input().strip()
These commands can obviously be combined


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