Task

Now, let's use our knowledge of sets and help Mickey.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.

Formula used:
	Avg = Sum of distint Heights/Total no of distint heights

Input Format

The first line contains the integer, , the total number of plants.
The second line contains the  space separated heights of the plants.

Constraints


Output Format

Output the average height value on a single line.

Sample Input

10
161 182 161 154 176 170 167 171 170 174
Sample Output

169.375

Sol-1:

def average(array):
    # your code goes here
    return sum(set(array))/len(set(array))
	
Sol-0:

The approach to solve this challenge follows: 

Step 1: Store the set of inputs in the variable distinctHeights.

Step 2: Store the sum of distinctHeights in the variable sumOfDistinctHeights.

Step 3: Store the total number of distinctHeights in the variable totalDistinctHeights.

Step 4: Take the average by dividing the sumOfDistinctHeights with totalDistinctHeights.

Step 5: Print the output.

from __future__ import division
n = int(input())
heights = [int(x) for x in input().split()]

#Step 1 - Make Set
distinctHeights = set(heights)

#Step 2 - Summation of Set
sumOfDistinctHeights = sum(distinctHeights)

#Step 3 - Length of Set
totalDistinctHeights = len(distinctHeights)

#Step 4 - Take Average
average = sumOfDistinctHeights/totalDistinctHeights

#Step 5 - Print Output
print (average)