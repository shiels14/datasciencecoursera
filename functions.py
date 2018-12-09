Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> 1 + 1
2
>>> 2 + 2
4
>>> 6 + 6
12
>>> 144-3
141
>>> 10 - 10
0
>>> 5 + 56
61
>>> 100 % of 5
SyntaxError: invalid syntax
>>> 1234 - 4567
-3333
>>> print(integrity)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print(integrity)
NameError: name 'integrity' is not defined
>>> print("integrity")
integrity
>>> print("# reality")
# reality
>>> 9 + 9
18
>>> 3 * 3
9
>>> 34567 * 67
2315989
>>> print("i am awsome")
i am awsome
>>> a == b
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    a == b
NameError: name 'a' is not defined
>>> a != b
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    a != b
NameError: name 'a' is not defined
>>> a < b
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    a < b
NameError: name 'a' is not defined
>>> a <= b
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    a <= b
NameError: name 'a' is not defined
>>> a > b
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    a > b
NameError: name 'a' is not defined
>>> a >= b
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    a >= b
NameError: name 'a' is not defined
>>> a = 33
>>> b = 200
>>> if b > a:
	print("b is greater than a")

	
b is greater than a
>>> a = 23
>>> b = 200
>>> if b > a:
	print("b is greater than a")

	
b is greater than a
>>> a = 33
>>> b = 33
>>> if b > a:
	print("b is greater than a")
	elif a == b:
		
SyntaxError: invalid syntax
>>> print("a and b are equal")
a and b are equal
>>> a = 200
>>> b = 33
>>> if b > a:
	print("b is greater than a")
	elif a == b:
		
SyntaxError: invalid syntax
>>> print("a and b are equal")
a and b are equal
>>> else:
	
SyntaxError: invalid syntax
>>> print("a is greater than b")
a is greater than b
>>> a = 200
>>> b = 33
>>> if b > a:
	print("b is greater than a")
	else:
		
SyntaxError: invalid syntax
>>> print("b is not greater than a")
b is not greater than a
>>> if a > b: print("a is greater than b")

a is greater than b
>>> print("A") if a > b else print("B")
A
>>> print("A") if a > b else print("=") if a == b else print("B")
A
>>> if a > b and c > a:
	print("Both conditions are True")

	
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    if a > b and c > a:
NameError: name 'c' is not defined
>>> if a > b or a > c:
	print("At least one of the conditions are True")

	
