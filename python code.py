Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
>>> for key in counts:
	if counts[key] > 10:
		print(key, counts[key])

		
annie 42
jan 100
>>> counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
>>> lst = list(counts.keys())
>>> print(lst)
['chuck', 'annie', 'jan']
>>> lst.sort()
>>> for key in 1st:
	
SyntaxError: invalid syntax
>>> for key in lst:
	print(key, counts[key])

	
annie 42
chuck 1
jan 100
>>> import string
>>> string.puntuation
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    string.puntuation
AttributeError: module 'string' has no attribute 'puntuation'
>>> import string
>>> fname = input('Enter the file name: ')
Enter the file name: try:
>>> fhand = open(fname)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    fhand = open(fname)
FileNotFoundError: [Errno 2] No such file or directory: 'try:'
>>> except:
	
SyntaxError: invalid syntax
>>> print('File cannot be opened:', fname)
File cannot be opened: try:
>>> exit()
>>> counts = dict()
>>> for line in fhand:
	line = line.rstrip()
	line = line.translate(line.maketrans('','', string.punctuation))
	line = line.lower()
	words = line.split()
	for word not in counts:
		
SyntaxError: invalid syntax
>>> counts[word] = 1
Traceback (most recent call last):
  File "<pyshell#28>", line 1, in <module>
    counts[word] = 1
NameError: name 'word' is not defined
>>> else:
	
SyntaxError: invalid syntax
>>> counts[word] += 1
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    counts[word] += 1
NameError: name 'word' is not defined
>>> print(counts)
{}
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> t1 = ('a',)
>>> type(t1)
<class 'tuple'>
>>> t2 = ('a')
>>> type(t2)
<class 'str'>
>>> t = tuple()
>>> print(t)
()
>>> t = tuple('lupins')
>>> print(t)
('l', 'u', 'p', 'i', 'n', 's')
>>> t = ('a', 'b', 'c', 'd', 'e')
>>> print(t[0])
a
>>> print(t[1:3])
('b', 'c')
>>> t[0] = 'A'
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    t[0] = 'A'
TypeError: 'tuple' object does not support item assignment
>>> T = ('A',) + T[1:]
Traceback (most recent call last):
  File "<pyshell#45>", line 1, in <module>
    T = ('A',) + T[1:]
NameError: name 'T' is not defined
>>> PRINT(T)
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    PRINT(T)
NameError: name 'PRINT' is not defined
>>> t = 9'A',) + t[1:]
SyntaxError: invalid syntax
>>> t = ('A',) + t[1:]
>>> print(t)
('A', 'b', 'c', 'd', 'e')
>>> (0, 1, 2) < (0, 3, 4)
True
>>> (0, 1, 2000000) < (0, 3, 4)
True
>>> txt = 'but soft what light in yonder window breaks'
>>> words = txt.split()
>>> t = list()
>>> for word in words:
	t.append((len(word), word))
	t.sort(reverse=True)
	res = list()
	for length, word in t:
		res.append(word)
		print(res)

		
