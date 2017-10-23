##@Print Function##
=======
Notes:
=======
Example 2:
for i in xrange(10):
    print i,
Prints each element separated by space on a single line. Removing the comma at the end will print each element on a new line.
Let's import the advanced print_function from the __future__ module.
Its method signature is below:
print(*values, sep=' ', end='\n', file=sys.stdout)
print(value1, value2, value3, sep=' ', end='\n', file=sys.stdout)
Here, values is an array and *values means array is unpacked, you can add values separated by a comma too. The arguments sep, end, and file are optional, but they can prove helpful in formatting output without taking help from a string module.
The argument definitions are below: 
sep defines the delimiter between the values. 
end defines what to print after the values. 
file defines the output stream.
in Python 2 print_function is much faster than the default print

=======
Notes: https://www.hackerrank.com/challenges/python-print/forum
=======
In this example given by @SemperPeritus, he's providing a function log_in that takes name, password, captcha as arguments.
In general, you pass in arguments like so:
function(arg1,arg2,arg3)
But, if you put them in a list such as:
function([arg1,arg2,arg3])
then it's like you're only passing in 1 argument (the list) and you'll get an error saying function was expecting 3 arguments and only got 1.
On the other hand if you were to include * it would "unpack" the list (imagine the list is a suitcase and the elements are pieces of clothing you want to put on the bed to look at individually. you can't do that without unpacking the suitcase, right?) so that it would still work:
function(*[arg1,arg2,arg3])
becomes
function(arg1,arg2,arg3)
So *user changes from a list:
user = [name, password, captcha]
to arguments:
*user = name, password, captcha
So now log_in will work without errors because it was passed 3 arguments instead of 1!


Q)Read an integer N.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the values in between.

Input Format 
The first line contains an integer .

Output Format 
Output the answer as explained in the task.

Sample Input
3
Sample Output
123

Sol:
from __future__ import print_function
n = int(input())

#for i in range(1, n+1):print(i, end="")
#print(*range(1, n+1), sep='')
[print(i, end='') for i in range(1,n+1)]
