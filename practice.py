Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> it1 = iter([1, 2, 3])
>>> it2 = iter([4, 5, 6])
>>> itertools.chain(it1, it2)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    itertools.chain(it1, it2)
NameError: name 'itertools' is not defined
>>> [1, 2, 3, 4, 5, 6]
[1, 2, 3, 4, 5, 6]
>>> for x, y in itertools.izip(["a", "b", "c"], [1, 2, 3]):
	print(x, y)

	
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    for x, y in itertools.izip(["a", "b", "c"], [1, 2, 3]):
NameError: name 'itertools' is not defined
>>> print("x, y")
x, y
>>> a 1
SyntaxError: invalid syntax
>>> b 2
SyntaxError: invalid syntax
>>> c 3
SyntaxError: invalid syntax
>>> it = iter(range(5))
>>> x, it1 = peep(it)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x, it1 = peep(it)
NameError: name 'peep' is not defined
>>> print x, list(it1)
SyntaxError: invalid syntax
>>> 0 [0, 1, 2, 3, 4]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    0 [0, 1, 2, 3, 4]
TypeError: 'int' object is not subscriptable
>>> list(enumerate(["a", "b", "c"])
	 [(0, "a"), (1, "b"), (2, "c")]
	 for i, c in enumerate(["a", "b", "c"]):
	 
SyntaxError: invalid syntax
>>> print i, c
	 
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(i, c)?
>>> count_change(10, [1, 5])
	 
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    count_change(10, [1, 5])
NameError: name 'count_change' is not defined
>>> count_change(10, [1, 2])
	 
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    count_change(10, [1, 2])
NameError: name 'count_change' is not defined
>>> count_change(100, [1, 5, 10, 25, 50])
	 
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    count_change(100, [1, 5, 10, 25, 50])
NameError: name 'count_change' is not defined
>>> permute([1, 2, 3])
	 
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    permute([1, 2, 3])
NameError: name 'permute' is not defined
>>> 42
	 
42
>>> 4 + 2
	 
6
>>> 8 + 8
	 
16
>>> 5 / 2
	 
2.5
>>> 123/ 4
	 
30.75
>>> 2345,56/7
	 
(2345, 8.0)
>>> print("Hello , world!!!")
	 
Hello , world!!!
>>> x = 4
	 
>>> x * x
	 
16
>>> foo
	 
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    foo
NameError: name 'foo' is not defined
>>> foo = 45
	 
>>> foo
	 
45
>>> x = 4
	 
>>> x
	 
4
>>> x = 'hello'
	 
>>> x
	 
'hello'
>>> a, b= 1, 2
	 
>>> a
	 
1
>>> b
	 
2
>>> a + b
	 
3
>>> a, b = b, a
	 
>>> a
	 
2
>>> b
	 
1
>>> x = 4
	 
>>> y = x + 1
	 
>>> x = 2
	 
>>> print(x, y)
	 
2 5
>>> x, y = 2, 6
	 
>>> x, y = y, x + 2
	 
>>> print(x, y)
	 
6 4
>>> a, b = 2, 3
	 
>>> c, b = a, c + 1
	 
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    c, b = a, c + 1
NameError: name 'c' is not defined
>>> printa, b, c
	 
Traceback (most recent call last):
  File "<pyshell#55>", line 1, in <module>
    printa, b, c
NameError: name 'printa' is not defined
>>> 42
	 
42
>>> 4 + 2
	 
6
>>> 4.2
	 
4.2
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
>>> x = "hello"
	 
>>> y + 'world'
	 
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    y + 'world'
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(x, y)
	 
hello 4
>>> x = """This is a multi-line string
written in
three lines."""
	 
>>> print(x)
	 
This is a multi-line string
written in
three lines.
>>> y = '''multi-line strings can be written using three single quote characters as well. The string can contain 'single quotes' or " double quotes" in side it.'''
	 
>>> print(y)
	 
multi-line strings can be written using three single quote characters as well. The string can contain 'single quotes' or " double quotes" in side it.
>>> def square(x):
	 return x * x

	 
>>> square(5)
	 
25
>>> square(2) + square(3)
	 
13
>>> square(square(3))
	 
81
>>> def sum_of_squares(x, y):
	 return quare(x) + square(y)

	 
>>> sum_of_squares(2, 3)
	 
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    sum_of_squares(2, 3)
  File "<pyshell#91>", line 2, in sum_of_squares
    return quare(x) + square(y)
NameError: name 'quare' is not defined
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
	 print(x, y)

	 
>>> pi = 3.14
	 
>>> def area(r):
	 return pi * r * r

	 
>>> 
