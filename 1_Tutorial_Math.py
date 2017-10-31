#@Power - Mod Power::
So far, we have only heard of Python's powers. Now, we will witness them!

Powers or exponents in Python can be calculated using the built-in power function. Call the power function a^b as shown below:

>>> pow(a,b) 
or

>>> a**b
It's also possible to calculate a^b mod m.

>>> pow(a,b,m)  
This is very helpful in computations where you have to print the resultant % mod.

Note: Here, a and b can be floats or negatives, but, if a third argument is present, b cannot be negative.

Note: Python has a math module that has its own pow(). It takes two arguments and returns a float. Frankly speaking, we will never use math.pow().
