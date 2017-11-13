#@input()

x = 2
print eval ('x+1')
Output of this code = 3

So , eval('expression') is used to evaluate an expression . It is used to find the value of the expression , given the values of all the variables involved in that expression.
input() and eval() perform the same task of evaluating an expression.
input() is equivalent to eval(raw_input()) . Let us see how :

For the given question the code using input() is as follows:
x,k = map ( int , raw_input().split())
print input() == k

And the code using eval( raw_input() ) is as follows:
x,k = map ( int , raw_input().split())
print eval(raw_input()) == k

The code using eval() is as follows :
x,k = map ( int , raw_input().split())
s= raw_input()
print eval(s) == k