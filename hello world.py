Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello World")
Hello World
>>> if 5 > 2:
	print("Five is greater than two!")

	
Five is greater than two!
>>> if 5 > 2:
	print("Five is greater than two!")

	
Five is greater than two!
>>> #This is a comment.
>>> print("Hello, World!")
Hello, World!
>>> """This is amultiline docstring."""
'This is amultiline docstring.'
>>> print("Hello, World!")
Hello, World!
>>> x = 5
>>> y = "John"
>>> print(x)
5
>>> print(y)
John
>>> x = 4 # x is of type int
>>> x = "Sally" # x is now of type str
>>> print(x)
Sally
>>> x = "awesome"
>>> print("Python is " + x)
Python is awesome
>>> x = "Python is "
>>> y = "awesome"
>>> z = x + y
>>> print(z)
Python is awesome
>>> x = 5
>>> y = 10
>>> print(x + y)
15
>>> x = 5
>>> y = "John"
>>> print(x + y)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(x + y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> carname = "volvo"
>>> carname = "ford"
>>> carname = "holden"
>>> x = 1 #int
>>> y = 2.8 #float
>>> z = 1j #complex
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'complex'>
>>> x = 1
>>> y = 356656222554887711
>>> z = -3255522
>>> print(type(x))
<class 'int'>
>>> print(type(y))
<class 'int'>
>>> print(type(z))
<class 'int'>
>>> x = 1.10
>>> y = 1.0
>>> z = -35.59
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 35e3
>>> y = 12E4
>>> z = -87.7e100
>>> print(type(x))
<class 'float'>
>>> print(type(y))
<class 'float'>
>>> print(type(z))
<class 'float'>
>>> x = 3+5j
>>> y = 5j
>>> z = -5j
>>> print(type(x))
<class 'complex'>
>>> print(type(y))
<class 'complex'>
>>> print(type(z))
<class 'complex'>
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> int()
0
>>> float()
0.0
>>> float()
0.0
>>> float()
0.0
>>> float()
0.0
>>> float()
0.0
>>> float()
0.0
>>> float()
0.0
>>> str()
''
>>> str()
''
>>> str()
''
>>> str()
''
>>> str()
''
>>> str()
''
>>> str()
''
>>> str()
''
>>> x = int(1)
>>> y = int(2.8)
>>> z = int("3")
>>> x = float(1)
>>> y = float(2.8)
>>> z = float("3")
>>> w = float("4.2")
>>> a = "Hello, World!"
>>> print(a[1])
e
>>> b = "Hello, World!"
>>> print(b[2:5])
llo
>>> a = "Hello, World!"
>>> print(len(a))
13
>>> a = "Hello, World!"
>>> print(a.lower())
hello, world!
>>> a = "Hello, World"
>> print(a.upper))
SyntaxError: invalid syntax
>>> print(a.upper())
HELLO, WORLD
>>> a = "Hello, World!"
>>> print(a.split(","))
['Hello', ' World!']
>>> print("Enter your name:")
Enter your name:
>>> x = input()
print("Hello, " + x)
>>> x = "Hello World"
>>> print(len(x))
11
>>> 234 * 0
0
>>> 3456 * 123
425088
>>> 345 / 9
38.333333333333336
>>> 3452.67 / 1234
2.7979497568881686
>>> def read_words(filename):
        return open(filename).read().split()
def main(filename):
        frequency = word_frequency(read_words(filename))
        for word, count in frequency.items():
                print word, count
                if _name_ == "_main_":
                        import sys
                        main(sys.argv[1]



# print() and newline character.

('a' instead of 'w')
f = open("log.txt", "a")
print('print a line')







