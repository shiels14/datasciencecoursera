Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> the_world_is_flat = True
>>> if the_world_is_flat:
	print("Be careful not to fall off!")

	
Be careful not to fall off!
>>> a, b = 0, 1
>>> while a < 1000:
	print(a, end=',')
	a, b = b, a+b

	
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 5
1.6
>>> 17 / 3
5.666666666666667
>>> 17 // 3
5
>>> 17 % 3
2
>>> 5 * 3 + 2
17
>>> 5 ** 2
25
>>> 2 ** 7
128
>>> width= 20
>>> height = 5 * 9
>>> width * height
900
>>> n
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    n
NameError: name 'n' is not defined
>>> n # try to access an undefined variable
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    n # try to access an undefined variable
NameError: name 'n' is not defined
>>> 4 * 3.75 - 1
14.0
>>> tax = 12.5 / 100
>>> price = 100.50
>>> price * tax
12.5625
>>> price + _
113.0625
>>> round(_, 2)
113.06
>>> "spam eggs"
'spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesnt"
'doesnt'
>>> '"yes," they said.'
'"yes," they said.'
>>> "\yes,\" they said."
'\\yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> print('"Isn\'t," they said.')
"Isn't," they said.
>>> s = 'First line.\nSecond line.'
>>> s
'First line.\nSecond line.'
>>> print(s)
First line.
Second line.
>>> print('C:\some\name')
C:\some
ame
>>> print(r'C:\some\name')
C:\some\name
>>> print("""\
Usage: thingy [options]
-h
-H hostname
""")
Usage: thingy [options]
-h
-H hostname

>>> 3 * 'un' + 'ium'
'unununium'
>>> 'py' 'thon
SyntaxError: EOL while scanning string literal
>>> print("hello world")
hello world
>>> print("lol")
lol
>>> 
