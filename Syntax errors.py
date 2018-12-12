Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 1
2
>>> 2 + 2
4
>>> 234 + 3
237
>>> numcalls = 0
>>> def square (x):
	global numcalls
	numcalls = numcalls + 1
	return x * x

>>> print square(5)
SyntaxError: invalid syntax
>>> print square(2 * 5)
SyntaxError: invalid syntax
>>> x = 1
>>> def f():
	x = 2
	return x
print(x)
SyntaxError: invalid syntax
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print f()
SyntaxError: invalid syntax
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
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
>>> def increment (x, amount=1):
	return x + amount

>>> increment(10)
11
>>> increment(10, 5)
15
>>> increment(10, amount=2)
12
>>> cube = lambda x: x ** 3
>>> fxy(cube, 2, 3)
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    fxy(cube, 2, 3)
NameError: name 'fxy' is not defined
>>> fxy(lambda x: x ** 3, 2, 3)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    fxy(lambda x: x ** 3, 2, 3)
NameError: name 'fxy' is not defined
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
  File "<pyshell#40>", line 1, in <module>
    count_digits(5)
NameError: name 'count_digits' is not defined
>>> count_digits(12345)
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    count_digits(12345)
NameError: name 'count_digits' is not defined
>>> x = "hello"
>>> print x.upper()
SyntaxError: invalid syntax
>>> print("x.upper"())
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    print("x.upper"())
TypeError: 'str' object is not callable
>>> f = x.upper
>>> print f()
SyntaxError: invalid syntax
>>> istrcmp('python', 'python')
Traceback (most recent call last):
  File "<pyshell#47>", line 1, in <module>
    istrcmp('python', 'python')
NameError: name 'istrcmp' is not defined
>>> istrcmp('LateX', 'Latex')
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    istrcmp('LateX', 'Latex')
NameError: name 'istrcmp' is not defined
>>> istrcmp('a', 'b')
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
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
>>> "python" < "java"
False
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
>>> x = 4
>>> y = 5
>>> p = x < y or x < z
>>> print("p")
p
>>> True,  False= False, True
SyntaxError: can't assign to keyword
>>> print True, False
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(True, False)?
>>> print 2 < 3
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(2 < 3)?
>>> x = 42
>>> if x % 2 == 0: print 'even'
SyntaxError: Missing parentheses in call to 'print'. Did you mean print('even')?
>>> if x % 2 == 0:
	print('even')

	
even
>>> x = 3
>>> if x % 2 == 0:
	print('even')
	else:
		
SyntaxError: invalid syntax
>>> print('odd')
odd
>>> x = 42
>>> if x < 10:
	print('one digit number')
	elif x < 100:
		
SyntaxError: invalid syntax
>>> print('two digit number')
two digit number
>>> else:
	
SyntaxError: invalid syntax
>>> print('big number')
big number
>>> x = 2
>>> if x == 2::
	
SyntaxError: invalid syntax
>>> print(x)
2
>>> else:
	
SyntaxError: invalid syntax
>>> print(y)
5
>>> x = 2
>>> if x == 2:
	print(x)
	else:
		
SyntaxError: invalid syntax
>>> x +
SyntaxError: invalid syntax
>>> x = [1, 2, 3]
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
'Wed Dec 12 11:26:54 2018'
>>> import sys
>>> print sys.argv[1]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sys.argv[1])?
>>> $ python echo.py hello
SyntaxError: invalid syntax
>>> hello
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> $ python echo.py hello world
SyntaxError: invalid syntax
>>> hello
Traceback (most recent call last):
  File "<pyshell#111>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> $ python add.py 3 5
SyntaxError: invalid syntax
>>> 8
8
>>> % python add.py 29
SyntaxError: invalid syntax
>>> 11
11
>>> 10
10
>>> bro
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    bro
NameError: name 'bro' is not defined
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
>>> range(2, 10, 3)
range(2, 10, 3)
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
>>> x = [1, 2, 3, 4]
>>> x[6]
Traceback (most recent call last):
  File "<pyshell#137>", line 1, in <module>
    x[6]
