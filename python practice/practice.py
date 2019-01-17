Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 03:13:28) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("hello world")
hello world
>>> favourite_beach = "Bondi"
>>> type(favourite_beach)
<class 'str'>
>>> number_of_people_on_beach = 100000
>>> type(number_of_people_on_beach)
<class 'int'>
>>> beach_is_crowded = True
>>> type(beach_is_crowded)
<class 'bool'>
>>> beach_names = ["Bondi", "Tamarama", "Bronte", "Coogee", "Maroubra"]
>>> type(beach_names)
<class 'list'>
>>> print(beach_names)
['Bondi', 'Tamarama', 'Bronte', 'Coogee', 'Maroubra']
>>> beach_names[0]
'Bondi'
>>> beach_names[0:2]
['Bondi', 'Tamarama']
>>> beach_names.append("Manly")
>>> beach_names[::-1]
['Manly', 'Maroubra', 'Coogee', 'Bronte', 'Tamarama', 'Bondi']
>>> beach = {
	'name' : 'Bondi',
	'crowded' : True,
	'wave_height' : 3,
	'length' : 200
	}
>>> beach
{'name': 'Bondi', 'crowded': True, 'wave_height': 3, 'length': 200}
>>> beach['color'] = "red"
>>> beach['color']
'red'
>>> del beach['color']
>>> beach
{'name': 'Bondi', 'crowded': True, 'wave_height': 3, 'length': 200}
>>> if age_person > 18:
	return "They can drive"
SyntaxError: 'return' outside function
>>> else:
	
SyntaxError: invalid syntax
>>> return "They cannot drive"
SyntaxError: 'return' outside function
>>> number_of_friend = 4
>>> number_of_beach_towels = 5
>>> if number_of_mates > number_of_beach_towels:
	print("Get more towels")

	
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    if number_of_mates > number_of_beach_towels:
NameError: name 'number_of_mates' is not defined
>>> elif number_of_mates == number_of_beach_towels:
	
SyntaxError: invalid syntax
>>> print("Enough towels")
Enough towels
>>> print("To many towels!")
To many towels!
>>> beach_names = ["Bondi", "Tamarama", "Bronte", "Coogee", "Maroubra"]
>>> for name in beach_names :
	print("Let's go swim at {}!".format(name))

	
Let's go swim at Bondi!
Let's go swim at Tamarama!
Let's go swim at Bronte!
Let's go swim at Coogee!
Let's go swim at Maroubra!
>>> def choose_gift(age=18):
	"""
Calculates the cheap gift to give
according to the family member's age
"""
	if age < 18 :
		gift = "educational book"
		else:
			
SyntaxError: invalid syntax
>>> gift = "Crazy socks"
>>> return gift
SyntaxError: 'return' outside function
>>> shoose_gift(18)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    shoose_gift(18)
NameError: name 'shoose_gift' is not defined
>>> choose_gift(18)
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    choose_gift(18)
NameError: name 'choose_gift' is not defined
>>> def choose_gift(age=18):
	"""
Calculates the cheap gift to give
according to the family member's age
"""
if age < 18 :
	
SyntaxError: invalid syntax
>>> gift = "educational book"
>>> else :
	
SyntaxError: invalid syntax
>>> gift = "crazy socks"
>>> return gift
SyntaxError: 'return' outside function
>>> import math
>>> x = math.cos(2 * math.pi)
>>> print(x)
1.0
>>> import pandas as pd
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    import pandas as pd
ModuleNotFoundError: No module named 'pandas'
>>> before = []
>>> after = []
>>> for row in df.values:
	if row[3] == 7:
		if row[2] == 1:
			if row[1] ==1:
				before.append(row[0])
				elif row[1] == 3:
					
SyntaxError: invalid syntax
>>> after.append(row[0])
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    after.append(row[0])
NameError: name 'row' is not defined
>>> var = 4
>>> 8 / 0
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    8 / 0
ZeroDivisionError: division by zero
>>> 8 / 0 =
SyntaxError: invalid syntax
>>> 6 % 3
0
>>> 2 + 2
4
>>> 50 - 5*6
20
>>> (50 - 5*6) / 4
5.0
>>> 8 / 7
1.1428571428571428
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
>>> 6 ** 34
286511799958070431838109696
>>> width = 20
>>> height = 5 * 9
>>> width * height
900
>>> n
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    n
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
>>> 'spam eggs'
'spam eggs'
>>> 'doesn\'t'
"doesn't"
>>> "doesn't"
"doesn't"
>>> '"Yes," they said.'
'"Yes," they said.'
>>> "\"Yes,\" they said."
'"Yes," they said.'
>>> '"Isn\'t," they said.'
'"Isn\'t," they said.'
>>> i = 2568256
>>> print('The value of i is', i)
The value of i is 2568256
>>> a, b = 0, 1
>>> while a < 1000:
	print(a, end=',')
	a, b = b, a+b

	
0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
>>> a, b = 0, 1
>>> while a < 10:
	print(a)
	a, b = b, a+b

	
0
1
1
2
3
5
8
>>> 4 * 3.75 - 1
14.0
>>> print("""\
Usage: thingy [OPTIONS]
-h
-H hostname
""")
Usage: thingy [OPTIONS]
-h
-H hostname

>>> 3 * 'un' + 'ium'
'unununium'
>>> 'py' 'thon'
'python'
>>> text = ('Put several strings within parentheses '
	    'to have them joined together.')
>>> text
'Put several strings within parentheses to have them joined together.'
>>> prefix + 'thon'
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    prefix + 'thon'
NameError: name 'prefix' is not defined
>>> word = 'Python'
>>> word[0]
'P'
>>> word[5]
'n'
>>> word[-1]
'n'
>>> word[-2]
'o'
>>> word[-6]
'P'
>>> word[0:2]
'Py'
>>> word[2:5]
'tho'
>>> word[:2] + word[2:]
'Python'
>>> word[:4] + word[4:]
'Python'
>>> word[:2]
'Py'
>>> word[4:]
'on'
>>> word[-2:]
'on'
>>> 
