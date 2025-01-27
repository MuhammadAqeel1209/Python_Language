"""Generators in Python
Generators in Python are special type of functions that allow you to create an iterable sequence
of values. A generator function returns a generator object, which can be used to generate the values one-by-one 
as you iterate over it. they allow you to generate the values on-the-fly, rather than having to create and store the entire sequence in memory"""


"""Working of generator
In Python, you can create a generator by using the yield statement in a function. The yield statement returns a value from the generator 
and suspends the execution of the function until the next value is requested."""
def Generators():
    for i in range(500):
        i = i + i + 1
        yield i

gen = Generators()
for i in gen:
    print(i)