['but']
['soft']
['soft', 'but']
['what']
['what', 'soft']
['what', 'soft', 'but']
['light']
['light', 'what']
['light', 'what', 'soft']
['light', 'what', 'soft', 'but']
['light']
['light', 'what']
['light', 'what', 'soft']
['light', 'what', 'soft', 'but']
['light', 'what', 'soft', 'but', 'in']
['yonder']
['yonder', 'light']
['yonder', 'light', 'what']
['yonder', 'light', 'what', 'soft']
['yonder', 'light', 'what', 'soft', 'but']
['yonder', 'light', 'what', 'soft', 'but', 'in']
['yonder']
['yonder', 'window']
['yonder', 'window', 'light']
['yonder', 'window', 'light', 'what']
['yonder', 'window', 'light', 'what', 'soft']
['yonder', 'window', 'light', 'what', 'soft', 'but']
['yonder', 'window', 'light', 'what', 'soft', 'but', 'in']
['yonder']
['yonder', 'window']
['yonder', 'window', 'breaks']
['yonder', 'window', 'breaks', 'light']
['yonder', 'window', 'breaks', 'light', 'what']
['yonder', 'window', 'breaks', 'light', 'what', 'soft']
['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but']
['yonder', 'window', 'breaks', 'light', 'what', 'soft', 'but', 'in']
>>> m = [ 'have', 'fun' ]
>>> x, y=m
>>> x
'have'
>>> y
'fun'
>>> m = [ 'have', 'fun' ]
>>> x =m[0]
>>> y =m[1]
>>> x
'have'
>>> y
'fun'
>>> m = [ 'have', 'fun' ]
>>> (x, y) = m
>>> x
'have'
>>> y
'fun'
>>> a, b = b, a
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    a, b = b, a
NameError: name 'b' is not defined
>>> a, b = 1, 2, 3
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    a, b = 1, 2, 3
ValueError: too many values to unpack (expected 2)
>>> addr = 'monty@python.org'
>>> uname, domain = addr.split('@')
>>> print(uname)
monty
>>> print(domain)
python.org
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> print(t)
[('a', 10), ('b', 1), ('c', 22)]
>>> d = {'a':10, 'b':1, 'c':22}
>>> t = list(d.items())
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> t
[('a', 10), ('b', 1), ('c', 22)]
>>> for key, val in list(d.items()):
	print(val, key)

	
10 a
1 b
22 c
>>> d = {'a':10, 'b':1, 'c':22}
>>> l = list()
>>> for key, val in d.items() :
	l.append( (val, key) )

	
>>> 1
1
>>> [(10, 'a'), (22, 'c'), (1, 'b')]
[(10, 'a'), (22, 'c'), (1, 'b')]
>>> 1.sort(reverse=True)
SyntaxError: invalid syntax
>>> l.sort(reverse=True)
>>> 1
1
>>> [(22, 'c'), (10, 'a'), (1, 'b')]
[(22, 'c'), (10, 'a'), (1, 'b')]
>>> import string
>>> fhand = open('romeo-full.txt')
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    fhand = open('romeo-full.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'romeo-full.txt'
>>> counts = dict()
>>> for line in fhand:
	line = line.translate9str.maketrans('', '', string.punctuation))
	
SyntaxError: invalid syntax
>>> line = line.lower()
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    line = line.lower()
NameError: name 'line' is not defined
>>> words = line.split()
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    words = line.split()
NameError: name 'line' is not defined
>>> for word in words:
	if word not in counts:
		counts[word] = 1
		else:
			
SyntaxError: invalid syntax
>>> counts[word] += 1
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    counts[word] += 1
KeyError: 'in'
>>> lst = list()
>>> for key, val in list(counts.items()):
	lst.append((val, key))
	lst.sort(reverse=True)
	for key, val in lst[:10]:
		print(key, val)

		
>>> directory[last,first] = number
Traceback (most recent call last):
  File "<pyshell#122>", line 1, in <module>
    directory[last,first] = number
NameError: name 'number' is not defined
>>> for last, first in  directory:
	print(first, last, directory[last,first])

	
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    for last, first in  directory:
NameError: name 'directory' is not defined
>>> import re
>>> hand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    hand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> for line in hand:
	line = line.rstrip()
	if re.search('From:', line):
		print(line)

		
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    for line in hand:
NameError: name 'hand' is not defined
>>> import re
>>> hand = open('mbox-short.txt')
Traceback (most recent call last):
  File "<pyshell#134>", line 1, in <module>
    hand = open('mbox-short.txt')
FileNotFoundError: [Errno 2] No such file or directory: 'mbox-short.txt'
>>> for line in hand:
	line = line.rstrip()
	if re.search('^From:', line):
		print(line)

		
Traceback (most recent call last):
  File "<pyshell#139>", line 1, in <module>
    for line in hand:
NameError: name 'hand' is not defined
>>> 
