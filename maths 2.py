Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 2
>>> if x == 2:
	print x
	
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> else:
	
SyntaxError: invalid syntax
>>> print y
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(y)?
>>> x = 2
>>> if x == 2:
	else:
		
SyntaxError: invalid syntax
>>> print(x)
2
>>> print(y)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print(y)
NameError: name 'y' is not defined
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
>>> import sys
>>> print sys.argv[1]
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(sys.argv[1])?
>>> $ python echo.py hello
SyntaxError: invalid syntax
>>> hello
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> $ python echo.py hello world
SyntaxError: invalid syntax
>>> hello
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    hello
NameError: name 'hello' is not defined
>>> $ python add.py 3 5
SyntaxError: invalid syntax
>>> 8
8
>>> $ python add.py 29
SyntaxError: invalid syntax
>>> 11
11
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
>>> range(3, 6)
range(3, 6)
>>> range(2, 10, 3)
range(2, 10, 3)
>>> a = [1, 2, 3]
>>> b = [4, 5]
>>> a + b
[1, 2, 3, 4, 5]
>>> [1, 2, 3, 4, 5]
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
  File "<pyshell#54>", line 1, in <module>
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
>>> x[0:6:2]
range(0, 6, 2)
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
>>> print x
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(x)?
>>> print(x)
[0, 1, [3]]
>>> x[2] = 2
>>> print(x)
[0, 1, 2]
>>> for x in [1, 2, 3, 4]:
	print(x)
	for i  in range(10):
		print(i, i*i, i*i*i)

		
1
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
2
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
3
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
4
0 0 0
1 1 1
2 4 8
3 9 27
4 16 64
5 25 125
6 36 216
7 49 343
8 64 512
9 81 729
>>> zip(["a", "b", "c"], [1, 2, 3])
<zip object at 0x10b1d42c8>
>>> names = ["a", "b", "c"]
>>> values = [1, 2 3]
SyntaxError: invalid syntax
>>> for name, value in zip(names, values):
	print(name, value)

	
Traceback (most recent call last):
  File "<pyshell#95>", line 1, in <module>
    for name, value in zip(names, values):
