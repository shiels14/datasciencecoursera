Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 7.0 / 2.0
3.5
>>> 7.0 / 2
3.5
>>> 7 / 2.0
3.5
>>> 5 / 9.0
0.5555555555555556
>>> 190.9 / 4
47.725
>>> # this is an integer /
>>> 123.56 / 0
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    123.56 / 0
ZeroDivisionError: float division by zero
>>> 2345.66 / 8.0
293.2075
>>> 3456 / 67.190
51.436225628813816
>>> x = "hello"
>>> y = 'world'
>>> print(x,y)
hello world
>>> x = (""" I am the best in the world because this is a string")
written in
three lines."""
	 printx
	 
SyntaxError: invalid syntax
>>> print(x)
	 
hello
>>> print(y)
	 
world
>>> print(z)
	 
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    print(z)
NameError: name 'z' is not defined
>>> def square(x):
	 return x * x
	 square(5)
	 square(5)

	 
>>> print(square5)
	 
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    print(square5)
NameError: name 'square5' is not defined
>>> print("square 5")
	 
square 5
>>> square(2) + square(3)
	 
13
>>> square(square(3))
	 
81
>>> def sum_of_square(x, y):
	 return square(x) + square(y)

	 
>>> sum_of_square(2, 3)
	 
13
>>> f = square
	 
>>> f(4)
	 
16
>>> def fxy(f, x, y):
	 return f (x) + f(y)

	 
>>> fxy(square, 2, 3)
	 
13
>>> x = 0
	 
>>> y = 0
	 
>>> x = 9
	 
>>> t = 1
	 
>>> ss = shit
	 
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    ss = shit
NameError: name 'shit' is not defined
>>> ss = 8
	 
>>> stephen = 5
	 
>>> pie = 3
	 
>>> cool = 69
	 
>>> x = 0
	 
>>> y = 0
	 
>>> def incr(x):
	 y = x + 1
	 return y
	 incr(5)
	 print(x, y)

	 
>>> pi = 3.14
	 
>>> def area(r):
	 return pi * r * r

	 
>>> numcalls = 0
	 
>>> def square(x):
	 global numcalls
	 numcalls = numcalls + 1
	 return x * x

	 
>>> print square(5)
	 
SyntaxError: invalid syntax
>>> print("square 5")
	 
square 5
>>> print("square 7")
	 
square 7
>>> x = 1
	 
>>> def f():
	 return x
	 print(x)
	 print f()
	 
SyntaxError: invalid syntax
>>> print("f"()
	  print ("Hello World")
	  
SyntaxError: invalid syntax
>>> x = 1
	  
>>> def f():
	  return x
	  print(x)
	  print(f))
	 
SyntaxError: invalid syntax
>>> x = 1
	 
>>> def f()
	 
SyntaxError: invalid syntax
>>> y = x
	 
>>> x = 2
	 
>>> return x + y
	 
SyntaxError: 'return' outside function
>>> print x
	 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print f()
	 
SyntaxError: invalid syntax
>>> print x
	 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> x = 2
	 
>>> def f(a):
	 x = a * a
	 return x
	 y = f(3)
	 print x, y
	 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, y)?
>>> def difference(x, y):
	 return x - y

	 
>>> difference(5, 2)
	 
3
>>> difference(x=5, y=2)
	 
3
>>> difference(53, y=2)
	 
51
>>> difference(5, y=2)
	 
3
>>> difference(y=2, x=5)
	 
3
>>> def increment(x, amount=1):
	 return x + amount

	 
>>> increment(10)
	 
11
>>> increment(10, 5)
	 
15
>>> increment(10, amount=2)
	 
12
>>> cube = lambda x: x ** 3
	 
>>> fxy(cube, 2 3)
	 
SyntaxError: invalid syntax
>>> fxy(cube, 2, 3)
	 
35
>>> fxy(lambda x: x ** 3, 2, 3)
	 
35
>>> min(2, 3)
	 
2
>>> max(3, 4)
	 
