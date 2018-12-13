Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> var = 12
>>> var = 69
>>> var = 12345
>>> var = 4
>>> a = range(10)
>>> a
range(0, 10)
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x for x in a]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x*x for x in a]
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x+1 for x in a]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a = range(10)
>>> [x for x in a if x % 2 == 0]
[0, 2, 4, 6, 8]
>>> [x*x for x in a if x%2 == 0]
[0, 4, 16, 36, 64]
>>> a = [1, 2, 3, 4]
>>> b = [2, 3, 5, 7]
>>> zip(a, b)
<zip object at 0x10f85bf48>
>>> a = [1, 2, 3, 4]
>>> b = [2, 3, 5, 7]
>>> zip(a, b)
<zip object at 0x10f85bf88>
>>> [(1, 2), (2, 3), (3, 5), (4, 7)]
[(1, 2), (2, 3), (3, 5), (4, 7)]
>>> [x+y for x, y in zip(a, b)]
[3, 5, 8, 11]
>>> [(x, y) for x in range(5) for y in range(5) if (x+y) % 2 == 0]
[(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (4, 0), (4, 2), (4, 4)]
>>> [(x. y) for x in range(5) for y in range(5) if (x+y) %2 == o and x != y]
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    [(x. y) for x in range(5) for y in range(5) if (x+y) %2 == o and x != y]
  File "<pyshell#23>", line 1, in <listcomp>
    [(x. y) for x in range(5) for y in range(5) if (x+y) %2 == o and x != y]
NameError: name 'o' is not defined
>>> [(x, y) for x in range(5) for y in range(5) if (x+y) %2 == 0]
[(0, 0), (0, 2), (0, 4), (1, 1), (1, 3), (2, 0), (2, 2), (2, 4), (3, 1), (3, 3), (4, 0), (4, 2), (4, 4)]
>>> n = 25
>>> [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x + y*y == z*z
print(x, y, z)
     
SyntaxError: invalid syntax
>>> print("x, y, z")
     
x, y, z
>>> def square(x): return x * x

     
>>> map(square, range(5))
     
<map object at 0x10de205c0>
>>> def even(x): return x %2 == 0

     
>>> filter(even, range(10))
     
<filter object at 0x10de207b8>
>>> triplets(5)
     
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    triplets(5)
NameError: name 'triplets' is not defined
>>> enumerate(["a", "b", "c"])
     
<enumerate object at 0x10de18990>
>>> [(0, "a"), (1, "b"), (2, "c")]
     
[(0, 'a'), (1, 'b'), (2, 'c')]
>>> for index, value in enumerate(["a", "b", "c"]):
     print index, value
     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(index, value)?
>>> print("index, value")
     
index, value
>>> a = array(2, 3)
     
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    a = array(2, 3)
NameError: name 'array' is not defined
>>> a
     
[1, 2, 3, 4]
>>> [[None, None, None], [None, None, None]]
     
[[None, None, None], [None, None, None]]
>>> a[0] [0] = 5
     
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    a[0] [0] = 5
TypeError: 'int' object does not support item assignment
>>> [[5, None None], [None, None, None]]
     
SyntaxError: invalid syntax
>>> printopen('a.csv').read()
     
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    printopen('a.csv').read()
NameError: name 'printopen' is not defined
>>> a,b,c
     
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a,b,c
NameError: name 'c' is not defined
>>> 1,2,3
     
(1, 2, 3)
>>> 2,3,4
     
(2, 3, 4)
>>> 3,4,5
     
(3, 4, 5)
>>> parse_csv('a.csv')
     
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    parse_csv('a.csv')
NameError: name 'parse_csv' is not defined
>>> [['a', 'b', 'c'], ['1', '2', '3'] ['2', '3', '4'], ['3', '4', '5']]
     
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    [['a', 'b', 'c'], ['1', '2', '3'] ['2', '3', '4'], ['3', '4', '5']]
TypeError: list indices must be integers or slices, not tuple
>>> print open('a.txt').read()
     
SyntaxError: invalid syntax
>>> a!b!c
     
SyntaxError: invalid syntax
>>> 1!1!3
     
SyntaxError: invalid syntax
>>> 2!3!4
     
SyntaxError: invalid syntax
>>> 3!4!5
     
SyntaxError: invalid syntax
>>> parse("a.txt', '!', '#')
	  
SyntaxError: EOL while scanning string literal
>>> [['a', 'b', 'c'], ['1', '2', '3']
     ['2', '3', '4'], ['3', '4', '5']]
	  
Traceback (most recent call last):
  File "<pyshell#62>", line 2, in <module>
    ['2', '3', '4'], ['3', '4', '5']]
TypeError: list indices must be integers or slices, not tuple
>>> words = mutate('hello')
     
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    words = mutate('hello')
NameError: name 'mutate' is not defined
>>> 'helo' in words
     
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    'helo' in words
NameError: name 'words' is not defined
>>> 'cello' in words
     
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    'cello' in words
NameError: name 'words' is not defined
>>> 'helo' in words
     
Traceback (most recent call last):
  File "<pyshell#66>", line 1, in <module>
    'helo' in words
NameError: name 'words' is not defined
>>> nearly_equal('python', 'perl')
     
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    nearly_equal('python', 'perl')
NameError: name 'nearly_equal' is not defined
>>> nearly_equal('perl', 'pearl')
     
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    nearly_equal('perl', 'pearl')
NameError: name 'nearly_equal' is not defined
>>> nearly_equal('python', 'jython')
     
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    nearly_equal('python', 'jython')
NameError: name 'nearly_equal' is not defined
>>> nearly_equal('man', 'woman')
     
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    nearly_equal('man', 'woman')
NameError: name 'nearly_equal' is not defined
>>> a = {'x': 1, 'y': 2, 'z': 3}
     
>>> a['x']
     
1
>>> a['z']
     
3
>>> b = {}
     
>>> b['x'] = 2
     
>>> b[2] = 'foo'
     
>>> b[(1, 2)] = 3
     
>>> b
     
{'x': 2, 2: 'foo', (1, 2): 3}
>>> {(1, 2): 3, 'x': 2, 3: 'foo')
     
SyntaxError: invalid syntax
>>> a = {'x': 1, 'y': 2, 'z': 3}
     
>>> del a['x']
     
>>> a
     
{'y': 2, 'z': 3}
>>> 
a.keys()
     
dict_keys(['y', 'z'])
>>> ['x', 'y', 'z']
     
['x', 'y', 'z']
>>> a.values()
     
dict_values([2, 3])
>>> [1, 2, 3]
     
[1, 2, 3]
>>> a.items()
     
dict_items([('y', 2), ('z', 3)])
>>> [('x', 1), ('y', 2), ('z', 3)]
     
[('x', 1), ('y', 2), ('z', 3)]
>>> for key in a: print key
     
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(key)?
>>> x
     
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> for key, value in a.items(): print key, value
     
SyntaxError: invalid syntax
>>> x = 1
     
>>> y = 2
     
>>> z = 3
     
>>> 'x' in a
     
False
>>> 'p' in a
     
False
>>> a.has_key('x')
     
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    a.has_key('x')
AttributeError: 'dict' object has no attribute 'has_key'
>>> a.has_key('p')
     
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    a.has_key('p')
AttributeError: 'dict' object has no attribute 'has_key'
>>> d = {'x': 1, 'y': 2, 'z': 3}
     
>>> d.get('x', 5)
     
1
>>> d.get('p', 5)
     
5
>>> d.setdefaault('x', 0)
     
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    d.setdefaault('x', 0)
AttributeError: 'dict' object has no attribute 'setdefaault'
>>> d
     
{'x': 1, 'y': 2, 'z': 3}
>>> d.setdefault('p', 0)
     
0
>>> d
     
{'x': 1, 'y': 2, 'z': 3, 'p': 0}
>>> 'hello % {'name': 'python'}
     
SyntaxError: invalid syntax
>>> 'Chapter %(index)d: %(name)s' % {'index': 2, 'name': 'Data Structures'}
     
'Chapter 2: Data Structures'
>>> def word_frequency(words):
"""Returns frequency of each word given a list of words.
print("Hello world!", end = '')
