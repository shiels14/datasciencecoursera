Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> 
>>> a = random.randit(2, 6)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a = random.randit(2, 6)
AttributeError: module 'random' has no attribute 'randit'
>>> a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
>>> b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
>>> x = [1, 2, 3]
>>> y = [5, 10, 15]
>>> allproducts = [a*b for a in x for b in y]
>>> x = [1, 2, 3]
>>> y = [5, 10, 15]
>>> customlist = [a*b for a in x for b in y if a*b%2 != 0]
>>> a = random.sample(range(100), 5)
>>> def get_integer():
	return int(input("Give me a number: "))

>>> def get_integer():
	return int(input("Give me a number: "))

>>> age = get_integer()
Give me a number: school_year = get_integer()
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    age = get_integer()
  File "<pyshell#17>", line 2, in get_integer
    return int(input("Give me a number: "))
ValueError: invalid literal for int() with base 10: 'school_year = get_integer()'
>>> if age > 15:
	print("You are over the age of 15")
	print("You are in grade " + str(school_year))

	
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    if age > 15:
NameError: name 'age' is not defined
>>> def get_integer(help_text):
	return int(input(help_text))

>>> def get_integer(help_text):
	return int(input(help_text))

>>> age = get_integer("Tell me your age: ")
Tell me your age: 25
>>> school_year = get_integer("What grade are you in? ")
What grade are you in? 17
>>> if age > 25:
	print("You are over the age of 15")

	
>>> print("you are in grade " + str(school_year))
you are in grade 17
>>> def get_integer(help_text+"Give me a number: "):
	
SyntaxError: invalid syntax
>>> def get_integer(help_text="Give me a number: "):
	return int(input(help_text))

>>> def get_integer(help_text="Give me a number: "):
	return int(input(help_text))

>>> age = get_integer("Tell me your age: ")
Tell me your age: 25
>>> if age > 15:
	print("You are over the age of 15")
	print('You are in grade " + str(school_year))
	      
SyntaxError: EOL while scanning string literal
>>> a = [5, 10, 15, 20, 25])
	
SyntaxError: invalid syntax
>>> a = [5, 10, 15, 20,25]
>>> names = set()
>>> names.add("Michelle")
>>> names.add("Robin")
>>> names.add("Michelle")
>>> print(names)
{'Robin', 'Michelle'}
>>> names = ["Michele", "Robin", "Sara" "Michele"]
>>> names = set(names)
>>> names = list(names)
>>> print(names)
['SaraMichele', 'Robin', 'Michele']
>>> teststring = "this is a test"
>>> result = teststring.split("t")
>>> [' ', 'his is a ', 'es', ' ' ]
[' ', 'his is a ', 'es', ' ']
>>> teststring = " this has a lot of spaces and tabs"
>>> result = teststring.split()
>>> ['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
['this', 'has', 'a', 'lot', 'of', 'spaces', 'and', 'tabs']
>>> listofstrings = ['a', 'b', 'c']
>>> a**b**c
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    a**b**c
NameError: name 'c' is not defined
>>> import requests
Traceback (most recent call last):
  File "<pyshell#65>", line 1, in <module>
    import requests
ModuleNotFoundError: No module named 'requests'
>>> url = '
SyntaxError: EOL while scanning string literal
>>> r = requests.get(url)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    r = requests.get(url)
NameError: name 'requests' is not defined
>>> r_html = r.text
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    r_html = r.text
NameError: name 'r' is not defined
>>> soup = BeautifulSoup(r_html)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    soup = BeautifulSoup(r_html)
NameError: name 'BeautifulSoup' is not defined
>>> title = soup.find('span', 'articletitle').string
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    title = soup.find('span', 'articletitle').string
NameError: name 'soup' is not defined
>>> welcome to the Cows and Bulls Game!
SyntaxError: invalid syntax
>>> Enter a number:
	
SyntaxError: invalid syntax
>>> 1234
1234
>>> 2 cows, 0 bulls
SyntaxError: invalid syntax
>>> 1256
1256
>>> 1 cow, 1 bull
SyntaxError: invalid syntax
>>> ...
Ellipsis
>>> def square(num):
	return num * num

>>> if_name_=="_main_":
	
SyntaxError: invalid syntax
>>> user_num = input("Give me a number: ")
Give me a number: 34
>>> print(square(num))
Traceback (most recent call last):
  File "<pyshell#83>", line 1, in <module>
    print(square(num))
NameError: name 'num' is not defined
>>> def square(num):
	return num * num

>>> user_num = input("Give me a number: ")
Give me a number: 34
>>> print(square(num))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(square(num))
NameError: name 'num' is not defined
>>> num=24
>>> a=34.999
>>> result=num*(13/a**2)+1.0
>>> print "Reult:",result
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Reult:",result)?
>>> # Set up calculation inputs
>>> num = 24
>>> a = 34.999
>>> # Calculate result using the Godzilla algorithm
>>> result = num * (13 / a**2) + 1.0
>>> print "Result:", result
SyntaxError: Missing parentheses in call to 'print'. Did you mean print("Result:", result)?
>>> 