4
>>> len("helloworld")
	 
10
>>> int("50")
	 
50
>>> str(123)
	 
'123'
>>> count_digits(5)
	 
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    count_digits(5)
NameError: name 'count_digits' is not defined
>>> count_digits(12345)
	 
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    count_digits(12345)
NameError: name 'count_digits' is not defined
>>> x = "hello"
	 
>>> print x.upper()
	 
SyntaxError: invalid syntax
>>> print("x.upper")
	 
x.upper
>>> istrcmp('python', 'python')
	 
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    istrcmp('python', 'python')
NameError: name 'istrcmp' is not defined
>>> istrcmp("Python", "Python")
	 
Traceback (most recent call last):
  File "<pyshell#133>", line 1, in <module>
    istrcmp("Python", "Python")
NameError: name 'istrcmp' is not defined
>>> istrcmp("LaTex", 'Latex")
	    
SyntaxError: EOL while scanning string literal
>>> istrcmp('a', 'b')
	    
Traceback (most recent call last):
  File "<pyshell#135>", line 1, in <module>
    istrcmp('a', 'b')
NameError: name 'istrcmp' is not defined
>>> 2 < 3
	    
True
>>> 13 > 5
	    
True
>>> 4 < 4
	    
False
>>> 1567 < 9
	    
False
>>> 123 <= 4
	    
False
>>> x = 543
	    
>>> 2 > x . 13
	    
SyntaxError: invalid syntax
>>> 3 < x < 12
	    
False
>>> 3 < 1
	    
False
>>> 45 < 3
	    
False
>>> # < less than
	    
>>> # > greater than
	    
>>> x = 5
	    
>>> 2 < x < 10
	    
True
>>> 2 < 3 < 4 < 5 < 6
	    
True
>>> "python" > "perl"
	    
True
>>> "python" > "java"
	    
True
>>> True and True
	    
True
>>> True and False
	    
False
>>> 2 < 3 and 5 < 4
	    
False
>>> 2 < 3 or 5 < 4
	    
True
>>> print 2 < 3 and 3 > 4
	    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(2 < 3 and 3 > 4)?
>>> print("2 < 3 and 3 > 4")
	    
2 < 3 and 3 > 4
>>> print ("2 < 3 or 3 > 1")
	    
2 < 3 or 3 > 1
>>> print("2 < 3 or not 3 > 1")
	    
2 < 3 or not 3 > 1
>>> print ("2 < 3 and not 3 > 1")
	    
2 < 3 and not 3 > 1
>>> x = 4
	    
>>> y = 5
	    
>>> p = x < y or x < z
	    
>>> print(p)
	    
True
>>> True, False = False, True
	    
SyntaxError: can't assign to keyword
>>> print True, False
	    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(True, False)?
>>> print 2 < 3
	    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(2 < 3)?
>>> x = 42
	    
>>> if x % 2 == 0: print("even")

	    
even
>>> if x % 2 == 0:
	    print("even")

	    
even
>>> x = 3
	    
>>> if x % 2 == 0:
	    print("even")
	    else:
	    
SyntaxError: invalid syntax
>>> print("odd")
	    
odd
>>> x = 42
	    
>>> if x < 10:
	    print("one digit number")
	    elif x < 100:
	    
SyntaxError: invalid syntax
>>> print("two digit number")
	    
two digit number
>>> else:
	    
SyntaxError: invalid syntax
>>> print("big number")
	    
big number
>>> x = 2
	    
>>> if x == 2:
	    print(x)

	    
2
>>> else:
	    
SyntaxError: invalid syntax
>>> x +
	    
SyntaxError: invalid syntax
>>> x = ["hello", "world"]
	    
>>> x = [1, 2, "hello", "world", ["another", "list"]]
	    
>>> x = [1, 2, 3]
	    
>>> len(x)
	    
3
>>> x = [1, 2, 3]
	    
>>> x[1]
	    
2
>>> x[1] = 4
	    
>>> x[1]
	    
4
>>> import time
	    
>>> time.asctime()
	    
'Mon Jan 14 16:29:56 2019'
>>> import sys
	    
>>> time.asctime()
	    
'Mon Jan 14 16:31:17 2019'
>>> import sys
	    
>>> print sys.argv[1]
	    
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sys.argv[1])?
>>> print("sys.argv[1]")
	    
