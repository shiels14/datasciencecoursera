Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> fib
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    fib
NameError: name 'fib' is not defined
>>> fib <function fib at 10042ed0>
SyntaxError: invalid syntax
>>> f = fib
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    f = fib
NameError: name 'fib' is not defined
>>> f(100)
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f(100)
NameError: name 'f' is not defined
>>> def fib(n):
	# """write the series of the cars """
	a, b = 0, 1
	while a < n:
		print(a, end='')
		a, b = b, a+b
		print()

		
>>> # Now call a function
>>> fib(2000)
0
1
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
>>> fib
<function fib at 0x10d0d8c80>
>>> f = fib
>>> f(100)
0
1
1
2
3
5
8
13
21
34
55
89
>>> fib(0)
>>> print(fib(0))
None
>>> def fib2(n):
	result = []
	a, b = 0, 1
	while a < n:
		result.append(a)
		a, b = b, a+b
		return result

	
>>> f100 = fib2(100)
>>> f100
[0]
>>> def ask_ok(prompt, retries=4, reminder='Please try again!!'):
	while True:
		ok = input(prompt)
		if ok in ('y', 'ye', 'yes'):
			return True
		if ok in ('n', 'no', 'nop', 'nope'):
			return False
		retries = retries - 1
		if retries < 0:
			raise ValueError('invalid user response')
		print(reminder)

		
>>> i = 5
>>> def f(arg=1):
	print(arg)
	i = 6
	f()
	def f(a, L=[]):
		L.append(a)
		return L
	print(f(1))
	print(f(2))
	print(f(3))

	
>>> [1]
[1]
>>> [1, 2]
[1, 2]
>>> [1, 2, 3]
[1, 2, 3]
>>> def f(a, L=None):
	if L is None:
		L = []
		L.append(a)
		return L

	
>>> def parrot(voltage, state='a stiff', action='voom' type='Norwegian Blue'):
	
SyntaxError: invalid syntax
>>> print("--This parrot wouldn't", action, end='')
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print("--This parrot wouldn't", action, end='')
NameError: name 'action' is not defined
>>> print("if you put", voltage, "volts through it.")
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    print("if you put", voltage, "volts through it.")
NameError: name 'voltage' is not defined
>>> print("--Lovely plumage, the", type)
--Lovely plumage, the <class 'type'>
>>> print("--It's', state, "!")
	  
SyntaxError: invalid syntax
>>> list(range(3, 6))
	  
[3, 4, 5]
>>> args = [3, 6]
	  
>>> list(range(*args))
	  
[3, 4, 5]
>>> def make_incrementor(n):
	  return lambda x: x + n

	  
>>> f = make_incrementor(42)
	  
>>> f(0)
	  
42
>>> f(1)
	  
43
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
	  
>>> pairs.sort(key=lambda pair: pair[1])
	  
>>> pairs
	  
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
>>> 
