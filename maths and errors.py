Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 42
42
>>> 4 + 2
6
>>> print("Hello World")
Hello World
>>> 1 + 2
3
>>> x = 4
>>> x * x
16
>>> foo
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    foo
NameError: name 'foo' is not defined
>>> foo = 4
>>> foo
4
>>> x = 4
>>> x
4
>>> x = 'hello'
>>> x
'hello'
>>> 'hello'
'hello'
>>> a, b = 1, 2
>>> a
1
>>> b
2
>>> a + b
3
>>> a, b = 1, 2
>>> a, b = b, a
>>> a
2
>>> b
1
>>> x = 4
>>> y = x + 1
>>> x = 2
>>> print x, y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, y)?
>>> print(x , y)
2 5
>>> x, y = 2, 6
>>> x, y = y x + 2
SyntaxError: invalid syntax
>>> print x, y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, y)?
>>> print(x, y)
2 6
>>> a, b = 2, 6
>>> x, y = y, x + 2
>>> print(x, y)
6 4
>>> a, b = 2, 3
>>> c, b = a, c + 1
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    c, b = a, c + 1
NameError: name 'c' is not defined
>>> print a, b, c
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a, b, c)?
>>> 42
42
>>> 4 + 2
6
>>> 4.2
4.2
>>> 4.2 + 2.3
6.5
>>> 7 + 2
9
>>> 7 - 2
5
>>> 7 * 2
14
>>> 7 / 2
3.5
>>> 7 ** 2
49
>>> 7 % 2
1
>>> 7.0 / 2.0
3.5
>>> 7.0 / 2
3.5
>>> 7 / 2.0
3.5
>>> 7 + 2 + 5 - 3
11
>>> 2 * 3 + 4
10
>>> 2 + 3 * 4
14
>>> (2 + 3) * 4
20
>>> x - "hello"
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    x - "hello"
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> x - ("hello")
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    x - ("hello")
TypeError: unsupported operand type(s) for -: 'int' and 'str'
>>> y = 'world'
>>> print x, y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, y)?
>>> hello world
SyntaxError: invalid syntax
>>> def square(x):
	return x * x

>>> square(5)
25
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
	return f(x) + f(y)

>>> fxy(square, 2, 3)
13
>>> x = 0
>>> y = 0
>>> def incr(x):
	y = x + 1
	return y
incr(5)
SyntaxError: invalid syntax
>>> print(x, y)
0 0
>>> pi = 3.14
>>> def area(r):
	return pi * r * r

>>> numcalls = 0
>>> def square(x):
	global numcalls:
		
SyntaxError: invalid syntax
>>> numcaalls = numcalls + 1
>>> return x * x
SyntaxError: 'return' outside function
>>> print square(5)
SyntaxError: invalid syntax
>>> print square(2*5)
SyntaxError: invalid syntax
>>> x = 1
>>> def f():
	return x
print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print f()
SyntaxError: invalid syntax
>>> x = 1
>>> def f():
	return x
print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print f()
SyntaxError: invalid syntax
>>> x = 1
>>> def f():
	return x
print(x)
SyntaxError: invalid syntax
>>> print f()
SyntaxError: invalid syntax
>>> x = 1
>>> def f():
	x = 2
	return x
print f()
SyntaxError: invalid syntax
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> x = 2
>>> def f(a):
	x - a * a
	return x
y = f(3)
SyntaxError: invalid syntax
>>> print x, y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x, y)?
>>> def difference(5, 2)
SyntaxError: invalid syntax
>>> def difference(x, y):
	return x - y

>>> difference(5, 2)
3
>>> difference(x=5, y=2)
3
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
>>> fxy(cube, 2, 3)
35
>>> fxy(lambda x: x ** 3, 2, 3)
35
>>> min(2, 3)
2
>>> max(3, 4)
4
>>> len('helloworld")
	
SyntaxError: EOL while scanning string literal
>>> len("helloworld")
	
10
>>> int('50")
	
SyntaxError: EOL while scanning string literal
>>> int("50")
	
50
>>> str(123)
	
'123'
>>> count_digits(5)
	
Traceback (most recent call last):
  File "<pyshell#144>", line 1, in <module>
    count_digits(5)
NameError: name 'count_digits' is not defined
>>> count_digits(12345)
	
Traceback (most recent call last):
  File "<pyshell#145>", line 1, in <module>
    count_digits(12345)
NameError: name 'count_digits' is not defined
>>> x = "hello"
	
>>> print x.upper()
	
SyntaxError: invalid syntax
>>> f = x. upper
	
>>> print f()
	
SyntaxError: invalid syntax
>>> istrcmp('python', 'python')
	
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    istrcmp('python', 'python')
NameError: name 'istrcmp' is not defined
>>> istrcmp('LaTex', 'Latex')
	
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    istrcmp('LaTex', 'Latex')
NameError: name 'istrcmp' is not defined
>>> istrcmp('a', 'b')
	
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    istrcmp('a', 'b')
NameError: name 'istrcmp' is not defined
>>> 2 < 3
	
True
>>> 2 > 3
	
False
>>> x = 5
	
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
>>> print 2 < 3 and 3 > 1
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(2 < 3 and 3 > 1)?
>>> (print) 2 < 3 and 3 > 1
	
SyntaxError: invalid syntax
>>> print("2 < 3 and 3 > 1")
	
2 < 3 and 3 > 1
>>> print("2 < 3 or 3 > 1")
	
2 < 3 or 3 > 1
>>> print("2 < 3 or not 3 > 1")
	
2 < 3 or not 3 > 1
>>> print("2 < 3 and not 3 > 1")
	
2 < 3 and not 3 > 1
>>> x = 4
	
>>> y = 5
	
>>> p = x < y or x < z
	
>>> print(p)
	
True
>>> print p
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(p)?
>>> y
	
5
>>> x = 42
	
>>> if x % 2 == 0: print 'even'
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('even')?
>>> if x % 2 == 0: print("even")
	even
	
SyntaxError: unexpected indent
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
>>> 