NameError: name 'values' is not defined
>>> sum([1, 2, 3])
6
>>> sum(["hello", "world"])
Traceback (most recent call last):
  File "<pyshell#97>", line 1, in <module>
    sum(["hello", "world"])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> sum(["aa", "bb", "cc"])
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    sum(["aa", "bb", "cc"])
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> product([1, 2, 3])
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    product([1, 2, 3])
NameError: name 'product' is not defined
>>> factorial(4)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    factorial(4)
NameError: name 'factorial' is not defined
>>> reverse([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    reverse([1, 2, 3, 4])
NameError: name 'reverse' is not defined
>>> reverse(reverse([1, 2, 3, 4]))
Traceback (most recent call last):
  File "<pyshell#102>", line 1, in <module>
    reverse(reverse([1, 2, 3, 4]))
NameError: name 'reverse' is not defined
>>> cumulative_sum([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#103>", line 1, in <module>
    cumulative_sum([1, 2, 3, 4])
NameError: name 'cumulative_sum' is not defined
>>> cumulative_sum([4, 3, 2, 1])
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    cumulative_sum([4, 3, 2, 1])
NameError: name 'cumulative_sum' is not defined
>>> cumulative_product([1, 2, 3, 4])
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    cumulative_product([1, 2, 3, 4])
NameError: name 'cumulative_product' is not defined
>>> cumulative_product([4, 3, 2, 1])
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    cumulative_product([4, 3, 2, 1])
NameError: name 'cumulative_product' is not defined
>>> unique([1, 2, 1, 3, 2, 5])
Traceback (most recent call last):
  File "<pyshell#107>", line 1, in <module>
    unique([1, 2, 1, 3, 2, 5])
NameError: name 'unique' is not defined
>>> dups([1, 2, 1, 3, 2, 5])
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    dups([1, 2, 1, 3, 2, 5])
NameError: name 'dups' is not defined
>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
NameError: name 'group' is not defined
>>> group([1, 2, 3, 4, 5, 6, 7, 8, 9, 4)
	  
SyntaxError: invalid syntax
>>> a = [2, 10, 4, 3, 7]
	  
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
  File "<pyshell#118>", line 1, in <module>
    a.sort()
TypeError: '<' not supported between instances of 'int' and 'str'
>>> a
	  
['hello', 1, 'world', 45, 2]
>>> a = [[2, 3], [1, 6]
	 a.sort()
	 
SyntaxError: invalid syntax
>>> a
	 
['hello', 1, 'world', 45, 2]
>>> a = [[2, 3], [4, 6], [6, 1]]
	 
>>> a.sort(key=lamba x: x[1])
	 
SyntaxError: invalid syntax
>>> a
	 
[[2, 3], [4, 6], [6, 1]]
>>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
	 
Traceback (most recent call last):
  File "<pyshell#126>", line 1, in <module>
    lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
NameError: name 'lensort' is not defined
>>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
	 
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
NameError: name 'unique' is not defined
>>> a = (1, 2, 3)
	 
>>> a[0]
	 
1
>>> a = 1, 2, 3
	 
>>> a[0]
	 
1
>>> len(a)
	 
3
>>> a[1:]
	 
(2, 3)
>>> a = 91)
	  
SyntaxError: invalid syntax
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
>>> x = [3, 1, 2, 1]
	  
>>> set([1, 2, 3])
	  
{1, 2, 3}
>>> x = set([1, 2, 3])
	  
>>> x.add(4)
	  
>>> x
	  
{1, 2, 3, 4}
>>> set([1, 2, 3, 4])
	  
{1, 2, 3, 4}
>>> x = set([1, 2, 3])
	  
>>> 1 in x
	  
True
>>> 5 in x
	  
False
>>> len("abrakadabra")
	  
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
>>> a[-2:]
	  
'ld'
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
>>> 'Chapter %d: %s' % (2, 'Data Structures')
	  
'Chapter 2: Data Structures'
>>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
	  
Traceback (most recent call last):
  File "<pyshell#174>", line 1, in <module>
    extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
NameError: name 'extsort' is not defined
>>> f = open('foo.txt', 'r')
	  
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    f = open('foo.txt', 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'foo.txt'
>>> f = open('foo.txt', 'w')
	  
>>> f = open('foo.txt', 'a')
	  
>>> open('foo.txt').read()
	  
''
>>> 'first line\nsecond line\nlast line\n'
	  
'first line\nsecond line\nlast line\n'
>>> open('foo.txt').readlines()
	  
[]
>>> f = open('foo.txt')
	  
>>> f.readline()
	  
''
>>> f.readline()
	  
''
>>> f = open('foo.txt', 'w')
	  
>>> f.write('a\nb\nc')
	  
5
>>> f.close()
	  
>>> f.open('foo.txt', 'a')
	  
Traceback (most recent call last):
  File "<pyshell#187>", line 1, in <module>
    f.open('foo.txt', 'a')
AttributeError: '_io.TextIOWrapper' object has no attribute 'open'
>>> f.write('d\n')
	  
Traceback (most recent call last):
  File "<pyshell#188>", line 1, in <module>
    f.write('d\n')
ValueError: I/O operation on closed file.
>>> f.close()
	  
>>> f = open('foo.txt')
	  
>>> f.writelines(['a\n', 'b\n', 'c\n'])
	  
Traceback (most recent call last):
  File "<pyshell#191>", line 1, in <module>
    f.writelines(['a\n', 'b\n', 'c\n'])
io.UnsupportedOperation: not writable
>>> def charcount(filename):
	  return len(open(filename).read())

	  
>>> def wordcount(filename).read())
SyntaxError: invalid syntax
>>> def wordcount(filename):
	return len(open(filename).read().split())

>>> def linecount(filename):
	return len(open(filename).readlines())

>>> a = range(10)
>>> a
range(0, 10)
>>> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9,]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [x for x in a]
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
<zip object at 0x10b1cedc8>
>>> [(1, 2), (2, 3), (3, 5), (4, 7)]
[(1, 2), (2, 3), (3, 5), (4, 7)]
>>> [x+y for x, y in zip(a, b)]
[3, 5, 8, 11]
>>> n = 25
>>> [(x, y, z) for x in range(1, n) for y in range(x, n) for z in range(y, n) if x*x
     [(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 15, 17), (9, 12, 15), (12, 16, 20)]
     
