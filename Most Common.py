#@Most Common:
You are given a string S which contains only lowercase English characters. 
Your task is to find the top three most common characters in the string S.

Input Format

A single line of input containing the string S.

Output Format

Print the three most common characters along with their occurrence count each on a separate line. 
Sort output in descending order of occurrence count. 
If the occurrence count is the same, sort the characters in ascending order.

Sample Input 0
aabbbccde

Sample Output 0
b 3
a 2
c 2

Explanation 0

Here, b occurs 3 times. It is printed first.
Both a and c occur 2 times. So, a is printed in the second line and c in the third line because a comes before c.

Note: The string S has at least 3 distinct characters.

Sol-0:
This can be solved by using Python counters or counting sort. 

Approach:

STEP 1: Create a list, letters, of size 26. Initialize each element to .

STEP 2: Traverse through the input string S. If a character in the string is 'a', then increment letter[0] by 1 . If 'b' is found, then increment letter[1] by 1 and so on.

STEP 3: Now run a loop three times. Inside the loop, store the maximum value of letters in the variable max_letter.

STEP 4:. In the scope of the previous loop, run another loop and find the index of the first occurrence of max_letter. Now, print the appropriate letter associated with that index and the max_letter.

S = raw_input()
letters = [0]*26

for letter in S:
    letters[ord(letter)-ord('a')] += 1

for _ in range(3):
    
    max_letter = max(letters)
    
    for index in range(26):
        if max_letter == letters[index]:
            print chr(ord('a')+index), max_letter
            letters[index] = -1
            break

			
Counter Solution 1:
from collections import Counter
from operator import itemgetter

for item in (sorted(sorted(Counter(raw_input()).items()), key = itemgetter(1), reverse = True)[:3]):
    print item[0], item[1]

	
Counter Solution 2:
from collections import Counter

for letter, counts in sorted(Counter(raw_input()).most_common(),key = lambda x:(-x[1],x[0]))[:3]:
    print letter, counts

Sol-1:
The OrderedCounter is explained here: https://codefisher.org/catch/blog/2015/06/16/how-create-ordered-counter-class-python/

from collections import Counter, OrderedDict

class OrderedCounter(Counter, OrderedDict):
    pass
[print(*c) for c in OrderedCounter(sorted(input())).most_common(3)]
