Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> def square(x): return x * x

>>> map(square, range(5))
<map object at 0x10967add8>
>>> [0, 1, 4, 9, 16]
[0, 1, 4, 9, 16]
>>> def even(x): return x %2 == 0

>>> filter(even, range(10))
<filter object at 0x10967add8>
>>> [0, 2, 4, 6, 8]
[0, 2, 4, 6, 8]
>>> triplets(5)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    triplets(5)
NameError: name 'triplets' is not defined
>>> enumerate(['a", "b", 'c"])
	       
SyntaxError: invalid syntax
>>> enumerate(["a", "b", "c"])
	       
<enumerate object at 0x10976c090>
>>> [(0, "a"), (1, "b"), (2, "c")]
	       
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> for index, value in enumerate(["a", "b", "c"]):
	       print index, value
	       
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(index, value)?
>>> print(index, value)
	       
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    print(index, value)
NameError: name 'index' is not defined
>>> a = array(2, 3)
	       
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a = array(2, 3)
NameError: name 'array' is not defined
>>> a
	       
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> a[0] [0] = 5
	       
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a[0] [0] = 5
NameError: name 'a' is not defined
>>> [[5, None, None], [None, None, None]]
	       
[[5, None, None], [None, None, None]]
>>> print open('a.csv').read()
	       
SyntaxError: invalid syntax
>>> a,b,c
	       
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a,b,c
NameError: name 'a' is not defined
>>> 1,2,3
	       
(1, 2, 3)
>>> 2,3,4
	       
(2, 3, 4)
>>> 3,4,5
	       
(3, 4, 5)
>>> parse_csv('a.csv')
	       
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    parse_csv('a.csv')
NameError: name 'parse_csv' is not defined
>>> [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4',] ['3', '4', '5']]
	       
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4',] ['3', '4', '5']]
TypeError: list indices must be integers or slices, not tuple
>>> print open('a.txt').read()
	       
SyntaxError: invalid syntax
>>> 
