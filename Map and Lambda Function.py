#@Map and Lambda Function:

Concept

The map() function applies a function to every member of an iterable and returns the result. It takes two parameters: first, the function that is to be applied and secondly, the iterables. 
Let's say you are given a list of names, and you have to print a list that contains the length of each name.

>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function that has only one line in its body. It proves very handy in functional and GUI programming.

>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
Note:

Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside lists and dictionaries.

Input Format

One line of input: an integer N.

Output Format

A list on a single line containing the cubes of the first N fibonacci numbers.

Sample Input

5
Sample Output

[0, 1, 1, 8, 27]
Explanation

The first 5 fibonacci numbers are [0,1,1,2,3], and their cubes are [0,1,1,8,27].

Sol-0:
Use map and lambda x : x*x*x tools to compute the cube of fibonacci numbers.

# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(raw_input())
A = [0,1]
for i in range(2,N): A.append(A[i-1]+A[i-2])        
print map(lambda a: a*a*a,A)[:N]


Sol-1:

cube = lambda x: pow(x,3)# complete the lambda function 
def fibonacci(n):
     # return a list of fibonacci numbers
     lis = [0,1]
     for i in range(2,n):
         lis.append(lis[i-2] + lis[i-1])
     return(lis[0:n])