IndexError: list index out of range
>>> x = [1, 2, 3, 4]
>>> x[-1]
4
>>> x [-2]
3
>>> x = [1, 2, 3, 4]
>>> x[0:2]
[1, 2]
>>> x{1:4]
SyntaxError: invalid syntax
>>> x[1:4]
[2, 3, 4]
>>> x[0:-1]
[1, 2, 3]
>>> x = [1, 2, 3, 4]
>>> a[:2]
[1, 2]
>>> a[2:]
[3]
>>> a[:]
[1, 2, 3]
>>> x = range(10)
>>> x
range(0, 10)
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10,]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 8, 10]
>>> x[0:6:2]
range(0, 6, 2)
>>> x[x::-1]
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    x[x::-1]
TypeError: slice indices must be integers or None or have an __index__ method
>>> x[::-1]
range(9, -1, -1)
>>> x[::-1]
range(9, -1, -1)
>>> x = [1, 2, 3, 4]
>>> x[1] = 5
>>> x
[1, 5, 3, 4]
>>> x = [1, 2, 3, 4]
>>> 2 in x
True
>>> 10 in x
False
>>> a = [1, 2]
>>> a.append(3)
>>> a
[1, 2, 3]
>>> x = [0, 1, [2]]
>>> x[2] [0] = 3
>>> print(x)
[0, 1, [3]]
>>> x[2].append(4)
>>> print(x)
[0, 1, [3, 4]]
>>> x[2] = 2
>>> print(x)
[0, 1, 2]
>>> for x in [1, 2, 3, 4]:
	print(x)
	for i range(10):
		
SyntaxError: invalid syntax
>>> print("i, i*i, i*i*i")
i, i*i, i*i*i
>>> zip(["a", "b", "c"], [1, 2, 3])
<zip object at 0x10e2586c8>
>>> names = ["a", "b", "c"]
>>> values = [1, 2, 3]
>>> for name, value in zip(names, values):
	print("name, value")

	
name, value
name, value
name, value
>>> sum([1, 2, 3])
6
>>> sum(["hello", "world"])
Traceback (most recent call last):
  File "<pyshell#184>", line 1, in <module>
    sum(["hello", "world"])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(["aa", "bb", "cc"])