sys.argv[1]
>>> $ python echo.py hello
	    
SyntaxError: invalid syntax
>>> hello
	    
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> [1, 2, 3, 4]
	    
[1, 2, 3, 4]
>>> ["hello", "world"]
	    
['hello', 'world']
>>> [0, 1.5, "hello"]
	    
[0, 1.5, 'hello']
>>> [0, 1.5, "hello"]
	    
[0, 1.5, 'hello']
>>> a = [1, 2]
	    
>>> b = [1.5, 2, a]
	    
>>> b
	    
[1.5, 2, [1, 2]]
>>> range(4)
	    
range(0, 4)
>>> [0, 1, 2, 3]
	    
[0, 1, 2, 3]
>>> range(3, 6)
	    
range(3, 6)
>>> [3, 4, 5]
	    
[3, 4, 5]
>>> range(2, 10, 3)
	    
range(2, 10, 3)
>>> [2, 5, 8]
	    
[2, 5, 8]
>>> a = [1, 2, 3, 4]
	    
>>> len(a)
	    
4
>>> a = [1, 2, 3]
	    
>>> b = [4, 5]
	    
>>> a + b
	    
[1, 2, 3, 4, 5]
>>> b * 3
	    
[4, 5, 4, 5, 4, 5]
>>> x = [1, 2]
	    
>>> x[0]
	    
1
>>> x[1]
	    
2
>>> x [2]
	    
Traceback (most recent call last):
  File "<pyshell#232>", line 1, in <module>
    x [2]
IndexError: list index out of range
>>> x = [1, 2, 3, 4]
	    
>>> x [6]
	    
Traceback (most recent call last):
  File "<pyshell#234>", line 1, in <module>
    x [6]
IndexError: list index out of range
>>> x = [1, 2, 3, 4]
	    
>>> x[-2]
	    
3
>>> x = [1, 2, 3, 4]
	    
>>> x[0:2]
	    
[1, 2]
>>> x[1:4]
	    
[2, 3, 4]
>>> x[0:-1]
	    
[1, 2, 3]
>>> a[2:]
	    
[3]
>>> a[:]
	    
[1, 2, 3]
>>> x = range(10)
	    
>>> x
	    
range(0, 10)
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	    
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> x[0:6:2]
	    
range(0, 6, 2)
>>> x[::-1]
	    
range(9, -1, -1)
>>> [9,8,7,6,5,4,3,2,1,0]
	    
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
>>> x = [1, 2, 3, 4]
	    
>>> x[1] = 5
	    
>>> x
	    
[1, 5, 3, 4]
>>> [1, 2, 3, 4]
	    
[1, 2, 3, 4]
>>> x = [1, 2, 3, 4]
	    
>>> 2 in x
	    
True
>>> 10 in x
	    
False
>>> a = [1, 2]
	    
>>> a.appenend(3)
	    
Traceback (most recent call last):
  File "<pyshell#257>", line 1, in <module>
    a.appenend(3)
AttributeError: 'list' object has no attribute 'appenend'
>>> a.append(3)
	    
>>> a
	    
[1, 2, 3]
>>> x = [0, 1, [2]]
	    
>>> x[2][0] = 3
	    
>>> print("x")
	    
x
>>> x[2].append(4)
	    
>>> print("x")
	    
x
>>> x[2] = 2
	    
>>> print("x")
	    
x
>>> for x in [1, 2, 3, 4]:
	    print("x")

	    
x
x
x
x
>>> for i in range(10):
	    print("i, i*i, i*i*i")

	    
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
i, i*i, i*i*i
>>> zip(["a", "b", "c"], [1, 2, 3])
	    
<zip object at 0x1052bf388>
>>> 