At least one of the conditions are True
>>> a = 50
>>> b = 10
>>> if a > b:
	print('Hello World")
	      
SyntaxError: EOL while scanning string literal
>>> if a > b:
	      print("Hello World")

	      
Hello World
>>> i = 1
	      
>>> while i < 6:
	      print(i)
	      i += 1

	      
1
2
3
4
5
>>> i = 1
	      
>>> while i < 6:
	      print(i)
	      if i == 3:
	      break
	      
SyntaxError: expected an indented block
>>> i += 1
	      
>>> i = 0
	      
>>> while i < 6:
	      i += 1
	      if i == 3:
	      continue
	      
SyntaxError: expected an indented block
>>> print(i)
	      
0
>>> i = 1
	      
>>> while i < 6:
	      print(i)
	      i += 1

	      
1
2
3
4
5
>>> friuts = ["apple", "banana", "cherry"]
	      
>>> for x in fruits:
	      print(x)

	      
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    for x in fruits:
NameError: name 'fruits' is not defined
>>> for x in "banana":
	      print(x)

	      
b
a
n
a
n
a
>>> fruits = ["apple", "banana", "cherry"]
	      
>>> for x in fruits:
	      print(x)
	      if x == "banana":
	      break
	      
SyntaxError: expected an indented block
>>> fruits = ["apple", "banana", "cherry"]
	      
>>> for x in fruits:
	      if x == "banana":
	      break
	      
SyntaxError: expected an indented block
>>> print(x)
	      
a
>>> fruits = ["apple", "banana", "cherry"]
	      
>>> for x in fruits:
	      if x == "banana":
	      continue
	      
SyntaxError: expected an indented block
>>> print(x)
	      
a
>>> for x in range(6):
	      print(x)

	      
0
1
2
3
4
5
>>> for x in range(2, 6):
	      print(x)

	      
2
3
4
5
>>> for x in range(2, 30, 3):
	      print(x)

	      
2
5
8
11
14
17
20
23
26
29
>>> for x in range(6):
	      print(x)
	      else:
	      
SyntaxError: invalid syntax
>>> print("Finally finished!")
	      
Finally finished!
>>> adj = ["red", "big", "tasty"]
	      
>>> fruits = ["apple", "banana", "cherry"]
	      
>>> for x in adj:
	      for y in fruits:
	      print(x, y)
	      
SyntaxError: expected an indented block
>>> def tri_recursion(k):
	      if(k>0):
	      result = k+tri_recursion(k-1)
	      
SyntaxError: expected an indented block
>>> print(result)
	      
Traceback (most recent call last):
  File "<pyshell#136>", line 1, in <module>
    print(result)
NameError: name 'result' is not defined
>>> else:
	      
SyntaxError: invalid syntax
>>> result = 0
	      
>>> return result
	      
SyntaxError: 'return' outside function
>>> print("\n\nRecurrsion Example Results")
	      


Recurrsion Example Results
>>> tri_recursion(6)
	      
Traceback (most recent call last):
  File "<pyshell#141>", line 1, in <module>
    tri_recursion(6)
NameError: name 'tri_recursion' is not defined
>>> fruits = ["apple", "banana", "cherry"]
	      
>>> for x in fruits:
	      print(x)

	      
apple
banana
cherry
>>> def my_function():
	      print("Hello from a function")

	      
>>> def my_function():
	      print("Hello from a function")

	      
>>> my_function()
	      
Hello from a function
>>> def_function(fnama):
	      
SyntaxError: invalid syntax
>>> print(fname + " Refsnes")
	      
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    print(fname + " Refsnes")
NameError: name 'fname' is not defined
>>> my_function('Email")
		
SyntaxError: EOL while scanning string literal
>>> my_function("Email")
		
Traceback (most recent call last):
  File "<pyshell#156>", line 1, in <module>
    my_function("Email")
TypeError: my_function() takes 0 positional arguments but 1 was given
>>> my_function("Tobias")
		
Traceback (most recent call last):
  File "<pyshell#157>", line 1, in <module>
    my_function("Tobias")
TypeError: my_function() takes 0 positional arguments but 1 was given
>>> my_function("Linus")
		
Traceback (most recent call last):
  File "<pyshell#158>", line 1, in <module>
    my_function("Linus")
TypeError: my_function() takes 0 positional arguments but 1 was given
>>> def my_function(country = "Norway"):
		print("I am from " + country)

		
>>> my_function("Sweden")
		
I am from Sweden
>>> my_function("India")
		
I am from India
>>> my_function()
		
I am from Norway
>>> my_function("Brazil")
		
I am from Brazil
>>> def my_function(x):
		return 5 * x

		
>>> print(my_function(3))
		
15
>>> print(my_function(5))
		
25
>>> print(my_function(9))
		
45
>>> def my_function():
		print("Hello from a function")

		
>>> it1 = iter([1, 2, 3])
		
>>> it2 = iter([4, 5, 6])
		
>>> itertools.chain(it1, it2)
		
Traceback (most recent call last):
  File "<pyshell#177>", line 1, in <module>
    itertools.chain(it1, it2)
NameError: name 'itertools' is not defined
>>> [1, 2, 3, 4, 5, 6]
		
[1, 2, 3, 4, 5, 6]
>>> for x, y in itertools.izio(["a", "b", "c"], [1, 2, 3]):print(x, y)

		
Traceback (most recent call last):
  File "<pyshell#180>", line 1, in <module>
    for x, y in itertools.izio(["a", "b", "c"], [1, 2, 3]):print(x, y)
NameError: name 'itertools' is not defined
>>> x = lambda a, b : a * b
		
>>> print(x(5, 6))
		
30
>>> x = lambda a, b, c : a + b + c
		
>>> print(x(5, 6, 2))
		
13
>>> def myfunc(n):
		return lambda a : a * n

		
>>> def my func(n):
		
SyntaxError: invalid syntax
>>> return lambda a : a * n
		
SyntaxError: 'return' outside function
>>> mydoubler = myfunc(2)
		
>>> print(mydoubler(11))
		
22
>>> def my func(n):
		
SyntaxError: invalid syntax
>>> return lambda a : a * n
		
SyntaxError: 'return' outside function
>>> mytripler = myfunc(3)
		
>>> print(mytripler(11))
		
33
>>> def myfunc(n):
		return lambda a : a * n
		mydoubler = myfunc(2)
		mytripler = myfunc(3)

		
>>> print(mydoubler(11))
		
22
>>> print(mytripler(11))
		
33
>>> x = lambda a : a
		
>>> cars = ["Ford", "Volvo", "BMW"]
		
>>> car1 = "Ford":
		
SyntaxError: invalid syntax
>>> car1 = ("Ford")
		
>>> car2 = ("Volvo")
		
>>> CAR3 = ("BMW")
		
>>> x = cars[0]
		
>>> cars[0] = ("Toyota")
		
>>> x = len(cars)
		
>>> for x in cars:
		print(x)

		
Toyota
Volvo
BMW
>>> cars.append("Honda")
		
>>> cars.pop(1)
		
'Volvo'
>>> cars.remove("Volvo")
		
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    cars.remove("Volvo")
ValueError: list.remove(x): x not in list
>>> class Myclass:
		x = 5

		
>>> p1 = MyClass()
		
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    p1 = MyClass()
NameError: name 'MyClass' is not defined
>>> print(p1.x)
		
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    print(p1.x)
NameError: name 'p1' is not defined
>>> classs Person:
		
SyntaxError: invalid syntax
>>> class Person:
		def_init_(self, name, age):
		
SyntaxError: invalid syntax
>>> self.name = name
		
Traceback (most recent call last):
  File "<pyshell#226>", line 1, in <module>
    self.name = name
NameError: name 'name' is not defined
>>> self.age = age
		
Traceback (most recent call last):
  File "<pyshell#227>", line 1, in <module>
    self.age = age
NameError: name 'age' is not defined
>>> p1.age = 40
		
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    p1.age = 40
NameError: name 'p1' is not defined
>>> del p1.age
		
Traceback (most recent call last):
  File "<pyshell#229>", line 1, in <module>
    del p1.age
NameError: name 'p1' is not defined
>>> del p1
		
Traceback (most recent call last):
  File "<pyshell#230>", line 1, in <module>
    del p1
NameError: name 'p1' is not defined
>>> mytuple = ("apple", "banana", "cherry")
		
>>> myit = iter(mytuple)
		
>>> print(next(myit))
		
apple
>>> print(next(myit))
		
banana
>>> print(next(myit))
		
cherry
>>> mystr = ("banana")
		
>>> myit = iter(mystr)
		
>>> print(next(myit))
		
b
>>> print(next(myit))
		
a
>>> print(next(myit))
		
n
>>> print(next(myit))
		
a
>>> print(next(myit))
		
n
>>> print(next(myit))
		
a
>>> mytuple = ("apple", "banana", "cherry")
		
>>> for x in mytuple:
		print(x)

		
apple
banana
cherry
>>> mystr = ("banana")
		
>>> for x in mystr:
		print(x)

		
b
a
n
a
n
a
>>> class MyNumbers:
		def__iter__(self):
		
SyntaxError: invalid syntax
>>> self.a = 1
		
Traceback (most recent call last):
  File "<pyshell#254>", line 1, in <module>
    self.a = 1
NameError: name 'self' is not defined
>>> return self
		
SyntaxError: 'return' outside function
>>> def __next__(self):
		x = self.a
		self.a += 1
		return x

		
>>> myclass = MyNumbers()
		
Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    myclass = MyNumbers()
NameError: name 'MyNumbers' is not defined
>>> myiter = iter(myclass)
		
Traceback (most recent call last):
  File "<pyshell#262>", line 1, in <module>
    myiter = iter(myclass)
NameError: name 'myclass' is not defined
>>> print(next(myiter))
		
Traceback (most recent call last):
  File "<pyshell#263>", line 1, in <module>
    print(next(myiter))
NameError: name 'myiter' is not defined
>>> print(next(myiter))
		
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    print(next(myiter))
NameError: name 'myiter' is not defined
>>> print(next(myiter))
		
Traceback (most recent call last):
  File "<pyshell#265>", line 1, in <module>
    print(next(myiter))
NameError: name 'myiter' is not defined
>>> print(next(myiter))
		
Traceback (most recent call last):
  File "<pyshell#266>", line 1, in <module>
    print(next(myiter))
NameError: name 'myiter' is not defined
>>> print(next(myiter))
		
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    print(next(myiter))
NameError: name 'myiter' is not defined
>>> def greeting(name):
		print("Hello, " + name)

		
>>> import mymodule
		
Traceback (most recent call last):
  File "<pyshell#271>", line 1, in <module>
    import mymodule
ModuleNotFoundError: No module named 'mymodule'
>>> mymodule.greeting("Jonathan")
		
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    mymodule.greeting("Jonathan")
NameError: name 'mymodule' is not defined
>>> person1 = {
	"name": "John",
	"age": 36,
	"country": 'Norway"
	
SyntaxError: EOL while scanning string literal
>>> }
		
SyntaxError: invalid syntax
>>> import mymodule
		
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    import mymodule
ModuleNotFoundError: No module named 'mymodule'
>>> a = mymodule.person1["age"]
		
Traceback (most recent call last):
  File "<pyshell#279>", line 1, in <module>
    a = mymodule.person1["age"]
NameError: name 'mymodule' is not defined
>>> print(a)
		
50
>>> 
