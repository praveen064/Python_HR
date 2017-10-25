#@Data types

##@Lists##   
=======
Notes: --->https://www.hackerrank.com/challenges/python-lists/tutorial
		https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split
=======

You can initialize a list as:
arr = list()
# or simply
arr = []
or with a few elements as:
arr = [1,2,3]
Elements can be accessed easily similar to most programming languages:
print arr[0]
# result is 1
print arr[0] + arr[1] + arr[2]
# result is 6
Lists in Python are very versatile. You can add almost anything in a Python list.
In Python, you can create a list of any objects: strings, integers, or even lists. You can even add multiple types in a single list!
Let's look at some of the methods you can use on list.
1.) append(x)
Adds a single element x to the end of a list.
arr.append(9)   
print arr  
# prints [1, 2, 3, 9]
2.) extend(L)
Merges another list L to the end.
arr.extend([10,11])
print arr
# prints [1, 2, 3, 9, 10, 11]
3.) insert(i,x) 
Inserts element x at position i.
arr.insert(3,7)
print arr
# prints [1, 2, 3, 7, 9, 10, 11]
4.) remove(x) 
Removes the first occurrence of element x.
arr.remove(10)  
arr  
# prints [1, 2, 3, 7, 9, 11]
5.) pop() 
Removes the last element of a list. If an argument is passed, that index item is popped out.
temp = arr.pop()
print temp 
# prints 11
6.) index(x) 
Returns the first index of a value in the list. Throws an error if it's not found.
temp = arr.index(3)
print temp
# prints 2
7.) count(x) 
Counts the number of occurrences of an element x.
temp = arr.count(1)
print temp
# prints 1
8.) sort() 
Sorts the list.
arr.sort()
print arr
# [1, 2, 3, 7, 9]
9.) reverse() 
Reverses the list.
arr.reverse()
print arr
# [9, 7, 3, 2, 1]

Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.


=====		
Note:
===== 
Using underscore ("_") as the variable name in the for appears to be common practice when you don't intend to use the variable in the loop. Underscore is a valid variable name, so you could use it in the loop, but it would make for unreadable code (what does underscore mean?) so using it designates that the variable has no meaning or is otherwise unnecessary.

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


#@Comprehensions:

Concept
You have already used lists in previous hacks. List comprehensions are an elegant way to build a list without having to use different for loops to append values one by one. These examples might help.
The simplest form of a list comprehension is: 

[ expression-involving-loop-variable for loop-variable in sequence ] 

This will step over every element in a sequence, successively setting the loop-variable equal to every element one at a time. It will then build up a list by evaluating the expression-involving-loop-variable for each one. This eliminates the need to use lambda forms and generally produces a much more readable code than using map() and a more compact code than using a for loop.
>> ListOfNumbers = [ x for x in range(10) ] # List of integers from 0 to 9
>> ListOfNumbers
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
List comprehensions can be nested where they take the following form: 

[ expression-involving-loop-variables for outer-loop-variable in outer-sequence for inner-loop-variable in inner-sequence ] 
This is equivalent to writing: 
results = []
for outer_loop_variable in outer_sequence:
    for inner_loop_variable in inner_sequence:
        results.append( expression_involving_loop_variables )

The final form of list comprehension involves creating a list and filtering it similar to using the filter() method. The filtering form of list comprehension takes the following form: 

[ expression-involving-loop-variable for loop-variable in sequence if boolean-expression-involving-loop-variable ] 

This form is similar to the simple form of list comprehension, but it evaluates boolean-expression-involving-loop-variable for every item. It also only keeps those members for which the boolean expression is True.
>> ListOfThreeMultiples = [x for x in range(10) if x % 3 == 0] # Multiples of 3 below 10
>> ListOfThreeMultiples
[0, 3, 6, 9]

#@Nested Lists:

Let's implement a nested list! A nested list is a list that contains another list (i.e.: a list of lists). For example:
nested_list = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
print len(nested_list)
# prints 3
print nested_list[1]
# prints ['red', 'black']
print nested_list[1][0]
# prints red
To go through every element in a list, use a nested for loop.


#@Finding the percentage:

A dictionary is a data type which stores values in pairs. For each element in the dictionary, there is a unique key that points to a value. A dictionary is mutable. It can be changed.
 
For example:
a_dict = {'one': 1} # Here 'one' is the key.  
Note: The key of a dictionary is immutable. We cannot use a list as a key because a list is mutable. But we can make a tuple of list and use as key.
a_dict['two'] = 2 # Adds key 'two' which points to 2
print a_dict['one']
# prints 1  
if 'three' in a_dict:
    # To check whether a certain string exist as a key in the dictionary  
    print a_dict['three']
else:  
    print "Three not there"
# prints Three not there
del a_dict['one']
# Deletes index 'one' and the value associated with it  
print a_dict
# prints {'two': 2}
Note: A dictionary is unordered. So, only use the keys to navigate through the dictionary.