Traceback (most recent call last):
  File "<pyshell#185>", line 1, in <module>
    sum(["aa", "bb", "cc"])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> product([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#186>", line 1, in <module>
    product([1, 2, 3])
NameError: name 'product' is not defined
>>> factorial(4)
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    factorial(4)
NameError: name 'factorial' is not defined
>>> reverse([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    reverse([1, 2, 3, 4])
NameError: name 'reverse' is not defined
>>> reverse(reverse([1, 2, 3, 4])
	    [1, 2, 3, 4]

var = x
	    
SyntaxError: invalid syntax
>>> cumulative_sum([1, 2, 3, 4])
	    
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    cumulative_sum([1, 2, 3, 4])
NameError: name 'cumulative_sum' is not defined
>>> cumulative_sum([4, 3, 2, 1])
	    
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    cumulative_sum([4, 3, 2, 1])
NameError: name 'cumulative_sum' is not defined
>>> unique([1, 2, 1, 3, 2, 5])
	    
Traceback (most recent call last):
  File "<pyshell#197>", line 1, in <module>
    unique([1, 2, 1, 3, 2, 5])
NameError: name 'unique' is not defined
>>> [1, 2, 3, 5]
	    
[1, 2, 3, 5]
>>> dups([1, 2, 1, 3, 2, 5])
	    
Traceback (most recent call last):
  File "<pyshell#199>", line 1, in <module>
    dups([1, 2, 1, 3, 2, 5])
NameError: name 'dups' is not defined
>>> [1, 2]
	    
[1, 2]
>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
	    
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
NameError: name 'group' is not defined
>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
	    
Traceback (most recent call last):
  File "<pyshell#202>", line 1, in <module>
    group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
NameError: name 'group' is not defined
>>> a = [2, 10 , 4, 3, 7]
	    
>>> a.sort()
	    
>>> a
	    
[2, 3, 4, 7, 10]
>>> a = [4, 3, 5, 9, 2]
	    
>>> sorted(a)
	    
[2, 3, 4, 5, 9]
>>> a
	    
[4, 3, 5, 9, 2]
>>> a = ["hello", 1, "world", 45, 2]
	    
>>> a.sort()
	    
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a
	    
['hello', 1, 'world', 45, 2]
>>> a = [[2, 3], [1, 6]]
	    
>>> a.sort()
	    
>>> a
	    
[[1, 6], [2, 3]]
>>> a = [[2, 3], [4, 6], [6, 1]]
	    
>>> a.sort(key=lambda x: x[1])
	    
>>> a
	    
[[6, 1], [2, 3], [4, 6]]
>>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
	    
Traceback (most recent call last):
  File "<pyshell#218>", line 1, in <module>
    lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
NameError: name 'lensort' is not defined
>>> ['c', 'perl', 'java', 'ruby', 'python', 'haskell']
	    
['c', 'perl', 'java', 'ruby', 'python', 'haskell']
>>> unique(["python", "java", "Python", "java"], key=lambda s: s.lower())
	    
Traceback (most recent call last):
  File "<pyshell#220>", line 1, in <module>
    unique(["python", "java", "Python", "java"], key=lambda s: s.lower())
NameError: name 'unique' is not defined
>>> a = (1, 2, 3)
	    
>>> a[0]
	    
1
>>> len(a)
	    
3
>>> a[1:]
	    
(2, 3)
>>> a = (1)
	    
>>> a
	    
1
>>> b = (1,)
	    
>>> b
	    
(1,)
>>> b[0]
	    
1
>>> x = set([3, 1, 2, 1])
	    
>>> set([1, 2, 3])
	    
{1, 2, 3}
>>> x = {3, 1, 2, 1}
	    
>>> set([1, 2, 3])
	    
{1, 2, 3}
>>> x = set([1, 2, 3])
	    
>>> x.add(4)
	    
>>> x
	    
{1, 2, 3, 4}
>>> set([1, 2, 3, 4])
	    
{1, 2, 3, 4}
>>> x = set([1' 2' 3])
	    
SyntaxError: invalid syntax
>>> 1 in x
	    
True
>>> 5 in x
	    
False
>>> len("abrakadadra")
	    
11
>>> a = "helloworld"
	    
>>> a[1]
	    
'e'
>>> a[-2]
	    
'l'
>>> a[1:5]
	    
'ello'
>>> a[:5]
	    
'hello'
>>> a[5:]
	    
'world'
>>> a[:-2]
	    
'hellowor'
>>> a[::-1]
	    
'dlrowolleh'
>>> 'hell' in 'hello'
	    
True
>>> 'full' in 'hello'
	    
False
>>> 'el' in 'hello'
	    
True
>>> "hello world".split()
	    
['hello', 'world']
>>> "a,b,c".split(',')
	    
['a', 'b', 'c']
>>> "".join(['hello', 'world'])
	    
'helloworld'
>>> ','.join(['a', 'b', 'c'])
	    
'a,b,c'
>>> ' hello world\n'.strip()
	    
'hello world'
>>> 'abcdefgh'.strip('abdh')
	    
'cdefg'
>>> a = 'hello'
	    
>>> b = 'python'
	    
>>> "%s %s" % (a, b)
	    
'hello python'
>>> "Chapter %d: %s' % (2, 'Data Structures')
	    
SyntaxError: EOL while scanning string literal
>>> ('Chapter %d: %s' % ("2, 'Data Structures')
			 
SyntaxError: EOL while scanning string literal
>>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c])
	     
SyntaxError: EOL while scanning string literal
>>> ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
	     
['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
>>> f = open('foo.txt', 'r')
	     
>>> f = open('foo.txt', 'w')
	     
>>> open('foo.txt').readlines()
	     
[]
>>> ['first line\n', 'second line\n', 'last line\n']
	     
['first line\n', 'second line\n', 'last line\n']
>>> f = open('foo.txt')
	     
>>> f.readline()
	     
''
>>> 'first line\n'
	     
'first line\n'
>>> f.readline()
	     
''
>>> 'second line\n'
	     
'second line\n'
>>> f.readline()
	     
''
>>> 'last line\n'
	     
'last line\n'
>>> f.readline()
	     
''
>>> f = open('foo.txt', 'w')
	     
>>> f.write('aa\nb\nc')
	     
6
>>> f.close()
	     
>>> f.open('foo.txt', 'a')
	     
Traceback (most recent call last):
  File "<pyshell#281>", line 1, in <module>
    f.open('foo.txt', 'a')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> f.write('d\n')
	     
Traceback (most recent call last):
  File "<pyshell#282>", line 1, in <module>
    f.write('d\n')
ValueError: I/O operation on closed file.
>>> f.close()
	     
>>> f = open('foo.txt')
	     
>>> f.writelines(['a\n', 'b\n', 'c\n'])
	     
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    f.writelines(['a\n', 'b\n', 'c\n'])
io.UnsupportedOperation: not writable
>>> f.close()
	     
>>> def charcount(filename):
	     return len(open(filename).read())

	     
>>> def wordcount(filename):
	     return len(open(filename).read().split())

	     
>>> a = range(10)
	     
>>> a
	     
range(0, 10)
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
	     
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x for x in a]
	     
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x*x for x in a]
	     
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
>>> [x+1 for x in a]
	     
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> a = range(100
	      [x for x in a if x % 2 == 0]
	      
SyntaxError: invalid syntax
>>> [0, 2, 3, 6, 8]
	      
[0, 2, 3, 6, 8]
>>> [x*x for x in a if x%2 == 0]
	      
[0, 4, 16, 36, 64]
>>> a = [1, 2, 3, 4]
	      
>>> b = [2, 3, 5, 7]
	      
>>> zip(a, b)
	      
<zip object at 0x10e1e8f48>
>>> [(1, 2), (2, 3), (3, 5), (4, 7)]
	      
[(1, 2), (2, 3), (3, 5), (4, 7)]
>>> [x+y for x, y in zip(a, b)]
	      
[3, 5, 8, 11]
>>> 
