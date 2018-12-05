Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> {
	"May": 3,
	"November": 2,
	"December": 1,
	}
{'May': 3, 'November': 2, 'December': 1}
>>> sandwiches = ["ham", "cheese", "roast beef", "ham", "cheese", "roast beef", "ham"]
>>> Counter({"ham": 3, "roast beef": 2, "cheese": 2})
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    Counter({"ham": 3, "roast beef": 2, "cheese": 2})
NameError: name 'Counter' is not defined
>>> print("There are{} ham sandwiches".format(c["ham"]))
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    print("There are{} ham sandwiches".format(c["ham"]))
NameError: name 'c' is not defined
>>> output_file("plot.html")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    output_file("plot.html")
NameError: name 'output_file' is not defined
>>> x = [10, 20, 30]
>>> y = [4, 5, 6]
>>> p = figure()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    p = figure()
NameError: name 'figure' is not defined
>>> p.vbar(x=x, top=y, width=0.5)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    p.vbar(x=x, top=y, width=0.5)
NameError: name 'p' is not defined
>>> show(p)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    show(p)
NameError: name 'show' is not defined
>>> out_file("plot.html")
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    out_file("plot.html")
NameError: name 'out_file' is not defined
>>> x_categories = ['a", "b", "c", "d", "e"]
		    
SyntaxError: EOL while scanning string literal
>>> x = ["a", "d", "e"]
		    
>>> y = [4, 5, 6]
		    
>>> p = figure(x_range_categories)
		    
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    p = figure(x_range_categories)
NameError: name 'figure' is not defined
>>> p.vbar(x=x, top=y, width=0.5)
		    
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    p.vbar(x=x, top=y, width=0.5)
NameError: name 'p' is not defined
>>> name = input ("what is your name: ")
		    
what is your name: Stephen
>>> age = int(input("How old are you: " )
year = str((2014 - age)+100)
	      
SyntaxError: invalid syntax
>>> print(name + " will be 100 years old in the year " + year)
	      
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(name + " will be 100 years old in the year " + year)
NameError: name 'year' is not defined
>>> ("Hello World")
	      
'Hello World'
>>> print("Hello World")
	      
Hello World
>>> # This is a comment
	      
>>> print("Hello, World")
	      
Hello, World
>>> C:\Users\Your Name>python myfile.py
	      
SyntaxError: unexpected character after line continuation character
>>> if 5 > 2:
	      print('Five is greater than two!" )
		    
SyntaxError: EOL while scanning string literal
>>> " " "This is a multiline docstring." " "
		    
' This is a multiline docstring. '
>>> print("Hello, World")
		    
Hello, World
>>> x = 5
		    
>>> y = "Stephen Shiels"
		    
>>> print9x)
	      
SyntaxError: invalid syntax
>>> print(x)
	      
5
>>> print(y)
	      
Stephen Shiels
>>> x = 4 # x is of type int
	      
>>> x = "Stephen" # x is now of type str
	      
>>> x = "awsome"
	      
>>> print("Python is " + x)
	      
Python is awsome
>>> x = "Python is "
	      
>>> y = "awsome"
	      
>>> z = x + y
	      
>>> print(z)
	      
Python is awsome
>>> x = 5
	      
>>> y = 10
	      
>>> print(x + y)
	      
15
>>> x = 5
	      
>>> y = "John"
	      
>>> print(x + y)
	      
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    print(x + y)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> x = 5
	      
>>> y = 10
	      
>>> print("carname + volvo")
	      
carname + volvo
>>> carname = volvo
	      
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    carname = volvo
NameError: name 'volvo' is not defined
>>> print("Carname = Volvo")
	      
Carname = Volvo
>>> x = 1 # int
	      
>>> y = 2.8 # float
	      
>>> z = 1j # complex
	      
>>> print(type(x))
	      
<class 'int'>
>>> print(type(y))
	      
<class 'float'>
>>> print(type(z))
	      
<class 'complex'>
>>> x = 1
	      
>>> y = 35656225544887711
	      
>>> z = 3255522
	      
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
>>> float()
	      
0.0
>>> str()
	      
''
>>> x = int(1)
	      
>>> y = int(2.8)
	      
>>> z = int("3")
	      
>>> x = float(1)
	      
>>> float(2.8)
	      
2.8
>>> y = float(2.8)
	      
>>> z = float("3")
	      
>>> w = float("4.2")
	      
>>> print(x)
	      
1.0
>>> print(y)
	      
2.8
>>> print(z)
	      
3.0
>>> print(w)
	      
4.2
>>> a = "Hello, World!"
	      
>>> print(a[1])
	      
e
>>> b = "Hello, World!"
	      
>>> print(b[2:5])
	      
llo
>>> a = " Hello, World!"
	      
>>> print(len(a))
	      
14
>>> a = "Hello, World!"
	      
>>> print(a.upper())
	      
HELLO, WORLD!
>>> a = "Hello, World!"
	      
>>> print(a.split(","))
	      
['Hello', ' World!']
>>> print("Stephen Shiels:")
	      
Stephen Shiels:
>>> x = input()
	      

>>> print("Hello, " + x)
	      
Hello, 
>>> x = "Hello World"
	      
>>> print("Hello World")
	      
Hello World
>>> x = "Hello World"
	      
>>> print(len(x))
	      
11
>>> +
	      
SyntaxError: invalid syntax
>>> x+y
	      
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    x+y
TypeError: can only concatenate str (not "float") to str
>>> -
	      
SyntaxError: invalid syntax
>>> x=5
	      
>>> x+3
	      
8
>>> x-=3
	      
>>> x*=3
	      
>>> x/=3
	      
>>> x%=3
	      
>>> x//=3
	      
>>> x**=3
	      
>>> x&=3
	      
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    x&=3
TypeError: unsupported operand type(s) for &=: 'float' and 'int'
>>> x|=3
	      
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    x|=3
TypeError: unsupported operand type(s) for |=: 'float' and 'int'
>>> x=x&3
	      
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    x=x&3
TypeError: unsupported operand type(s) for &: 'float' and 'int'
>>> x^=3
	      
Traceback (most recent call last):
  File "<pyshell#129>", line 1, in <module>
    x^=3
TypeError: unsupported operand type(s) for ^=: 'float' and 'int'
>>> x>>=3
	      
Traceback (most recent call last):
  File "<pyshell#130>", line 1, in <module>
    x>>=3
TypeError: unsupported operand type(s) for >>=: 'float' and 'int'
>>> x<<=3
	      
Traceback (most recent call last):
  File "<pyshell#131>", line 1, in <module>
    x<<=3
TypeError: unsupported operand type(s) for <<=: 'float' and 'int'
>>> x = 5
	      
>>> print(x > 3 and x < 10)
	      
True
>>> print("10+5")
	      
10+5
>>> print("10*5")
	      
10*5
>>> thislist = ["apple". "banana". "cherry"]
	      
SyntaxError: invalid syntax
>>> print(thislist)
	      
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    print(thislist)
NameError: name 'thislist' is not defined
>>> thislist = ["apple", "banana", "cherry"]
	      
>>> print(thislist)
	      
['apple', 'banana', 'cherry']
>>> thislist = ["apple", "banana", "cherry"]
	      
>>> thislist[1] = "blackcurrent"
	      
>>> print(thislist)
	      
['apple', 'blackcurrent', 'cherry']
>>> 
