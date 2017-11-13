#@Validating Email Addresses With a Filter:

Valid email addresses must follow these rules:

It must have the username@websitename.extension format type.
The username can only contain letters, digits, dashes and underscores.
The website name can only have letters and digits.
The maximum length of the extension is 3. 

Concept

A filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence where the function returned True. A Lambda function can be used with filters. 

Let's say you have to make a list of the squares of integers from 0 to 9 (both included).

>> l = list(range(10))
>> l = list(map(lambda x:x*x, l))
Now, you only require those elements that are greater than 10 but less than 80.

>> l = list(filter(lambda x: x > 10 and x < 80, l))

Input Format

The first line of input is the integer N, the number of email addresses. 
N lines follow, each containing a string.


Output Format

Output a list containing the valid email addresses in lexicographical order. If the list is empty, just output an empty list, [].

Sample Input

3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
Sample Output

['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

Sol-0:
We can solve this using the regex and filter tools.

import re
lst = list()
for i in range(int(input())):
    lst.append(input())
print (sorted(list(filter(lambda x: re.search(r'^[\w\d-]+@[A-Za-z0-9]+\.\w?\w?\w$',x),lst))))


lower text: 

def filter_mail(emails):

if __name__ == '__main__':
	n = int(input())
	emails = []
	for _ in range(n):
		emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)