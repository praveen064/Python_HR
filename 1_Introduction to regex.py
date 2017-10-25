#@Regex_module:
=====
Note: https://docs.python.org/3/howto/regex.html
http://www.regular-expressions.info/lookaround.html
=====

re

A regular expression (or RegEx) specifies a set of strings that matches it.

A regex is a sequence of characters that defines a search pattern, mainly for the use of string pattern matching.


The re.search() expression scans through a string looking for the first location where the regex pattern produces a match. 
It either returns a MatchObject instance or returns None if no position in the string matches the pattern.

Code

>>> import re
>>> print bool(re.search(r"ly","similarly"))
True

The re.match() expression only matches at the beginning of the string. 
It either returns a MatchObject instance or returns None if the string does not match the pattern. 
Code

>>> import re
>>> print bool(re.match(r"ly","similarly"))
False
>>> print bool(re.match(r"ly","ly should be in the beginning"))
True


We can use ^[+-]?\d*\.\d+$.
Explanation:
Let X be the floating point number we want to match. Then:
^ = the start of X.
[+-]? = optional, either + or -. 
\d* = zero or more digits. 
\. = . symbol. 
\d+ = one or more digits. 
$ = end of X.


Exception:can u explain this: '^[-+]?[0-9]*.[0-9]+$'
^ says start of the expression.
[-+]? says it can start with either - or +.
[0-9] says any number from 0-9 can be followed after it.
* says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, even 0 times.
'.' is placeholder for any character.(for the answer it should be '\.' instead of '.' ; '\' is escape character. Because of this you can literally mean a dot in expression).
again[0-9] as explained earlier.
'+' says that whichever thing it follows[in this case it is[0-9]], it can repeat arbitrarily times, but atleast one time.
$ follows whichever thing it should come in the end.


--> filter() returns every element in the second argument for which the function in the first argument evaluates as true. Using None as the first argument removes all items that are equivalent to false. The latter two test cases have consecutive delimiters, so using re.split() creates empty elements in the list. filter() returns the list without those empty elements.
There are plenty of other ways to do it, though. I like BigJin's method below since it doesn't even need filter(), just adding a + to the regex to match consecutive delimiters.

@#Group(), Groups() & Groupdict()

group()

A group() expression returns one or more subgroups of the match. 
Code

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.group(0)       # The entire match 
'username@hackerrank.com'
>>> m.group(1)       # The first parenthesized subgroup.
'username'
>>> m.group(2)       # The second parenthesized subgroup.
'hackerrank'
>>> m.group(3)       # The third parenthesized subgroup.
'com'
>>> m.group(1,2,3)   # Multiple arguments give us a tuple.
('username', 'hackerrank', 'com')
groups()

A groups() expression returns a tuple containing all the subgroups of the match. 
Code

>>> import re
>>> m = re.match(r'(\w+)@(\w+)\.(\w+)','username@hackerrank.com')
>>> m.groups()
('username', 'hackerrank', 'com')
groupdict()

A groupdict() expression returns a dictionary containing all the named subgroups of the match, keyed by the subgroup name. 
Code

>>> m = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
>>> m.groupdict()
{'website': 'hackerrank', 'user': 'myname', 'extension': 'com'}


##@Re.findall() & Re.finditer()##

re.findall()

The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings. 
Code

>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']

re.finditer()

The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string. 
Code

>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']


'''	
Explination:
' Can someone kindly explain to me the use/meaning of the '?<=' and '?=' in the above snippet (from the editorial) in detail. Also,in re does ['+xyz+'] always get replaced by the string in xyz or it happens only when we use the '?' thingys? What is meant by positive/negative lookahead/lookbehind? I did google and refer the python documentation but couldn't understand about the '?' thingys nor could I find any concise explanation of the lookahead/lookbehind stuff. HELP! :


(?=...)
Matches if ... matches next, but doesn’t consume any of the string. This is called a lookahead assertion. For example, Isaac (?=Asimov) will match 'Isaac ' only if it’s followed by 'Asimov'.
(?<=...)
Matches if the current position in the string is preceded by a match for ... that ends at the current position. This is called a positive lookbehind assertion. (?<=abc)def will find a match in abcdef, since the lookbehind will back up 3 characters and check if the contained pattern matches.

regarding ['+xyz+']:
it is just a way of building a string with concatenation (using '+'), and it has nothing to do with the question mark '?', for example:
list = 'abcdefg'
pattern = '['+list+']'
is equivalent to
pattern = '[' + 'abcdefg' + ']'
and is equivalent to
pattern = '[abcdefg]'
'?' in your example is a part of syntax for lookahead/lookbehind assertions (see below)
lookahead/lookbehind are collectively called lookaround and used as the boundary assertion mechanism:
positive lookahead means that you want your pattern to be followed by a specific character/expression, example:
vowels = 'aeiou'
match = re.findall(r'['+vowels+']{2,}(?=\d)', input)
that means: in your input you are looking for two or more vowels (your pattern: ['+vowels+']{2,}) that have to be followed by a digit (positive lookahead: (?=\d)):
  input        match
'eo3ppaao' -> ['eo']
it doesn't match 'aao' as it is not followed by a digit.
syntax for positive lookahead is demonstrated above: to the right of your pattern you insert the opening parenthesis followed by a question mark and an equals sign:
[pattern](?=
then you add a character/expression you want your pattern to be followed by and the closing parenthesis:
 [pattern](?=[expression])
negative lookahead means that you want your pattern to be followed by anything but certanly not by a specific character/expression, example:
vowels = 'aeiou'
match = re.findall(r'['+vowels+']{2,}(?!\d)', input)
that means: in your input you are looking for two or more vowels (your pattern: ['+vowels+']{2,}) that have to be followed by anything but certanly not by a digit (negative lookahead: (?!\d)):
  input        match
'eo3ppaao' -> ['aao']
it matches 'aao' as it is not followed by a digit.
note that it will not match 'aa' or 'ao' because {2,} is greedy.
syntax for negative lookahead is demonstrated above: to the right of your pattern you insert the opening parenthesis followed by a question mark and an exclamation point:
[pattern](?!
then you add a character/expression you want your pattern not to be followed by and the closing parenthesis:
[pattern](?![expression])
also note that using simple negation [^\d] instead of negative lookahead (?!\d) will not match anything if your pattern contains the last character of input as [^\d] means any character other than a digit but it still has to be a character. this is an important feature of lookaround's:
vowels = 'aeiou'
match_1 = re.findall(r'['+vowels+']{3}(?!\d)', input)
match_2 = re.findall(r'['+vowels+']{3}[^\d]', input)

  input       match_1
'eo3ppaao' -> ['aao']

  input       match_2
'eo3ppaao' -> []
everything above goes for positive lookbehind and negative lookbehind in the same way. the only difference is that you are looking at the character/expression that is in front of your pattern, not after your pattern.
so, instead of inserting lookaround to the right of your pattern you insert lookaround to the left of it.
syntax for lookbehind changes to:
(?<=[expression])[pattern]  #positive lookbehind
(?<![expression])[pattern]  #negative lookbehind
basically, it is the same as for lookahead, you just have to add '<' to the right of the question mark.
another important feature of lookaround's: they are excluded from the match.
for instance, in your example:
match = re.findall(r'(?<=['+consonants+'])(['+vowels+']{2,})(?=['+consonants+'])',raw_input(),flags = re.I)
if you find two or more vowels(your pattern) between consonants, match will return only vowels, lookaround's will be dropped, they are used only to assert boundaries of your pattern.
'''

#@start() & end()

These expressions return the indices of the start and end of the substring matched by the group.

Code

>>> import re
>>> m = re.search(r'\d+','1234')
>>> m.end()
4
>>> m.start()
0


@#Regex Substitution##
The re.sub() tool (sub stands for substitution) evaluates a pattern and, for each valid match, it calls a method (or lambda). 
The method is called for all matches and can be used to modify strings in different ways. 
The re.sub() method returns the modified string as an output.

Transformation of Strings

Code

import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
Output

1 4 9 16 25 36 49 64 81

Replacements in Strings

Code

import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
Output

<head>
<title>HTML</title>
</head>
<object type="application/x-flash" 
  data="your-file.swf" 
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
